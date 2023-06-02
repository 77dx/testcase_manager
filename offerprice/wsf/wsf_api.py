from . import apiData
from . tools.HandleRequest import HandleRequest
from . tools.HandleMysql import HandleMysql
from . tools.HandleExcel import HandleExcel
from . wsf_sql import WsfSql
from . tools.logger import logger
from . import conf
import time
import datetime
class WsfApi:
    def __init__(self):
        self.req = HandleRequest()
        self.sql = HandleMysql()
        self.csv = HandleExcel()
        self.get_data = WsfSql()

    def user_login(self,account=apiData.user_account):
        """登录网站用户web端
        :return:
        """
        ul = apiData.user_login
        ul["data"] = "principal="+account+"&password=test%40123456&userType=user&isRemember=true&companyName=&origin=web"
        self.res = self.req.run_api(ul)
        apiData.global_params["userId"] = self.res.json()["data"]["userId"]
        self.user_cookies = self.res.cookies.get_dict()
        apiData.global_params["user_cookies"] = self.user_cookies
        if self.res.json()["code"] == "success":
            logger.info("用户%s登录成功"%account)
            logger.info("user_cookies：%s"%self.user_cookies)
            return self.user_cookies
        else:
            logger.error("用户%s登录失败！！！"%account)

    def user_re_orderToken(self,user_cookies):
        """用户下单前获取token
        :return: reOrderToken
        """
        ot = apiData.user_reOrderToken
        self.res = self.req.run_api(ot,user_cookies)
        reOrderToken = self.res.json()["data"]["reOrderToken"]
        apiData.global_params["reOrderToken"] = reOrderToken
        if self.res.json()["code"] == "success":
            logger.info("reOrderToken获取成功")
            return reOrderToken
        else:
            logger.error("reOrderToken获取失败！！！")

    def user_offerMasterList(self,cookies,orderId,master_phone):
        """
        获取订单报价师傅列表
        :param cookies:
        :param orderId:
        :return: 字典{"masterId":"","offerPrice":'"}
        """
        masterId = self.get_data.get_masterUserId(master_phone)
        offerList = apiData.user_offerList
        offerList["data"] = "id=%s" %orderId
        res = self.req.run_api(offerList, cookies=cookies)
        res_data = res.json()
        if res_data["code"] == "success":
            offerList = res_data["data"]["publicOfferList"]
            offerPrice = None
            flag = True
            for offerDetail in offerList:
                if offerDetail["masterId"] == masterId:
                    offerPrice = offerDetail["offerPrice"]
                    flag = False
            logger.info("报价师傅列表查询成功,已找到要报价的师傅")
            if flag:
                logger.error("报价列表未找到要指派的师傅！")
            result = {}
            result["masterId"] = masterId
            result["offerPrice"] = offerPrice
            return result
        else:
            logger.error("报价师傅列表查询失败！！！")

    def user_hireMaster(self,cookies,orderId,master_phone,offerPrice):
        """
        用户指派师傅
        :param cookies:
        :param orderId:
        :param masterId:
        :param offerPrice:
        :return:
        """
        masterId = self.get_data.get_masterUserId(master_phone)
        testData = apiData.user_hireMaster
        testData["data"]= "orderId=%s&masterId=%s&masterPrice=%s" %(orderId,masterId,offerPrice)
        res = self.req.run_api(testData, cookies=cookies)
        if res.json()["code"] == "success":
            sql5 = "SELECT team_name FROM `t_master_information_service`.`master_info` t WHERE t.`master_id`=%s" % masterId
            master_name = self.sql.get_data(sql5)
            logger.info("成功指派师傅为：%s" % master_name)
        else:
            logger.error("用户指派师傅失败！！！")

    def user_payPrice(self,cookies,orderId):
        """
        获取支付价格
        :param cookies:
        :param orderId:
        :return: 支付价格
        """
        payinfoData = apiData.user_payInfo
        payinfoData["data"]["orderId"] = orderId
        res = self.req.run_api(payinfoData, cookies=cookies)
        if res.json()["code"] == "success":
            orderTotalAmount = res.json()["data"]["orderTotalAmount"]
            apiData.global_params["orderTotalAmount"] = orderTotalAmount
            logger.info("获取到支付金额%s" % apiData.global_params["orderTotalAmount"])
            return orderTotalAmount
        else:
            logger.error("获取支付金额失败！！！")

    def user_postOrder(self,cookies,orderId,amount):
        """
        用户提交订单，获取支付id
        :param cookies:
        :param orderId:
        :param amount:
        :return:支付id:paymentId
        """
        postpaymentData = apiData.user_postPayment
        postpaymentData["data"]["id"] = orderId
        postpaymentData["data"]["amount"] = amount
        res = self.req.run_api(postpaymentData, cookies=cookies)
        if res.json()["code"] == "success":
            paymentId = res.json()["data"]["id"]
            apiData.global_params["paymentId"] = paymentId
            logger.info("获取到支付id%s" % apiData.global_params["paymentId"])
            return paymentId
        else:
            logger.error("获取到支付id失败！！！")

    def user_payConfirm(self,cookies,paymentId):
        """
        用户确认支付
        :param cookies:
        :param paymentId:
        :return: None
        """
        payconfirmData = apiData.user_payConfirm
        payconfirmData["data"]["paymentId"] = paymentId
        payconfirmData["data"]["returnUrl"] = "https://test-cashier-desk.wanshifu.com/qrcode/jdpay?paymentId=%s" % paymentId
        res = self.req.run_api(payconfirmData, cookies=cookies)
        if res.json()["retCode"] == "200":
            logger.info("订单已支付成功")
        else:
            logger.error("订单支付失败！！！")

    def user_realPayPrice(self,cookies,orderId,master_phone=apiData.master_account,type="master"):
        masterId = self.get_data.get_masterUserId(master_phone)
        testData = apiData.user_realPayPrice
        testData["data"]= 'orderId=%s&masterId=%s&masterType=%s'%(orderId,masterId,type)
        res = self.req.run_api(testData, cookies=cookies)
        amount = res.json()["data"]["realNeedPayAmount"]
        if res.json()["code"] == "success":
            logger.info("订单实际验收金额为：%s"%amount)
            return amount
        else:
            logger.error("订单支付失败！！！")


    def user_confirmOrder(self,cookies,orderId,master_phone=apiData.master_account,type="master"):
        """
        用户验收订单
        :param cookies:
        :param orderId:
        :param master_phone:
        :param amount:
        :return:
        """
        masterId = self.get_data.get_masterUserId(master_phone)
        amount = self.user_realPayPrice(cookies,orderId,master_phone)
        testData = apiData.user_confirmOrder
        testData["data"]= 'orderId=%s&masterId=%s&amount=%s&masterType=%s&collection=1'%(orderId,masterId,amount,type)
        res = self.req.run_api(testData, cookies=cookies)
        if res.json()["code"] == "success":
            logger.info("订单已验收成功")
        else:
            logger.error("订单验收失败！！！")

    def user_orderList(self,cookies,orderStatus="wait_offer"):
        """
        查询用户订单列表数据
        :param cookies:
        :param orderStatus:wait_offer（待报价），wait_appoint(待指派)，wait_pay（待托管）,serving(服务中)
        :return: orderId_list
        """
        testData = apiData.user_orderList
        t1 = datetime.date.today() + datetime.timedelta(-7)
        t2 = time.strftime("%Y-%m-%d", time.localtime())
        testData["data"] = "page=1&orderStatus=%s&subUserId=all&startTime=%s&endTime=%s"%(orderStatus,t1,t2)
        res = self.req.run_api(testData,cookies=cookies)
        page = res.json()["data"]["totalPages"]
        orderId_list = []
        order_no = []
        for i in range(page):
            testData["data"] = "page=%s&orderStatus=%s&subUserId=all&startTime=%s&endTime=%s" % (i+1,orderStatus, t1, t2)
            res = self.req.run_api(testData, cookies=cookies)
            if res.json()["code"] == "success":
                lists = res.json()["data"]["lists"]
                if len(lists) != 0:
                    for i in lists:
                        orderId = i["orderId"]
                        orderId_list.append(orderId)
                        order_no.append(i["orderNo"])
                logger.info("订单列表查询成功")
            else:
                logger.error("订单列表查询失败！！！")
        print(order_no)
        return orderId_list

    def user_closeOrder(self,cookies,orderList,):
        """
        用户批量关闭订单
        :param cookies:
        :param orderList:
        :return:
        """
        testData = apiData.user_closeOrder
        for orderId in orderList:
            testData["data"] = 'orderId=%s&reason=订单下错了'%orderId
            res = self.req.run_api(testData,cookies)
            if res.json()["code"] == "success":
                logger.info("订单已关闭")
            else:
                logger.error("订单关闭失败！！！")

    def master_login(self,phone=apiData.master_account):
        """
        手机号码加密
        登录师傅，获取token
        :param phone:
        :return:
        """
        res_data = self.req.get(url="http://qa.wanshifu.com/ecb/{0}".format(phone))
        secret = res_data.json()["secret"]
        testData = apiData.master_login
        testData["data"]["phone"] = secret
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            signature = res.json()["data"]["signature"]
            apiData.global_params["signature"] = signature
            logger.info("%s师傅登录成功" % phone)
            return signature
        else:
            logger.info("%s师傅登录失败！！！" % phone)

    def master_offerPrice(self,token,price,orderId,orderServeType,orderModifyTime):
        """
        师傅报价-报价招标
        :param orderId:
        :param orderServeType:
        :param orderModifyTime:
        :return:
        """
        testData = apiData.master_offerPrice
        apiData.master_headers["signature"] = token
        testData["data"]["offerPrice"] = price
        testData["data"]["orderId"] = orderId
        testData["data"]["orderServeType"] = orderServeType
        testData["data"]["orderModifyTime"] = orderModifyTime
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            logger.info("师傅报价成功")
        else:
            logger.error("师傅报价失败！！！")
        return res

    def master_grabOrder_offerPrice(self,token,orderId,orderServeType,orderModifyTime):
        """
        师傅报价-一口价
        :param token:
        :param orderId:
        :param orderServeType:
        :param orderModifyTime:
        :return:
        """
        testData = apiData.master_grabOrder_offerPrice
        apiData.master_headers["signature"] = token
        testData["data"]["orderId"] = orderId
        testData["data"]["orderServeType"] = orderServeType
        testData["data"]["orderModifyTime"] = orderModifyTime
        res = self.req.run_api(testData)
        if res.json()["data"]["grabOrderFlag"] is True:
            logger.info("一口价报价成功")
        else:
            logger.error("一口价报价失败！！！")
        return res

    def master_appointClient(self,token,masterOrderId,master_phone):
        """
        师傅端预约客户
        :param token:
        :param masterOrderId:
        :return:
        """
        masterId = self.get_data.get_masterUserId(master_phone)
        testData = apiData.master_appointClient
        apiData.master_headers["signature"] = token
        testData["data"]["orderId"] = masterOrderId
        testData["data"]["teamVisitMasterIds"][0] = str(masterId)
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            logger.info("师傅预约成功")
        else:
            logger.error("师傅预约失败！！！")
        return res

    def master_doorInService(self,token,masterOrderId,master_phone):
        """
        师傅端上门签到
        :param token:
        :param masterOrderId:
        :return:
        """
        masterId = self.get_data.get_masterUserId(master_phone)
        testData = apiData.master_doorInService
        apiData.master_headers["signature"] = token
        testData["data"]["orderId"] = masterOrderId
        testData["data"]["teamVisitMasterIds"][0] = masterId
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            logger.info("师傅上门签到成功")
        else:
            logger.error("师傅上门签到失败！！！")
        return res

    def master_examineGoods(self,token,masterOrderId,sn=False,needConfirm=False):
        """
        师傅上门拆包验货
        :param token:
        :param masterOrderId:
        :return:
        """
        if sn:
            testData = apiData.master_examineGoods_sn
        else:
            testData = apiData.master_examineGoods
        apiData.master_headers["signature"] = token
        testData["data"]["orderId"] = masterOrderId
        testData["data"]["examineGoodsReceiptIid"] = conf.master_examineGoods["examineGoodsReceiptIid"]
        testData["data"]["examineGoodsIids"] = conf.master_examineGoods["examineGoodsIids"]
        testData["data"]["snBarCodeIids"] = conf.master_examineGoods["snBarCodeIids"]
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            logger.info("师傅上门拆包验货成功")
            if needConfirm:
                self.master_confirmInfo(token, masterOrderId)
        else:
            logger.error("师傅上门拆包验货失败！！！")
        return res

    def master_confirmInfo(self,token,masterOrderId):
        testData = apiData.master_comfirmInfo
        apiData.master_headers["signature"] = token
        testData["data"]["orderId"] = masterOrderId
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            logger.info("师傅现场确认成功")
        else:
            logger.error("师傅现场确认失败！！！")
        return res

    def master_confirmFinish(self,token,orderNo,masterOrderId,rateAward=False):
        """
        师傅确认完工
        :param token:
        :param orderNo:
        :param masterOrderId:
        :return:
        """
        verifyCode = self.get_data.get_user_verifyCode(orderNo)
        if rateAward:
            testData = apiData.master_confirmFinish_rateAward
        else:
            testData = apiData.master_confirmFinish
        apiData.master_headers["signature"] = token
        testData["data"]["orderId"] = masterOrderId
        testData["data"]["verifyCode"] = verifyCode
        res = self.req.run_api(testData)
        if res.json()["code"] == "success":
            logger.info("师傅确认完工成功")
        else:
            logger.error("师傅确认完工失败！！！")
        return res

    def ocs_push_order(self,orderNo):
        """
        人工推单
        """
        phone_list = self.csv.get_data(conf.push_phone_data)
        phones = ";".join(phone_list)
        sql_orderId = 'SELECT order_id FROM t_user_order_service.order_base where order_no = "%s"'%orderNo
        orderId = self.sql.get_data(sql_orderId)["order_id"]
        url = 'https://test-master-ocs.wanshifu.com/capacity/orderDistribute/addHandlePush'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept":"application/json, text/javascript, */*; q=0.01"
        }
        cookies = {
            "AdminName":"%E5%85%9A%E6%97%AD",
            "OcsAdminName":"%E5%85%9A%E6%97%AD",
            "OcsNewToken":"1",
            "OcsToken": "XDlTMlFpB2FRZFUVAWdfbAU9VG0BNFFuB2RcNg83A2kDZgFpCTkAbgI3UGI%3D",
            "commonToken":"XX5WZgFnX3oBbgZvB2YEJlUyCmpbMQU3AGIHY1xhUTFTPVc3UW8EZwAyAzRUalY3UjQEYlsx",
            "testocsCommonId" :"UjFRZAQ9AGIEYFxvA2dXMVM%2BCjkON1dnADdTbAsyBDhTZFBkCDIEM1ZjBmQDZ1Q0ADAEYAtpAjYHNFBvATpValJGUTEEPABjBDNcagM%2BVzFTMApvDmBXZQBrUzkLNQRrUzY%3D",
            "customer_num": "5040",
            "PHPSESSID":"p4479bbqqooslfuo240lb79ep3",
            "token":"f2a32c9b9a0424f1e1977d50000ac7b7"
        }
        data = 'userOrderId={0}&phones={1}'.format(orderId,phone_list)
        r = self.req.run_main(url=url,headers=headers,method='POST',data=data,cookies=cookies)
        logger.info("响应：%s"%r.text)

    def push_order(self,orderNo,master_list):
        """
        人工推单,推单的师傅列表与上不一致
        """
        sql_orderId = 'SELECT order_id FROM t_user_order_service.order_base where order_no = "%s"'%orderNo
        orderId = self.sql.get_data(sql_orderId)["order_id"]
        url = 'https://test-master-ocs.wanshifu.com/capacity/orderDistribute/addHandlePush'
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept":"application/json, text/javascript, */*; q=0.01"
        }
        cookies = {
            "AdminName":"%E5%85%9A%E6%97%AD",
            "OcsAdminName":"%E5%85%9A%E6%97%AD",
            "OcsNewToken":"1",
            "OcsToken": "XDlTMlFpB2FRZFUVAWdfbAU9VG0BNFFuB2RcNg83A2kDZgFpCTkAbgI3UGI%3D",
            "commonToken":"XX5WZgFnX3oBbgZvB2YEJlUyCmpbMQU3AGIHY1xhUTFTPVc3UW8EZwAyAzRUalY3UjQEYlsx",
            "testocsCommonId" :"UjFRZAQ9AGIEYFxvA2dXMVM%2BCjkON1dnADdTbAsyBDhTZFBkCDIEM1ZjBmQDZ1Q0ADAEYAtpAjYHNFBvATpValJGUTEEPABjBDNcagM%2BVzFTMApvDmBXZQBrUzkLNQRrUzY%3D",
            "customer_num": "5040",
            "PHPSESSID":"p4479bbqqooslfuo240lb79ep3",
            "token":"f2a32c9b9a0424f1e1977d50000ac7b7"
        }
        master_list = ";".join(master_list)
        data = 'userOrderId={0}&phones={1}'.format(orderId,master_list)
        r = self.req.run_main(url=url,headers=headers,method='POST',data=data,cookies=cookies)
        logger.info("响应：%s"%r.text)

    def enterprise_login(self):
        testData = apiData.enterprise_login
        res = self.req.run_api(testData)
        if res.json()["code"] == "1":
            enterprise_cookies = res.cookies.get_dict()
            logger.info("总包系统登录成功:"+str(enterprise_cookies))
            return enterprise_cookies
        else:
            logger.error("总包系统登录失败！！！")
        return res

    def enterprise_orderDetail(self,cookies,orderId):
        testData = apiData.enterprise_orderDetail
        testData["url"] = 'https://test-enterprise-api.wanshifu.com/order/orderDetails?orderId='+orderId
        testData["data"] = 'orderId='+orderId
        res = self.req.run_api(testData,cookies=cookies).json()
        if res["code"] == "1":
            logger.info("总包订单订单详情查询成功")
            order_dict = {}
            order_dict["orderId"] = res["data"]["base"]["orderId"]
            order_dict["orderNo"] = res["data"]["base"]["orderNo"]
            order_dict["globalOrderTraceId"] = res["data"]["base"]["globalOrderTraceId"]
            order_dict["serveType"] = res["data"]["base"]["serveType"]
            order_dict["serveTypeId"] = res["data"]["base"]["serveTypeId"]
            order_dict["categoryId"] = res["data"]["base"]["categoryId"]
            order_dict["userName"] = res["data"]["base"]["userName"]
            order_dict["goodsId"] = res["data"]["orderGoods"][0]["goodsId"]
            order_dict["thirdGoodsId"] = res["data"]["orderGoods"][0]["thirdGoodsId"]
            order_dict["buyerAddress"] = res["data"]["customerInfo"]["buyerAddress"]
            order_dict["buyerName"] = res["data"]["customerInfo"]["buyerName"]
            order_dict["buyerPhone"] = res["data"]["customerInfo"]["buyerPhone"]
            order_dict["detailedAddress"] = res["data"]["customerInfo"]["detailedAddress"]
            return order_dict
        else:
            logger.error("总包订单订单详情查询失败！！！")
        return res


    def enterprise_offerPrice(self,cookies,order_dict):
        """
        总包报价
        :param orderId:
        :return:
        """
        testData = apiData.enterprise_offerPrice
        testData["data"]["orderId"] = order_dict["orderId"]
        testData["data"]["orderNo"] = order_dict["orderNo"]
        testData["data"]["globalOrderTraceId"] = order_dict["globalOrderTraceId"]
        testData["data"]["serveType"] = order_dict["serveType"]
        testData["data"]["serveTypeId"] = order_dict["serveTypeId"]
        testData["data"]["categoryId"] = order_dict["categoryId"]
        testData["data"]["orderInitFee"] = str(conf.offerPrice)
        testData["data"]["sellerName"] = order_dict["userName"]
        testData["data"]["goodsInfo"][0]["ogId"]= order_dict["goodsId"]
        testData["data"]["goodsInfo"][0]["thirdOgId"] = order_dict["thirdGoodsId"]
        testData["data"]["detailedAddress"] = order_dict["detailedAddress"]
        testData["data"]["buyerName"] = order_dict["buyerName"]
        testData["data"]["buyerPhone"] = order_dict["buyerPhone"]
        testData["data"]["buyerAddress"] = order_dict["buyerAddress"]
        res = self.req.run_api(testData, cookies=cookies).json()
        if res["code"] == "1":
            logger.info("总包报价成功")
        else:
            logger.error("总包报价失败！！！")
        return res


if __name__ == '__main__':
    f = WsfApi()

    # cookies = f.user_login()

    #推单
    # f.push_order('P61146349276',conf.master_list)

    # 师傅登录
    # token = f.master_login()
    # f.master_appointClient(token,'61021863500','17688968877')

    #总包登录
    enter_cookies = f.enterprise_login()
    order_dict = f.enterprise_orderDetail(enter_cookies,'61189838575')
    f.enterprise_offerPrice(enter_cookies,order_dict)










