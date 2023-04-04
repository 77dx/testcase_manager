from .tools.HandleMysql import HandleMysql
from .tools.HandleRequest import HandleRequest
from .tools.logger import logger
import time

class WsfSql:

    def __init__(self):
        self.do_mysql = HandleMysql()
        self.req = HandleRequest()

    def get_master_orderId(self,orderNo):
        sql = 'SELECT order_id FROM t_master_order_service.order_base WHERE order_no= "%s"' % orderNo
        data = self.do_mysql.get_data(sql)["order_id"]
        return data

    def get_user_orderId(self,orderNo):
        sql = 'SELECT order_id FROM t_user_order_service.order_base where order_no = "%s"' %orderNo
        data = self.do_mysql.get_data(sql)["order_id"]
        return data

    def get_user_orderNo(self,orderId):
        sql = 'SELECT order_no FROM t_user_order_service.order_base where order_id = %s' %orderId
        data = self.do_mysql.get_data(sql)["order_no"]
        return data

    def get_masterUserId(self,phone,type="phone"):
        sql = None
        if type == "phone":
            sql = 'SELECT master_id FROM t_master_information_service.master_info t WHERE t.phone="%s"' %phone
        elif type == "masterName":
            sql = 'SELECT master_id FROM t_master_information_service.master_info t WHERE t.team_name="%s"' % phone
        data = self.do_mysql.get_data(sql)["master_id"]
        return data

    def get_user_verifyCode(self,orderNo):
        sql = 'SELECT service_confirm_code from t_user_order_service.order_demand_relation_info where order_no ="%s"' %orderNo
        data = self.do_mysql.get_data(sql)["service_confirm_code"]
        return data

    def get_enterpriseId(self,enterpriseName):
        sql = 'SELECT enterprise_id FROM t_enterprise_service.enterprise_info WHERE enterprise_name = "%s"' % enterpriseName
        data = self.do_mysql.get_data(sql)["enterprise_id"]
        return data

    def get_categoryId(self,categoryName):
        sql = 'SELECT id FROM t_order_config_service.config_server_category where cn_name="%s"' % categoryName
        data = self.do_mysql.get_data(sql)["id"]
        return data

    def get_goodsId(self,goodsName):
        sql = 'SELECT parent_id,goods_id FROM t_order_config_service.goods where goods_status = 1 and goods_name = "%s" ' % goodsName
        data = self.do_mysql.get_data(sql)
        return data

    def get_serveTypeId(self,serveTypeName):
        sql = 'SELECT serve_id,serve_type_id FROM t_order_config_service.serve WHERE name="%s" AND business_line_id = 1' % serveTypeName
        data = self.do_mysql.get_data(sql)
        return data

    def get_pushMaterIds(self,order_no,type=1):
        sql = 'SELECT t2.master_id FROM `t_master_order_service`.`order_push` t2, `t_master_information_service`.`master_info` t1 WHERE t1.master_id = t2.master_id AND t2.order_id IN ( SELECT order_id FROM t_master_order_service.order_base WHERE order_no = "%s" )  AND t1.master_source = "apps"'%order_no
        data = self.do_mysql.get_data(sql,d_type=type)
        push_master = []
        if type == 1:
            return data[0]["master_id"]
        else:
            for i in data:
                push_master.append(i["master_id"])
        return push_master

    def get_appointMethod(self,orderNo):
        sql = 'SELECT appoint_method FROM t_user_order_service.order_base WHERE order_no = "%s"' %orderNo
        data = self.do_mysql.get_data(sql)["appoint_method"]
        return data

    # 获取师傅报价时的参数
    def get_offerParam(self,master_orderId):
        sql = 'SELECT order_modify_time,serve_type FROM t_master_order_service.order_base WHERE order_id = "%s"'% master_orderId
        data = self.do_mysql.get_data(sql)
        return data

    # 查询已推单师傅
    def get_pushed_masterPhone(self,orderNo,offerNubmer):
        sql = 'SELECT t1.phone FROM `t_master_order_service`.`order_push` t2, `t_master_information_service`.`master_info` t1 WHERE t1.master_id = t2.master_id AND t2.order_id IN ( SELECT order_id FROM t_master_order_service.order_base WHERE order_no = "%s" ) AND t1.master_source = "apps" LIMIT %s' % (
                orderNo, offerNubmer)
        data = self.do_mysql.get_data(sql,d_type=offerNubmer)
        master_list = []
        for i in data:
            master_list.append(i["phone"])
        return master_list

    # 查询总包订单表订单id
    def get_enterprise_orderId(self,orderNo):
        sql = 'SELECT order_id FROM t_enterprise_order_service.order_base WHERE order_no = "%s"' %orderNo
        data = str(self.do_mysql.get_data(sql)["order_id"])
        return data

    # 查询所有的服务类目
    def get_all_category(self):
        sql = 'select id,cn_name from t_order_config_service.config_server_category'
        data = self.do_mysql.get_data(sql,d_type="all")
        return data[:-2]

    # 根据商品信息查询category
    def get_category_from_goodName(self,goodName):
        sql = 'select level_1_id from t_order_config_service.goods where goods_name="%s"'%goodName
        data = str(self.do_mysql.get_data(sql)["level_1_id"])
        return data



if __name__ == '__main__':
    w = WsfSql()
    # r = w.get_master_orderId("P6300000179")
    r = w.get_category_from_goodName("单开门")
    print(r)

