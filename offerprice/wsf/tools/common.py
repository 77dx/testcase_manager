import random
import socket

import numpy as np

class Common:

    # 随机生成手机号
    def Random_Phone(self):
        phone_list =  ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                  "153", "155", "156", "157", "158", "159", "186", "187", "188", "173", "177", "180", "181", "189",
                  "199"]
        random_phone = np.random.choice(phone_list)+''.join(random.choice("0123456789") for i in range(8))
        return random_phone

    # 获取本机ip
    def get_ip(self,domain):
        address = socket.getaddrinfo(domain,'https')
        return address[0][4][0]

    # 检查是否重复
    def checkRepeat(self,one,all):
        if one in all:
            return 1
        return 0

    def getCode(self):
        url = "https://dev-user-site-api.wanshifu.com/common/checkImageCode"
        param = "phone=17688968877&type=forgetWalletPwd&picCode=2"






if __name__ == '__main__':
    c = Common()
    # for i in range(5):
    #     p = c.Random_Phone()
    #     print(p)
    from conf.conf import *
    print(mysql)