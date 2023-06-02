import os
import random

from .tools.common import Common

#用户网站url
user_site = 'https://test-user-site-api.wanshifu.com'
base_url = 'https://test-user.wanshifu.com/login'
user_api = 'https://test-user-api.wanshifu.com'
user_web = 'https://test-user-web-api.wanshifu.com'
user_cashier= 'https://test-base-cashier-service.wanshifu.com'
user_account='17688968877'
pwd = 'test@123456'
walletPwd = '111111'

#总包地址
enterprise_url = 'https://test-enterprise-api.wanshifu.com'
enterprise_account = 'yunbang'
offerPrice = random.randint(21,100)

#师傅端url
master_app = 'https://test-master-app-api.wanshifu.com'
master_order = 'https://test-master-order-api.wanshifu.com'
master_account = 16602069795
price = 50

#ocs url
ocs_url = 'https://test-ocs.wanshifu.com'
ocs_account = "admin"
ocs_pwd = "adminwsf"

curPath = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
screenPath = curPath + '\\screenshot\\'

#临时存放已报价师傅手机
phone_data = curPath + '/data/phone.csv'
#人工配置推单并报价师傅
push_phone_data = curPath + '/data/push_phone.csv'

# 人工配置需要推单的师傅信息
master_list = [
    '13581379111',
    '18500000001',
    '15860669543',
    '18887654321',
    '18033051409',
    '18382059983',
    '18031033107',
    '18329577730',
    '13581379111',
    '15566660045',
    '15566660044',
    '18329577730',
    '13597739618',
    '15860669543',
    '15860669543',
    '13597739627',
    '13143125995',
    '17688968877',
    '18700000004',
    '18100010001',
    '18124114417',
    '18800000004',
    '18577777777',
    '18866660012',
    '15600000111',
    '19000000022',
    '18887654321',
    '17671154607'
]


# 获取当前环境，可预发布数据库和其他迭代环境数据库(多个迭代环境需维护)
current_ip = Common().get_ip(user_site.split("//")[1])
if current_ip == "47.107.250.117":    # 预发布
    mysql={
        "host":"172.18.9.99",
        "user":"user_test",
        "password":"UserTest1246",
        "database":"t_user_order_service",
        "port":3306
    }
    master_examineGoods = {
        "examineGoodsReceiptIid": "5148156112",
        "examineGoodsIids": "5148155958,5148155959,5148155958,5148155959,5148155958",
        "snBarCodeIids": "5148156076"
    }

else:
    mysql={
        "host":"172.18.9.99",   # 迭代测试环境
        "user":"user_test",
        "password":"UserTest1246",
        "database":"t_user_order_service",
        "port":3306
    }
    master_examineGoods = {
        "examineGoodsReceiptIid": "61021872210",
        "examineGoodsIids": "61021872206,61021872207,61021872208",
        "snBarCodeIids": "61021872209"
    }


