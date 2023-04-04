import requests
import json
from .logger import logger
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class HandleRequest:
    def get(self,url,headers=None,data=None,cookies=None):
        res = requests.get(url=url,data=data,headers=headers,cookies=cookies,verify=False)
        return res

    def post(self,url,headers=None,data=None,cookies=None):
        res = requests.post(url=url,data=data,headers=headers,cookies=cookies,verify=False)
        return res

    def run_main(self,url,method,headers=None,data=None,cookies=None):
        logger.info("请求url:"+url)
        logger.info("请求method:" + method)
        logger.info("请求headers:" + str(headers))
        logger.info("请求data:" + str(data))
        if method == "post" or method == "POST":
            if "application/json;charset=utf-8" in headers["Content-Type"]:
                res = self.post(url=url,data=json.dumps(data),headers=headers,cookies=cookies)
            else:
                res = self.post(url=url, data=data.encode('utf-8'), headers=headers,cookies=cookies)
        else:
            res = self.get(url=url,data=data,headers=headers,cookies=cookies)
        return res

    def run_api(self,testData,cookies=None):
        logger.info("接口名称:" + testData["name"])
        res = self.run_main(method=testData["method"], url=testData["url"], headers=testData["headers"],
                                data=testData["data"],cookies=cookies)
        logger.info("接口响应：" + json.dumps(res.json(),ensure_ascii=False))
        return res
