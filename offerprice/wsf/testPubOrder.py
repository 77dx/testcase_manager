from tools.common import Common
from data import apiData
from tools.HandleRequest import HandleRequest
from project.model.wsf_api import WsfApi
from wsf_sql import WsfSql
from tools.logger import logger
import time
import random
import hashlib

class TestPubOrder:
    def __init__(self):
        self.req = HandleRequest()
        self.get_data = WsfSql()
        self.api = WsfApi()
        self.sql = WsfSql()
        self.cookies = self.api.user_login()
        self.reOrderToken = self.api.user_re_orderToken(self.cookies)

    # 生成sign
    def generate_sign(self,reOrderToken,timestamp,toAccountType=None,toAccountId=None,autoReleaseTime=None):
        if autoReleaseTime is None:
            if toAccountType == "enterprise":
                data = "isDefinitePrice=0&reOrderToken=%s&key=wanshifu@20220824&timestamp=%s&toAccountId=%s&toAccountType=%s" %(reOrderToken,timestamp,toAccountId,toAccountType)
            else:
                data = "isDefinitePrice=0&reOrderToken=%s&key=wanshifu@20220824&timestamp=%s" %(reOrderToken,timestamp)
        else:
            if toAccountType == "enterprise":
                data = "autoReleaseTime=%s&isDefinitePrice=0&reOrderToken=%s&key=wanshifu@20220824&timestamp=%s&toAccountId=%s&toAccountType=%s" %(autoReleaseTime,reOrderToken,timestamp,toAccountId,toAccountType)
            else:
                data = "autoReleaseTime=%s&isDefinitePrice=0&reOrderToken=%s&key=wanshifu@20220824&timestamp=%s" %(autoReleaseTime,reOrderToken,timestamp)

        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        sign = md5.hexdigest().upper()
        return sign

    # 下单公共部分-可配置部分商品
    def user_pub_order_base(self,params=None, categoryName=None, serveTypeName=None,goodsName=None):
        categoryId = self.sql.get_categoryId(categoryName)
        goodsId = self.sql.get_goodsId(goodsName)
        serve_type_id = self.sql.get_serveTypeId(serveTypeName)
        params["data"]["orderBase"]["categoryId"] = categoryId
        params["data"]["orderBase"]["serveType"] = serve_type_id["serve_type_id"]
        params["data"]["orderBase"]["serveTypeId"] = serve_type_id["serve_id"]
        if goodsId["parent_id"] == categoryId:
            params["data"]["orderGoodsList"][0]["goodsCategory"] = goodsId["goods_id"]
            params["data"]["orderGoodsList"][0]["categoryChild"] = None
        else:
            params["data"]["orderGoodsList"][0]["goodsCategory"] = goodsId["parent_id"]
            params["data"]["orderGoodsList"][0]["categoryChild"] = goodsId["goods_id"]
        params["data"]["orderExtraData"]["buyerAddress"] = "顺昌路梧桐岛" + str(random.randint(11111,99999))
        params["data"]["orderExtraData"]["buyerPhone"] = Common().Random_Phone()
        params["data"]["orderExtraData"]["buyerName"] = "鱼小七" + str(random.randint(111,999))
        params["data"]["reOrderToken"] = self.reOrderToken
        autoReleaseTime= None
        toAccountType = None
        toAccountId = None
        try:
            autoReleaseTime = params["data"]["autoReleaseTime"]
            toAccountType = params["data"]["toAccountType"]
            toAccountId = params["data"]["toAccountId"]
        except Exception as e:
            logger.error(e)
        finally:
            timestamp = int(round(time.time() * 1000))
            sign = self.generate_sign(self.reOrderToken,timestamp,toAccountType,toAccountId,autoReleaseTime)
            params["data"]["sign"] = sign
            params["data"]["timestamp"] = timestamp
            self.res = self.req.run_api(params, self.cookies)
            orderId = self.res.json()["data"]["orderId"]
            apiData.global_params["orderId"] = orderId
            if self.res.json()["code"] == "success":
                order_no = self.sql.get_user_orderNo(orderId)
                logger.info("订单发布成功,订单号为：%s" % order_no)
                return orderId
            else:
                logger.error("订单发布失败！")

    # 下单公共部分-固定商品(门窗，全屋定制)
    def user_pub_order_fixed(self, params=None,serveTypeName=None, goodsName=None):
        categoryId = self.sql.get_category_from_goodName(goodsName)
        goodsId = self.sql.get_goodsId(goodsName)
        serve_type_id = self.sql.get_serveTypeId(serveTypeName)
        params["data"]["orderBase"]["categoryId"] = categoryId
        params["data"]["orderBase"]["serveType"] = serve_type_id["serve_type_id"]
        params["data"]["orderBase"]["serveTypeId"] = serve_type_id["serve_id"]
        if goodsId["parent_id"] == categoryId:
            params["data"]["orderGoodsList"][0]["goodsCategory"] = goodsId["goods_id"]
            params["data"]["orderGoodsList"][0]["categoryChild"] = None
        else:
            params["data"]["orderGoodsList"][0]["goodsCategory"] = goodsId["parent_id"]
            params["data"]["orderGoodsList"][0]["categoryChild"] = goodsId["goods_id"]
        params["data"]["orderExtraData"]["buyerAddress"] = "顺昌路梧桐岛" + str(random.randint(11111, 99999))
        params["data"]["orderExtraData"]["buyerPhone"] = Common().Random_Phone()
        params["data"]["orderExtraData"]["buyerName"] = "鱼小七" + str(random.randint(111, 999))
        params["data"]["reOrderToken"] = self.reOrderToken
        autoReleaseTime = None
        toAccountType = None
        toAccountId = None
        try:
            autoReleaseTime = params["data"]["autoReleaseTime"]
            toAccountType = params["data"]["toAccountType"]
            toAccountId = params["data"]["toAccountId"]
        except Exception as e:
            logger.error(e)
        finally:
            timestamp = int(round(time.time() * 1000))
            sign = self.generate_sign(self.reOrderToken, timestamp, toAccountType, toAccountId, autoReleaseTime)
            params["data"]["sign"] = sign
            params["data"]["timestamp"] = timestamp
            self.res = self.req.run_api(params, self.cookies)
            orderId = self.res.json()["data"]["orderId"]
            apiData.global_params["orderId"] = orderId
            if self.res.json()["code"] == "success":
                order_no = self.sql.get_user_orderNo(orderId)
                logger.info("订单发布成功,订单号为：%s" % order_no)
                return orderId
            else:
                logger.error("订单发布失败！")

    # 家具-下报价招标订单-师傅/总包(可指定商品)
    def user_pub_jiaju_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if "送货到楼下" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_downstairs
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_downstairs,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "送货到家" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_home
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_home,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "送货到家并安装" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_home_and_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_home_and_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "安装" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "维修" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_repair
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_repair,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "返货" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_return
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_return,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "保养" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_jiaju_maintain
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jiaju_maintain,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 灯具-下报价招标订单(可指定商品)
    def user_pub_dengju_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if "安装" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_dengju_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_dengju_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif "维修" in serveTypeName:
            if enterpriseId is not None:
                params = apiData.user_publish_master_dengju_repair
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_dengju_repair,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 灯具-下单-一口价(灯具一口价的商品属性都不一样，无法指定商品)
    def user_pub_dengju_fixed_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        if serveTypeName == "灯具安装":
            if enterpriseName is not None:
                logger.error('总包，不支持灯具一口价下单')
            else:
                self.user_pub_order_base(params=apiData.user_publish_master_dengju_fixed_install,
                                         categoryName=categoryName,
                                         serveTypeName=serveTypeName, goodsName=goodsName)

    # 健身器材-下报价招标订单-师傅/总包(可指定商品)
    def user_pub_jianshenqicai_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "健身器材送货到家":
            if enterpriseId is not None:
                params = apiData.user_publish_master_jianshenqicai_home
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jianshenqicai_home,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "健身器材送货到家并安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_jianshenqicai_home_and_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jianshenqicai_home_and_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "健身器材安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_jianshenqicai_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jianshenqicai_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "健身器材返货":
            if enterpriseId is not None:
                logger.error('总包不支持健身器材-返货类型')
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_jianshenqicai_return,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 卫浴-下报价招标订单
    def user_pub_weiyu_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "卫浴安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "卫浴测量":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_measure
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_measure,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "卫浴测量并安装(新)":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_measure_and_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_measure_and_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "卫浴维修":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_repair
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_repair,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "卫浴送货到家":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_home
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_home,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "卫浴送货到家并安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_home_and_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_home_and_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "卫浴返货":
            if enterpriseId is not None:
                params = apiData.user_publish_master_weiyu_return
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_weiyu_return,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 晾衣架-下报价招标订单
    def user_pub_liangyijia_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "晾衣架安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_liangyijia_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_liangyijia_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "晾衣架维修":
            if enterpriseId is not None:
                params = apiData.user_publish_master_liangyijia_repaire
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_liangyijia_repaire,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "晾衣架测量":
            if enterpriseId is not None:
                params = apiData.user_publish_master_liangyijia_measure
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_liangyijia_measure,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "晾衣架拆机":
            if enterpriseId is not None:
                params = apiData.user_publish_master_liangyijia_dismantle
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_liangyijia_dismantle,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "晾衣架拆机并返货":
            if enterpriseId is not None:
                params = apiData.user_publish_master_liangyijia_dismantle_and_return
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_liangyijia_dismantle_and_return,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 窗帘-下报价招标订单
    def user_pub_chuanglian_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "窗帘安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_chuanglian_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_chuanglian_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "窗帘维修":
            if enterpriseId is not None:
                params = apiData.user_publish_master_chuanglian_repaire
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_chuanglian_repaire,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "窗帘测量":
            if enterpriseId is not None:
                params = apiData.user_publish_master_chuanglian_measure
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_chuanglian_measure,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "窗帘测量并安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_chuanglian_measure_and_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_chuanglian_measure_and_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 智能锁-下报价招标订单(可指定商品)
    def user_pub_zhinengsuo_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "智能锁安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_zhinengsuo_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_zhinengsuo_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "智能锁维修":
            if enterpriseId is not None:
                params = apiData.user_publish_master_zhinengsuo_repaire
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_zhinengsuo_repaire,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 智能锁-下单一口价订单
    def user_pub_zhinengsuo_fixed_order(self, categoryName=None, serveTypeName=None, goodsName=None,enterpriseName=None):
        orderId = None
        if serveTypeName == "智能锁安装":
            orderId = self.user_pub_order_base(params=apiData.user_publish_master_zhinengsuo_fixed_install,
                                               categoryName=categoryName,
                                               serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 门窗-下报价招标订单(不可指定服务类型和商品，商品为固定的)
    def user_pub_door_order(self,categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "门窗安装":
            params = apiData.user_publish_master_door_install
            if enterpriseId is not None:
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_fixed(params=params,serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_fixed(params=params,serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 全屋定制-下报价招标订单(不可指定商品，商品为固定的)
    def user_pub_customerization_order(self, goodsName="衣柜",serveTypeName=None, enterpriseName=None):
        enterpriseId = None
        res = None
        if enterpriseName is not None:
            enterpriseId = self.get_data.get_enterpriseId(enterpriseName)
        if serveTypeName == "全屋定制安装":
            params = apiData.user_publish_master_customization_install
            if enterpriseId is not None:
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_fixed(params=params, serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_fixed(params=params, serveTypeName=serveTypeName, goodsName=goodsName)
            return orderId

    # 浴霸-下报价招标订单
    def user_pub_yuba_order(self, categoryName=None, serveTypeName=None, goodsName=None, enterpriseName=None):
        enterpriseId = None
        orderId = None
        if enterpriseName is not None:
            enterpriseId = self.sql.get_enterpriseId(enterpriseName)
        if serveTypeName == "浴霸安装":
            if enterpriseId is not None:
                params = apiData.user_publish_master_yuba_install
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_yuba_install,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        elif serveTypeName == "浴霸维修":
            if enterpriseId is not None:
                params = apiData.user_publish_master_yuba_repaire
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                orderId = self.user_pub_order_base(params=params, categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
            else:
                orderId = self.user_pub_order_base(params=apiData.user_publish_master_yuba_repaire,
                                                   categoryName=categoryName,
                                                   serveTypeName=serveTypeName, goodsName=goodsName)
        return orderId

    # 墙纸-下报价招标订单(不可指定商品，商品为固定的)
    def user_pub_qiangzhi_order(self, serveTypeName=None, enterpriseName=None):
        enterpriseId = None
        res = None
        if serveTypeName == "墙纸安装":
            params = apiData.user_publish_master_qiangzhi_install
            params["data"]["orderExtraData"]["buyerAddress"] = "顺昌路梧桐岛" + str(random.randint(11111, 99999))
            params["data"]["orderExtraData"]["buyerPhone"] = Common().Random_Phone()
            params["data"]["orderExtraData"]["buyerName"] = "鱼小七" + str(random.randint(111, 999))
            params["data"]["reOrderToken"] = self.reOrderToken
            autoReleaseTime = params["data"]["autoReleaseTime"]
            sign = self.generate_sign(self.reOrderToken,autoReleaseTime)
            params["data"]["sign"] = sign
            params["data"]["timestamp"] = int(round(time.time()*1000))
            if enterpriseId is not None:
                enterpriseId = self.sql.get_enterpriseId(enterpriseName)
                params["data"]["toAccountId"] = enterpriseId
                params["data"]["toAccountType"] = "enterprise"
                res = self.req.run_api(params, cookies=self.cookies)
            else:
                res = self.req.run_api(params, cookies=self.cookies)
        orderId = res.json()["data"]["orderId"]
        return orderId

if __name__ == '__main__':
    p = TestPubOrder()
    # 家具
    orderId = p.user_pub_jiaju_order(categoryName="家具", serveTypeName="家具安装", goodsName="床垫", enterpriseName=None)
    # 灯具
    # p.user_pub_dengju_order(categoryName="灯具", serveTypeName="灯具安装", goodsName="简易吸顶灯", enterpriseName=None)
    # 卫浴
    # p.user_pub_weiyu_order(categoryName="卫浴", serveTypeName="卫浴安装", goodsName="普通坐便器盖板", enterpriseName=None)
    # 晾衣架
    # p.user_pub_liangyijia_order(categoryName="晾衣架", serveTypeName="晾衣架安装", goodsName="电动晾衣架", enterpriseName=None)
    # 窗帘
    # p.user_pub_chuanglian_order(categoryName="窗帘", serveTypeName="窗帘安装", goodsName="电动布帘", enterpriseName="云邦家居")
    # 智能锁
    # p.user_pub_zhinengsuo_order(categoryName="智能锁", serveTypeName="智能锁安装", goodsName="全自动智能锁", enterpriseName=None)
    # 门窗
    # p.user_pub_door_order(serveTypeName="门窗安装", goodsName="单开门", enterpriseName=None)
    # 全屋定制--下单失败
    # p.user_pub_customerization_order(serveTypeName="全屋定制安装", enterpriseName=None)
    # 浴霸
    # p.user_pub_yuba_order(categoryName="浴霸", serveTypeName="浴霸安装", goodsName="凉霸", enterpriseName=None)
    # 墙纸
    # p.user_pub_qiangzhi_order(serveTypeName="墙纸安装", enterpriseName=None)

