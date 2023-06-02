import random
from .wsf_api import WsfApi
from .wsf_sql import WsfSql
from .tools.HandleExcel import HandleExcel
from .tools.HandleMysql import HandleMysql
from .tools.HandleRequest import HandleRequest
from .tools.logger import logger
from . import conf

class TestScenario:
    def __init__(self):
        self.do_sql = HandleMysql()
        self.do_csv = HandleExcel()
        self.req = HandleRequest()
        self.api = WsfApi()
        self.get_data = WsfSql()

    def masterOfferPrice(self,order,offerNumber=5,price=None,isOrderId=False,auto=True,isGrabOrder=False):
        """
        多个师傅报价--已弃用
        :param order:
        :param offerNumber:
        :param price:
        :param isOrderId:
        :param auto:
        :param isGrabOrder:
        :return:
        """
        #根据order_no查询order_id
        if isOrderId:
            order_no = self.get_data.get_user_orderNo(order)
        else:
            order_no = order
        try:
            # 查询已推单师傅手机号
            phone_list = None
            if auto:
                sql2 = 'SELECT t1.phone FROM `t_master_order_service`.`order_push` t2, `t_master_information_service`.`master_info` t1 WHERE t1.master_id = t2.master_id AND t2.order_id IN ( SELECT order_id FROM t_master_order_service.order_base WHERE order_no = "%s" ) AND t1.master_source = "apps" LIMIT %s' %(order_no,offerNumber)
                phone_list = self.do_sql.get_data(sql2, offerNumber)
                self.api.ocs_push_order(order_no)
                self.do_csv.write_phone(phone_list)
                phone_list = self.do_csv.get_data()
                push_phone = self.do_csv.get_data(conf.push_phone_data)
                phone_list.extend(push_phone)
            else:
                #手动推单
                self.api.ocs_push_order(order_no)
                phone_list = self.do_csv.get_data(conf.push_phone_data)

            # sql查询推单order_id和推单时间
            sql3 = 'SELECT t2.order_id from t_master_order_service.order_push t2 JOIN t_master_information_service.master_info t1 WHERE t1.master_id = t2.master_id AND t2.order_id IN ( SELECT order_id FROM t_master_order_service.order_base WHERE order_no = "%s") AND t1.master_source = "apps" ;' % order_no
            id2 = self.do_sql.get_data(sql3)["order_id"]
            sql4 = "SELECT order_modify_time,serve_type FROM t_master_order_service.order_base WHERE order_id=%s" % id2
            r_order = HandleMysql().get_data(sql4)
            order_modify_time = str(r_order["order_modify_time"])
            order_serve_type = str(r_order["serve_type"])

            # 师傅端批量报价
            count = 0
            success_num = 0
            if phone_list is not None:
                #一口价订单报价
                if isGrabOrder:
                    # 师傅登录
                    signature = self.api.master_login(phone_list[-1])
                    # 师傅报价
                    res_offer = self.api.master_grabOrder_offerPrice(signature, id2, order_serve_type, order_modify_time)
                    # 判断是否报价成功
                    if res_offer.json()["data"] is None:
                        success_num += 1
                #报价招标订单报价
                else:
                    for phone in phone_list:
                        signature = self.api.master_login(phone)
                        random_price = random.randint(price[0],price[1])
                        res_offer = self.api.master_offerPrice(signature,random_price,id2,order_serve_type,order_modify_time)
                        if res_offer.json()["data"] is None:
                            success_num += 1
                        count += 1
                    logger.info("执行进度: %s of " % count + str(len(phone_list)))
                    logger.info("共查找%s个师傅，有%s个师傅报价成功" % (str(len(phone_list)), success_num))
            else:
                logger.error("phone数据为空，无法报价！")

        except Exception as e:
            logger.error("出现异常！ %s" % e)

    def user_getPrice_HireMster(self,cookies,orderId,master_phone):
        """
        用户指派指定的师傅
        :param cookies:
        :param orderId:
        :param master_phone:
        :return:
        """
        hire_master = self.api.user_offerMasterList(cookies, orderId, master_phone)
        self.api.user_hireMaster(cookies, orderId, master_phone, hire_master["offerPrice"])

    def userPayOrder(self,cookies,orderId):
        """
        用户支付订单
        :param cookies:
        :param orderId:
        :return:
        """
        orderTotalAmount = self.api.user_payPrice(cookies, orderId)
        paymentId = self.api.user_postOrder(cookies, orderId, orderTotalAmount)
        self.api.user_payConfirm(cookies, paymentId)

    # 师傅批量报价-新
    def auto_offerPrice(self,orderNo,offerNumber=1,price=None,auto=True):
        # 1. 查询订单类型appoint_method，报价招标：open；一口价：definite_price
        order_appointMethod = self.get_data.get_appointMethod(orderNo)
        # 2. 获取师傅库订单id
        master_orderId = self.get_data.get_master_orderId(orderNo)  # 获取师傅库订单id
        # 3. 根据订单类型报价
        master_list = []
        if auto:
            master_list = self.get_data.get_pushed_masterPhone(orderNo, offerNumber)  # 从推单列表获取前n位师傅的信息
        else:
            master_list = conf.master_list  # 获取手动配置的报价师傅列表
            if len(master_list) > offerNumber:
                master_list = master_list[:offerNumber]
            self.api.push_order(orderNo, master_list)  # 手动推单
        count = 0
        success_num = 0
        if order_appointMethod == "open":    # 报价招标
            # 查询报价必要参数
            offerParams = self.get_data.get_offerParam(master_orderId)
            order_modify_time = str(offerParams["order_modify_time"])
            order_serve_type = str(offerParams["serve_type"])
            # 循环师傅信息进行报价
            for phone in master_list:
                signature = self.api.master_login(phone)
                random_price = random.randint(price[0], price[1])
                res_offer = self.api.master_offerPrice(signature, random_price, master_orderId,order_serve_type, order_modify_time)
                count += 1
                res = res_offer.json()
                if res["status"] == "1" and res["data"] is None:  # 判断报价成功
                    success_num += 1
                    logger.info("师傅%s报价成功，报价进度：%s/%s" % (phone,count, len(master_list)))
                elif res["status"] == "0" or res["data"] is not None:  # 判断报价失败
                    logger.error("师傅%s报价失败，报价进度：%s/%s" % (phone,count, len(master_list)))
            logger.info("报价已结束，成功报价：%s/%s" % (success_num, len(master_list)))
        elif order_appointMethod == "definite_price":        # 一口价
            # 查询报价必要参数
            offerParams = self.get_data.get_offerParam(master_orderId)
            order_modify_time = str(offerParams["order_modify_time"])
            order_serve_type = str(offerParams["serve_type"])
            # 师傅报价
            signature = self.api.master_login(master_list[0])
            res_offer = self.api.master_grabOrder_offerPrice(signature, master_orderId, order_serve_type, order_modify_time)
            if res_offer.json()["data"]["grabOrderFlag"] is True:
                success_num += 1
            logger.info("报价已结束，成功报价：%s/1" % (success_num))

    # 师傅服务完工，家具-安装
    def master_do_work(self, orderNo, master_phone,needConfirm=False,sn=False,rateAward=False):
        signature = self.api.master_login(master_phone)
        master_orderId = self.get_data.get_master_orderId(orderNo)
        # 师傅预约
        self.api.master_appointClient(signature, master_orderId, master_phone)
        # 师傅上门签到
        self.api.master_doorInService(signature, master_orderId, master_phone)
        # 师傅拆包验货
        self.api.master_examineGoods(signature, master_orderId,sn,needConfirm)
        # 师傅确认完工
        self.api.master_confirmFinish(signature, orderNo, master_orderId,rateAward)

    # 总包报价
    def enterpriseOfferPrice(self,orderNo):
        # 查询总包订单库orderId
        enterprise_orderId = self.get_data.get_enterprise_orderId(orderNo)
        # 总包登录，获取cookeis
        cookies = self.api.enterprise_login()
        # 获取总包订单详情，提取参数
        order_dict = self.api.enterprise_orderDetail(cookies,enterprise_orderId)
        # 总包报价
        self.api.enterprise_offerPrice(cookies,order_dict)

if __name__ == '__main__':
    t  = TestScenario()
    # 师傅报价
    # t.masterOfferPrice('P61187960899', isOrderId=False, offerNumber=1, price=[100,100], auto=False, isGrabOrder=False)
    # 新-师傅报价
    # t.auto_offerPrice('P61254391083',offerNumber=1,price=[50,100],auto=False)
    # 师傅完工
    t.master_do_work('P61254415984','13581379111',needConfirm=False,sn=True,rateAward=True)
    # 总包报价
    # orderId = TestPubOrder().user_pub_jiaju_order(categoryName="家具", serveTypeName="家具安装", goodsName="书桌", enterpriseName="云邦家居")
    # orderNo = WsfSql().get_user_orderNo(orderId)
    # t.enterpriseOfferPrice("P61198756683")






