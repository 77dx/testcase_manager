from project.model.wsf_api import WsfApi
from wsf_sql import WsfSql
from testScenario import TestScenario
from testPubOrder import TestPubOrder
from tools.HandleExcel import HandleExcel
from tools.HandleMysql import HandleMysql
from tools.HandleRequest import HandleRequest
from conf import conf
from time import sleep

class TestProcess:
    def __init__(self):
        self.do_sql = HandleMysql()
        self.do_csv = HandleExcel()
        self.req = HandleRequest()
        self.api = WsfApi()
        self.scenario = TestScenario()
        self.pub_order = TestPubOrder()
        self.get_data = WsfSql()

    def order_process(self,master_phone,order_node,user_phone=conf.user_account,num=1):
        """
        order_node: 1(用户下单)，2(师傅报价)，3(指派师傅)，4(支付订单)，5(师傅预约)，6(上门签到)，7(拆包验货)，8(确认完工)，9(确认验收)
        :param user_phone:
        :param master_phone:
        :param order_node:
        :return:
        """
        cookies = self.api.user_login(user_phone)
        for i in range(num):
            # node=1,下单
            orderId = self.pub_order.user_pub_jiaju_order(categoryName="家具", serveTypeName="家具安装", goodsName="床垫",enterpriseName=None)
            orderNo = self.get_data.get_user_orderNo(orderId)
            if order_node == 1:
                continue
            # node=2,报价
            sleep(3)
            self.scenario.auto_offerPrice(orderNo, offerNumber=1, price=[21, 50], auto=False)
            if order_node == 2:
                continue
            # node=3,指派
            self.scenario.user_getPrice_HireMster(cookies, orderId, master_phone)
            if order_node == 3:
                continue
            # node=4,支付
            self.scenario.userPayOrder(cookies, orderId)
            if order_node == 4:
                continue
            # node=5,师傅预约
            sleep(5)
            master_orderId = self.get_data.get_master_orderId(orderNo)
            signature = self.api.master_login(master_phone)
            self.api.master_appointClient(signature, master_orderId, master_phone)
            if order_node == 5:
                continue
            # node=6,上门签到
            self.api.master_doorInService(signature, master_orderId, master_phone)
            if order_node == 6:
                continue
            # node=7,拆包验货
            self.api.master_examineGoods(signature, master_orderId,sn=True,needConfirm=False)
            if order_node == 7:
                continue
            # node=8,确认完工
            self.api.master_confirmFinish(signature, orderNo, master_orderId,rateAward=True)
            if order_node == 8:
                continue
            # node=9,确认验收
            self.api.user_confirmOrder(cookies, orderId, master_phone)


if __name__ == '__main__':
    p = TestProcess()
    # order_node: 1(用户下单)，2(师傅报价)，3(指派师傅)，4(支付订单)，5(师傅预约)，6(上门签到)，7(拆包验货)，8(确认完工)，9(确认验收)
    p.order_process('13581379111',order_node=8,num=10)
