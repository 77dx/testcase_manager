import time
from .conf import *
global_params = {}

#师傅端headers
master_headers = {
    "Content-Type": "application/json;charset=utf-8",
    "apkChannel": "default",
    "phoneType": "android",
    "versionCode": "767",
    "versionName": "7.6.7",
    "signature": None
}

#用户端headers
user_headers= {
    "Content-Type": "application/json;charset=utf-8"
}
user_headers_www= {
    "Content-Type": "application/x-www-form-urlencoded"
}

#api参数
user_login={
    "name": "用户网站登录",
    "url": user_site + '/user/security/login',
    "method": "post",
    "headers": user_headers_www,
    "data":"principal="+user_account+"&password=test%40123456&userType=user&isRemember=True&companyName=&origin=web"
}

user_reOrderToken={
    "name": "获取reOrderToken",
    "url": user_site + '/order/publish/info',
    "method": "post",
    "headers": user_headers_www,
    "data":"action=create"
}

#灯具-下单-报价招标-安装
user_publish_master_dengju_install={
    "name": "灯具-下单-报价招标-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": "cm",
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [{
                "aid": "6098095779",
                "height": None,
                "iid": "6098095777",
                "name": "file_1655364469000",
                "path": "https://qncdn.wanshifu.com/fd31756da19a191909adfde6610d6870",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "note": "特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "盏",
            "userGoodsImageList": [{
                "aid": "6098095751",
                "height": None,
                "iid": "6098095750",
                "name": "file_1655364448000",
                "path": "https://qncdn.wanshifu.com/5469a909a5480a178e5f63e517a4a151",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 414,
            "installRequire": {
                "floorThreePointFiveMeter": "",
                "needDemolish": "",
                "isCeiling": ""
            },
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 193,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "installNum": 1,
            "bulk": "100",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098095751"
                }],
                "environmentImageList": [{
                    "fileType": "image",
                    "attachmentId": "6098095779",
                    "fileName": "file_1655364469000",
                    "fileUrl": "https://qncdn.wanshifu.com/fd31756da19a191909adfde6610d6870"
                }],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "08ba45c39f8144da8a4c66da8f6443ee",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 10,
            "categoryId": 2,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 16:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#灯具-下单给师傅-报价招标-维修
user_publish_master_dengju_repair={
    "name": "灯具-下单-安装-报价",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 416,
            "categoryChild": 309,
            "bulkUnit": "cm",
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "故障描述故障描述",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "处",
            "userGoodsImageList": [{
                "aid": "6098096349",
                "height": None,
                "iid": "6098096347",
                "name": "file_1655364652000",
                "path": "https://qncdn.wanshifu.com/3f8cadc9f140e64de0b0d3786e333789",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "repairPartsDesc": [{
                "key": "0-0",
                "partsName": "灯头",
                "partsNumber": 1,
                "isReturn": 1
            }],
            "isNeedSendBack": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "6098096349",
                "height": None,
                "iid": "6098096347",
                "name": "file_1655364652000",
                "path": "https://qncdn.wanshifu.com/3f8cadc9f140e64de0b0d3786e333789",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098096349"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "34bc561fa47240a4afffeafba1442184",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 11,
            "categoryId": 2,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderRepairPartsRelevance": {
            "returnNote": "收件备注收件备注收件备注收件备注",
            "returnLogistics": ["顺丰速运"],
            "returnAddress": "广东省深圳市宝安区某街道路某花园",
            "returnPhone": "13612345678",
            "returnName": "某某",
            "returnPayMode": "advice_pay",
            "goodsCategoryChildId": 309,
            "goodsCategoryId": 416
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 16:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#灯具-下单给师傅-一口价-安装
user_publish_master_dengju_fixed_install={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": "cm",
            "ancillaryGoods": {},
            "environmentalImgLists": [{
                "aid": "6098096809",
                "height": None,
                "iid": "6098096807",
                "name": "file_1655364937000",
                "path": "https://qncdn.wanshifu.com/11aa241eb0d7ddd8094b7f60b5bb0a85",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "note": None,
            "userVideo": {},
            "number": 3,
            "goodsUnit": "盏",
            "category": None,
            "goodsCategory": 414,
            "categoryChild": 193,
            "goodsName": "商品型号",
            "name": "商品型号",
            "subTotal": "80.00",
            "userGoodsImageList": [{
                "aid": "6098096773",
                "height": None,
                "iid": "6098096772",
                "name": "file_1655364911000",
                "path": "https://qncdn.wanshifu.com/8e01e649542fb6eaef7835575695e026",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {
                "floorThreePointFiveMeter": "",
                "noCeiling": "",
                "noNeedDemolish": ""
            },
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "bulkExtra": {},
            "bulkAttr": {
                "sizeLevel6": ""
            },
            "bulk": "160cm≤直径（或最大边长）＜200cm",
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098096773"
                }],
                "environmentImageList": [{
                    "fileType": "image",
                    "attachmentId": "6098096809",
                    "fileName": "file_1655364937000",
                    "fileUrl": "https://qncdn.wanshifu.com/11aa241eb0d7ddd8094b7f60b5bb0a85"
                }],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "4c699e17f11f428188d5c58dc61107c6",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 10,
            "categoryId": 2,
            "serveType": 4
        },
        "isDefinitePrice": "1",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 16:00:00",
        "orderSpecificInfo": {},
        "definiteTotalPrice": 80,
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#健身器材-送货到家
user_publish_master_jianshenqicai_home={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "weight": "100",
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 45,
            "categoryChild": None,
            "doorHoleInfoList": [],
            "userGoodsImageList": [{
                "aid": "6098086227",
                "height": None,
                "iid": "6098086226",
                "name": "file_1655357924000",
                "path": "https://qncdn.wanshifu.com/6d31e7a617ca0bf55b6dacc7fb021c34",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "bulkUnit": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098086227"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "f7d0ce0a8d104394bc64201f4dffcce3",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 25,
            "categoryId": 10,
            "serveType": 2
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderLogisticsInfo": {
            "isArrived": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 14:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#健身器材-送货到家并安装
user_publish_master_jianshenqicai_home_and_install={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "weight": "100",
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [{
                "aid": "6098076746",
                "height": None,
                "iid": "6098076745",
                "name": "file_1655350502000",
                "path": "https://qncdn.wanshifu.com/1e5049f56d1bc7c03dbc04938a32573b",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 39,
            "categoryChild": None,
            "userGoodsImageList": [{
                "aid": "6098076711",
                "height": None,
                "iid": "6098076709",
                "name": "file_1655350487000",
                "path": "https://qncdn.wanshifu.com/95c3e7a81e49ffa781619610a2dd219a",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "bulkUnit": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098076711"
                }],
                "environmentImageList": [{
                    "fileType": "image",
                    "attachmentId": "6098076746",
                    "fileName": "file_1655350502000",
                    "fileUrl": "https://qncdn.wanshifu.com/1e5049f56d1bc7c03dbc04938a32573b"
                }],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "db4be293cddc46e585c91596d68a90e8",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 26,
            "categoryId": 10,
            "serveType": 3
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderLogisticsInfo": {
            "isArrived": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#健身器材-安装
user_publish_master_jianshenqicai_install={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "weight": "100",
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [{
                "aid": "6098077060",
                "height": None,
                "iid": "6098077059",
                "name": "file_1655350657000",
                "path": "https://qncdn.wanshifu.com/ba8f62c1e7c08d953011a149a5597f14",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 42,
            "categoryChild": None,
            "userGoodsImageList": [{
                "aid": "6098077025",
                "height": None,
                "iid": "6098077023",
                "name": "file_1655350646000",
                "path": "https://qncdn.wanshifu.com/810f28f29153988fd7eefe8c46164fc3",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6098077027",
                "height": None,
                "iid": "6098077026",
                "name": "file_1655350646000",
                "path": "https://qncdn.wanshifu.com/ef36a95de488c2f196bc49dda9ad3b96",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "bulkUnit": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098077025"
                }, {
                    "attachmentId": "6098077027"
                }],
                "environmentImageList": [{
                    "fileType": "image",
                    "attachmentId": "6098077060",
                    "fileName": "file_1655350657000",
                    "fileUrl": "https://qncdn.wanshifu.com/ba8f62c1e7c08d953011a149a5597f14"
                }],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "3531cd3571c14534a212ade42b1a16fe",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 27,
            "categoryId": 10,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#健身器材-返货
user_publish_master_jianshenqicai_return={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "weight": "100",
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 46,
            "categoryChild": None,
            "userGoodsImageList": [{
                "aid": "6098077396",
                "height": None,
                "iid": "6098077388",
                "name": "file_1655350819000",
                "path": "https://qncdn.wanshifu.com/90c08eb7756548af912db8c4bfe388cb",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "bulkUnit": None,
            "isDisassemble": "1",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098077396"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "ef5ef714da8b46acb6d083e0cf8e34b9",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 28,
            "categoryId": 10,
            "serveType": 6
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderReturnLogistics": {
            "receiverAddress": "收货地址",
            "company": "顺丰速运",
            "needMasterPack": "1",
            "needWoodpack": "1",
            "needPack": "1",
            "deliveryMode": "1",
            "insuredAmount": 0,
            "payMethod": "1",
            "receiverPhone": "15841236985",
            "receiverName": "老王"
        },
        "initPayLcsfee": "",
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-16 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#健身器材-调试
user_publish_master_jianshenqicai_debug = {
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data": {
        "serviceInfos": [{
            "userGoodsImgs": {},
            "userGoodsVideo": {},
            "serviceConfig": None,
            "aftersalesGoodsList": None,
            "serviceAttributeDetailDtoList": [{
                "componentsIdWeb": "AddNumberInputItem",
                "note": "商品数量(单位:台)",
                "componentsIdAndroid": "mobilQuantity",
                "defaultValue": "1",
                "componentsIdMP": "",
                "rulesParams": "{\"isReadOnly\":False,\"isRequire\":True,\"limitMax\":999,\"limitMin\":1,\"limitType\":\"number\"}",
                "isShowValue": True,
                "relationId": 3900911,
                "remark": "商品数量(单位:台)",
                "attributeKey": "goods_number",
                "sampleImageAids": "",
                "serviceAttributeValues": [{
                    "note": "",
                    "attributeValueName": "商品数量",
                    "childServiceAttributeDetailDtoList": None,
                    "isShowValue": True,
                    "relationId": 27354542,
                    "sort": 1,
                    "attributeId": 27354135,
                    "attributeValueGroupId": "0",
                    "expand": None,
                    "isDefault": True,
                    "attributeValueId": 27353991,
                    "attributeValueKey": " ",
                    "value": "1"
                }],
                "sort": None,
                "componentsIdH5": "",
                "attributeId": 27354135,
                "unit": "台",
                "isDynamicUpdate": None,
                "attributeTag": "goods_number",
                "isWithoutAttributeName": False,
                "attributeName": "商品数量",
                "placeholder": "商品数量(单位:台)",
                "componentsIdIOS": ""
            }, {
                "componentsIdWeb": "CommonInputItem",
                "note": "",
                "componentsIdAndroid": "mobileInput",
                "defaultValue": "",
                "componentsIdMP": "",
                "rulesParams": "{\"isReadOnly\":False,\"isRequire\":False,\"isSensitiveWords\":True,\"limitMax\":200,\"limitMin\":1,\"limitType\":\"text\"}",
                "isShowValue": True,
                "relationId": 3900913,
                "remark": "商家商品型号信息",
                "attributeKey": "goods_type",
                "sampleImageAids": "",
                "serviceAttributeValues": [{
                    "note": "请输入商品型号",
                    "attributeValueName": "商品型号属性值",
                    "childServiceAttributeDetailDtoList": None,
                    "isShowValue": None,
                    "relationId": 27353867,
                    "sort": 1,
                    "attributeId": 27353865,
                    "attributeValueGroupId": None,
                    "expand": None,
                    "isDefault": None,
                    "attributeValueId": 27353866,
                    "attributeValueKey": None,
                    "value": "商品型号"
                }],
                "sort": None,
                "componentsIdH5": "",
                "attributeId": 27353865,
                "unit": "",
                "isDynamicUpdate": False,
                "attributeTag": "goods_type,goods_name",
                "isWithoutAttributeName": False,
                "attributeName": "商品型号",
                "placeholder": "",
                "componentsIdIOS": ""
            }, {
                "componentsIdWeb": "EnvironmentalImgListsItem",
                "note": "上传如安装环境图、安装说明书等，可提高师傅安装效率（支持图片或PDF文件）",
                "componentsIdAndroid": "mobilPicture",
                "defaultValue": "",
                "componentsIdMP": "",
                "rulesParams": "{\"isReadOnly\":False,\"isRequire\":False,\"limitFormat\":\"image,pdf\",\"limitMax\":500,\"limitMaxFileNumber\":10,\"limitType\":\"file\"}",
                "isShowValue": True,
                "relationId": 3900915,
                "remark": "调试指引文件",
                "attributeKey": "debugging_guide",
                "sampleImageAids": "",
                "serviceAttributeValues": [],
                "sort": None,
                "componentsIdH5": "",
                "attributeId": 27354147,
                "unit": "",
                "isDynamicUpdate": None,
                "attributeTag": "install_guide",
                "isWithoutAttributeName": False,
                "attributeName": "调试指引",
                "placeholder": "上传如安装环境图、安装说明书等，可提高师傅安装效率（支持图片、或PDF文件）",
                "componentsIdIOS": ""
            }, {
                "attributeId": 27354143,
                "attributeName": "特殊要求",
                "serviceAttributeValues": [{
                    "attributeValueId": 27354144,
                    "value": "特殊要求特殊要求"
                }],
                "tag": "special_require"
            }, {
                "componentsIdWeb": "UserGoodsImageListItem",
                "note": "商品图片",
                "componentsIdAndroid": "mobilPicture",
                "defaultValue": "",
                "componentsIdMP": "",
                "rulesParams": "{\"isImageRisk\":True,\"isReadOnly\":False,\"isRequire\":True,\"limitFormat\":\"image\",\"limitMax\":15,\"limitMaxFileNumber\":5,\"limitType\":\"file\"}",
                "isShowValue": True,
                "relationId": 3900920,
                "remark": "商品图片",
                "attributeKey": "goods_image",
                "sampleImageAids": "",
                "serviceAttributeValues": [{
                    "note": "",
                    "attributeValueName": "商品图片",
                    "childServiceAttributeDetailDtoList": None,
                    "isShowValue": True,
                    "relationId": 27353980,
                    "sort": 2,
                    "attributeId": 27353977,
                    "attributeValueGroupId": "0",
                    "expand": {
                        "path": "https://qncdn.wanshifu.com/95c3e7a81e49ffa781619610a2dd219a",
                        "fileName": None,
                        "from": "inside",
                        "type": "image",
                        "aid": 6098076711,
                        "fileId": "6098076711"
                    },
                    "isDefault": True,
                    "attributeValueId": 27353978,
                    "attributeValueKey": " ",
                    "value": "6098076711"
                }],
                "sort": None,
                "componentsIdH5": "",
                "attributeId": 27353977,
                "unit": "",
                "isDynamicUpdate": False,
                "attributeTag": "goods_image",
                "isWithoutAttributeName": False,
                "attributeName": "商品图片",
                "placeholder": "商品图片",
                "componentsIdIOS": ""
            }, {
                "componentsIdWeb": "CommonUploadVideo",
                "note": "商品视频",
                "componentsIdAndroid": "mobilVideo",
                "defaultValue": "",
                "componentsIdMP": "",
                "rulesParams": "{\"isReadOnly\":False,\"isRequire\":False,\"limitDecimalPlaces\":0,\"limitFormat\":\"video\",\"limitMax\":\"500\",\"limitMaxFileNumber\":\"1\",\"limitType\":\"file\"}",
                "isShowValue": True,
                "relationId": 3900922,
                "remark": "商品视频",
                "attributeKey": "goods_video",
                "sampleImageAids": "",
                "serviceAttributeValues": [{
                    "note": " ",
                    "attributeValueName": "上传文件",
                    "childServiceAttributeDetailDtoList": None,
                    "isShowValue": True,
                    "relationId": 34498285,
                    "sort": 1,
                    "attributeId": 34498247,
                    "attributeValueGroupId": "0",
                    "expand": None,
                    "isDefault": True,
                    "attributeValueId": 27354156,
                    "attributeValueKey": "",
                    "value": "上传文件"
                }],
                "sort": None,
                "componentsIdH5": "",
                "attributeId": 34498247,
                "unit": "",
                "isDynamicUpdate": False,
                "attributeTag": "goods_video",
                "isWithoutAttributeName": False,
                "attributeName": "商品视频",
                "placeholder": "商品视频",
                "componentsIdIOS": ""
            }],
            "goodsCategory": [3900050],
            "serviceId": 620002,
            "parentId": 39,
            "uniKey": "lagf2iyq"
        }],
        "toAccountId": None,
        "reOrderToken": "d64bc93709d24c41a940b9e73b49c2b7",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 3900047,
            "categoryId": 10,
            "serveType": 16
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "8",
            "contactPhone": "15915468082",
            "expeditedType": "normal",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-11-14 15:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "182",
        "orderCreateSourceInfo": {
            "deviceId": "5cba6edc28059af3d22f11a7f8bb8fbe",
            "registerChannel": None,
            "origin": "web"
        },
        "sign": "5629FD69DE386F5152BDADC3C5AF476A",
        "timestamp": 1668408071657
    }
}

#家具-送货到楼下
user_publish_master_jiaju_downstairs={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号商品型号",
            "name": "商品型号商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "张",
            "userGoodsImageList": [{
                "aid": "6097980253",
                "height": None,
                "iid": "6097980252",
                "name": "file_1655275776000",
                "path": "https://qncdn.wanshifu.com/cf095247f916d2f5f40f448a156a6a43",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097980255",
                "height": None,
                "iid": "6097980254",
                "name": "file_1655275776000",
                "path": "https://qncdn.wanshifu.com/430d59267f923dae405ef5a1fb89a46f",
                "status": 1,
                "width": None,
                "type": "image"
        }],
            "goodsCategory": 410,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 134,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097980253"
                }, {
                    "attachmentId": "6097980255"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "8f880e3fa0a243c88b923fe43207a2a3",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 1,
            "categoryId": 1,
            "serveType": 1
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "客户旺旺号客户旺旺号",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "isArrived": "2"
        },
        "rateAwardData": {},
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-送货到家
user_publish_master_jiaju_home={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "张",
            "doorHoleInfoList": [],
            "userGoodsImageList": [{
                "aid": "6097985616",
                "height": None,
                "iid": "6097985617",
                "name": "file_1655279213000",
                "path": "https://qncdn.wanshifu.com/e60345954f71236cf9fbf5a3541a9869",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097985619",
                "height": None,
                "iid": "6097985618",
                "name": "file_1655279213000",
                "path": "https://qncdn.wanshifu.com/d91d37ce16280cbc66a77ded49893abd",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 410,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 135,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097985616"
                }, {
                    "attachmentId": "6097985619"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "f462680f3aee4a1b8e3956330462f766",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 2,
            "categoryId": 1,
            "serveType": 2
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 318,
            "buyerWangwang": "客户旺旺号",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderLogisticsInfo": {
            "isArrived": "2"
        },
        "rateAwardData": {},
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-送货到家并安装
user_publish_master_jiaju_home_and_install={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [{
                "aid": "6097986017",
                "height": None,
                "iid": "6097986016",
                "name": "file_1655279848000",
                "path": "https://qncdn.wanshifu.com/924c451f5e3b21be7bdf87705b416a68",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "个",
            "userGoodsImageList": [{
                "aid": "6097986011",
                "height": None,
                "iid": "6097986010",
                "name": "file_1655279830000",
                "path": "https://qncdn.wanshifu.com/828bb9f794c175494a9daec4df069dc7",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097986013",
                "height": None,
                "iid": "6097986012",
                "name": "file_1655279830000",
                "path": "https://qncdn.wanshifu.com/f91fa733bc950cc33df28861faa5a83f",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 408,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 126,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097986011"
                }, {
                    "attachmentId": "6097986013"
                }],
                "environmentImageList": [{
                    "fileType": "image",
                    "attachmentId": "6097986017",
                    "fileName": "file_1655279848000",
                    "fileUrl": "https://qncdn.wanshifu.com/924c451f5e3b21be7bdf87705b416a68"
                }],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "8863057a6d7b4d398263b1cf93d2389d",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 3,
            "categoryId": 1,
            "serveType": 3
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可里小姐",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "originShopId": 316,
            "buyerWangwang": "客户旺旺号",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderLogisticsInfo": {
            "isArrived": "2"
        },
        "rateAwardData": {},
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-安装
user_publish_master_jiaju_install={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data": {
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {
                "containMattress": "",
                "containNightstand": {
                    "number": 1
                }
            },
            "goodsName": "dx秋千",
            "name": "dx秋千",
            "environmentalImgLists": [],
            "note": None,
            "userVideo": {},
            "number": 1,
            "goodsUnit": "张",
            "userGoodsImageList": [{
                "aid": "6097433107",
                "height": None,
                "iid": "6097433106",
                "name": "file_1654843126000",
                "path": "https://qncdn.wanshifu.com/925f01ec82c706204ea975a2f8d0f0a7",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 402,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 68,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": True,
            "goodsAttr": {},
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097433107"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "d09055586abb4ffc9a7459de68eace13",
        "orderBase": {
            "fourthDivisionId": 440306003,
            "thirdDivisionId": 440306,
            "serveTypeId": 4,
            "categoryId": 1,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "clearanceType": "",
            "contactName": "8",
            "contactPhone": "15915468082",
            "buyerAddress": "顺昌路梧桐岛",
            "buyerPhone":"15841023589",
            "buyerName": "鱼小七",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "1"
        },
         "rateAwardData": {
            "rateAwardAmount": 10
        },
        "autoAppointRuleId": "",
        "autoReleaseTime": "2022-08-29 12:00:00",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-维修
user_publish_master_jiaju_repair={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "故障描述故障描述",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "处",
            "userGoodsImageList": [{
                "aid": "6097987124",
                "height": None,
                "iid": "6097987123",
                "name": "file_1655280302000",
                "path": "https://qncdn.wanshifu.com/9ca80952c768fd14b0867180140fda85",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097987127",
                "height": None,
                "iid": "6097987126",
                "name": "file_1655280302000",
                "path": "https://qncdn.wanshifu.com/0efc551052724d7c87ab6f2a56c587a6",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 407,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 118,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "6097987124",
                "height": None,
                "iid": "6097987123",
                "name": "file_1655280302000",
                "path": "https://qncdn.wanshifu.com/9ca80952c768fd14b0867180140fda85",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097987127",
                "height": None,
                "iid": "6097987126",
                "name": "file_1655280302000",
                "path": "https://qncdn.wanshifu.com/0efc551052724d7c87ab6f2a56c587a6",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097987124"
                }, {
                    "attachmentId": "6097987127"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "5368437f45264e3da0aead34025173a1",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 5,
            "categoryId": 1,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可里小姐",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15690876567",
            "originShopId": 316,
            "buyerWangwang": "客户旺旺号",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "autoReleaseTime": "2022-08-29 12:00:00",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-返货
user_publish_master_jiaju_return={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "张",
            "userGoodsImageList": [{
                "aid": "6097988053",
                "height": None,
                "iid": "6097988054",
                "name": "file_1655280806000",
                "path": "https://qncdn.wanshifu.com/325d6fd86e12644fa278f9f2e3989ede",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097988057",
                "height": None,
                "iid": "6097988055",
                "name": "file_1655280806000",
                "path": "https://qncdn.wanshifu.com/fe6ee4a980df002fe261fe70182fbe26",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 403,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 89,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "isDisassemble": "0",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097988053"
                }, {
                    "attachmentId": "6097988057"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "a8ab8f476d7d4ab8a5d7edc18db409a7",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 6,
            "categoryId": 1,
            "serveType": 6
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可西里",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15690876567",
            "originShopId": 318,
            "buyerWangwang": "客户旺旺号",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderReturnLogistics": {
            "receiverAddress": "客户旺旺号客户旺旺号客户旺旺号客户旺旺号客户旺旺号",
            "company": "顺丰速运",
            "needMasterPack": "1",
            "needWoodpack": "1",
            "needPack": "1",
            "deliveryMode": "1",
            "insuredAmount": 0,
            "payMethod": "1",
            "receiverPhone": "15841236985",
            "receiverName": "老王"
        },
        "initPayLcsfee": "",
        "rateAwardData": {},
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "autoReleaseTime": "2022-08-29 12:00:00",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-保养
user_publish_master_jiaju_maintain={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": None,
            "name": None,
            "environmentalImgLists": [],
            "note": "保养需求保养需求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "userGoodsImageList": [{
                "aid": "6097990205",
                "height": None,
                "iid": "6097990204",
                "name": "file_1655281797000",
                "path": "https://qncdn.wanshifu.com/2a21aa77eca25cb1c3a23ccf006cb966",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097990208",
                "height": None,
                "iid": "6097990206",
                "name": "file_1655281797000",
                "path": "https://qncdn.wanshifu.com/51cd296356a29bc4cc7e606fbef862d5",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 403,
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 89,
            "goodsBrand": None,
            "repairAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsAttr": {},
            "maintainType": {
                "wash": ""
            },
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "6097990205",
                "height": None,
                "iid": "6097990204",
                "name": "file_1655281797000",
                "path": "https://qncdn.wanshifu.com/2a21aa77eca25cb1c3a23ccf006cb966",
                "status": 1,
                "width": None,
                "type": "image"
            }, {
                "aid": "6097990208",
                "height": None,
                "iid": "6097990206",
                "name": "file_1655281797000",
                "path": "https://qncdn.wanshifu.com/51cd296356a29bc4cc7e606fbef862d5",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6097990205"
                }, {
                    "attachmentId": "6097990208"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "0b87084d9b194183b7ba37dc8c6d1bd9",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 7,
            "categoryId": 1,
            "serveType": 7
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "origin": "可可里小姐",
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15690876567",
            "originShopId": 316,
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-15 17:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#家具-工程单
user_publish_master_jiaju_gongchengdan ={
    "name": "用户下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": 10401,
            "goodsCategory": 10401,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61167495570"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            },
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "number": 1
        }],
        "toAccountId": None,
        "reOrderToken": "e7de1d2783e44bd9abd35cc93f24ed27",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 69,
            "categoryId": 1,
            "serveType": 15
        },
        "isDefinitePrice": "0",
        "isConvenientOrder": 0,
        "payTradeMode": "tob_pay",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactPhone": "13512341234",
            "contactName": "wudm",
            "expeditedType": "normal",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "customArriveStatus": "1"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2023-01-06 17:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "182",
        "orderEpcGenreData": {
            "serviceItem": "[{\"key\":\"mearsure\",\"name\":\"测量\"},{\"key\":\"install\",\"name\":\"安装\"}]",
            "courseDate": "2023-01-08",
            "constructionDays": "5",
            "daysUnit": "天"
        },
        "orderFileRelaList": [],
        "orderCreateSourceInfo": {
            "deviceId": "5cba6edc28059af3d22f11a7f8bb8fbe",
            "registerChannel": None,
            "origin": "web"
        },
        "accessoriesInfo": [],
        "sign": "7BBEC29B964C707EE9BBC2024B38177B",
        "timestamp": 1672994547516
    }
}

#卫浴-报价-安装
user_publish_master_weiyu_install={
    "name": "卫浴-下单-报价-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "addedService": None,
            "aftersalesGoodsId": None,
            "ancillaryFacilities": None,
            "ancillaryGoods": {},
            "bulk": None,
            "bulkAttr": None,
            "bulkExtra": None,
            "bulkUnit": None,
            "categoryChild": 178,
            "categoryChildName": "手持花洒",
            "categoryName": "花洒",
            "closingDemand": None,
            "createTime": 1679992478000,
            "demolish": None,
            "detailedCategory": None,
            "doorCategoryAttr": None,
            "doorHoleInfoList": None,
            "doorHoleNumber": None,
            "fixedWallAttr": None,
            "galleyDresserDetail": None,
            "goodsAttr": {},
            "goodsBrand": None,
            "goodsCategory": 27,
            "goodsCategoryRemark": None,
            "goodsConditionDetail": None,
            "goodsIncludeDetail": None,
            "goodsInfo": None,
            "goodsName": "dx秋千",
            "goodsUnit": "套",
            "goodsWeight": None,
            "haveCabinet": "without",
            "installAttr": None,
            "installNum": 1,
            "installPosition": None,
            "installRequire": {
                "noNeedDemolish": ""
            },
            "installRequireNum": [],
            "installType": None,
            "isDisassemble": None,
            "isNeedSendBack": None,
            "isNeedSnCode": 1,
            "maintainType": None,
            "measureRequire": None,
            "note": None,
            "number": "1",
            "ogId": 513168256,
            "orderGoodsImage": {
                "environmentImageList": [],
                "goodsImageList": [{
                    "attachmentId": 6097433107
                }],
                "goodsInventoryImageList": [],
                "isDefaultImg": 0
            },
            "repairAttr": None,
            "repairAttrNumber": None,
            "repairPartsDesc": None,
            "responsibleParty": None,
            "texture": None,
            "tipDoorNum": None,
            "ugId": None,
            "updateTime": 1679992478000,
            "userGoodsImageList": [{
                "attachmentId": 6097433107,
                "path": "https://qncdn.wanshifu.com/925f01ec82c706204ea975a2f8d0f0a7"
            }],
            "videoId": None,
            "videoImage": None,
            "videoType": None,
            "videoUrl": None,
            "warmWallOpen": None,
            "weight": None,
            "isDefaultImg": None,
            "environmentalImgLists": [],
            "goodsInventoryImageLists": [],
            "userVideo": {},
            "uniKey": "lfs05idc",
            "name": None
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "reminderTime": None,
            "measureOrderId": None,
            "isOriginalMaster": 0,
            "isAfterOrder": 0,
            "followServeType": None
        },
        "reOrderToken": "db61f4f8b0834a22ac47ec958d2331bb",
        "orderBase": {
            "thirdDivisionId": 440306,
            "serveTypeId": 15,
            "categoryId": 4,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "isConvenientOrder": 0,
        "payTradeMode": "tob_pay",
        "toAccountType": "master",
        "orderExtraData": {
            "contactPhone": "15915468082",
            "contactName": "8",
            "expeditedStatus": "normal",
            "expeditedType": "normal",
            "buyerAddress": "顺昌路梧桐岛96113",
            "buyerPhone": "18999188275",
            "buyerName": "鱼小七711",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": "0",
            "customArriveStatus": "2",
            "packageNum": ""
        },
        "rateAwardData": {
            "rateAwardAmount": 10
        },
        "autoAppointRuleId": "",
        "orderId": "12189495325",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        },
        "accessoriesInfo": []
    }
}
#卫浴-报价-测量
user_publish_master_weiyu_measure={
    "name": "卫浴-下单-报价-测量",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": None,
            "name": None,
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "个",
            "category": None,
            "goodsCategory": 22,
            "categoryChild": 149,
            "doorHoleInfoList": [],
            "userGoodsImageList": [{
                "aid": "6098281508",
                "height": None,
                "iid": "6098281507",
                "name": "file_1655704452000",
                "path": "https://qncdn.wanshifu.com/f3800ba1355c14a04d382ee59f03b56a",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "repairPartsDesc": [],
            "isNeedSendBack": None,
            "measureRequire": {
                "needDemolished": {
                    "cement": ""
                }
            },
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098281508"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "0d6a3164ea70436f84fef83bf4478023",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 49,
            "categoryId": 4,
            "serveType": 9
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-20 14:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#卫浴-报价-测量并安装新
user_publish_master_weiyu_measure_and_install={
    "name": "卫浴-下单-报价-测量",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "addedService": None,
            "ancillaryGoods": {},
            "bulk": "600",
            "bulkAttr": {},
            "bulkExtra": {},
            "bulkUnit": None,
            "category": 22,
            "categoryChild": 150,
            "categoryChildName": "智能坐便器",
            "categoryName": "坐便器/盖板",
            "checkStatus": 1,
            "closingDemand": None,
            "createTime": 1661744596,
            "detailedCategory": None,
            "doorCategory": None,
            "doorCategoryAttr": {},
            "doorHoleInfoList": None,
            "environmentalImgLists": [{
                "attachmentId": 61021314840,
                "fileName": "",
                "fileType": "image",
                "fileUrl": "",
                "path": "https://qncdn.wanshifu.com/b8279123161cfcd5cd80617419a061a1",
                "updateType": None
            }, {
                "attachmentId": 61021314842,
                "fileName": "",
                "fileType": "image",
                "fileUrl": "",
                "path": "https://qncdn.wanshifu.com/aa704a9a13b3f39448442c5b79b84d8b",
                "updateType": None
            }, {
                "attachmentId": 61021314844,
                "fileName": "",
                "fileType": "image",
                "fileUrl": "",
                "path": "https://qncdn.wanshifu.com/53e4e1bc986b0d4b61fed85a09a929e6",
                "updateType": None
            }, {
                "attachmentId": 61021314846,
                "fileName": "",
                "fileType": "image",
                "fileUrl": "",
                "path": "https://qncdn.wanshifu.com/9dcb44011c1dd8684de7b4512f18b14b",
                "updateType": None
            }],
            "fixedWallAttr": {
                "needFixedWall": ""
            },
            "goodsAttr": {
                "ordinary": ""
            },
            "goodsBrand": "热死热特让他人",
            "goodsConditionDetail": [],
            "goodsIncludeDetail": [],
            "goodsInfo": None,
            "goodsUnit": "个",
            "installAttr": None,
            "installRequire": {
                "needDemolish": {
                    "demolishGlass": ""
                }
            },
            "isDefaultImg": None,
            "isDefinitePrice": 1,
            "isDisassemble": "0",
            "isMaintenance": 1,
            "isMeasure": 1,
            "isNeedSnCode": None,
            "isOption": 1,
            "isShowSnButton": None,
            "lampNotDisplayItem": None,
            "maintainType": None,
            "name": "钻石形",
            "note": None,
            "number": 1,
            "orderServeVersion": None,
            "otherInfo": None,
            "picNum": 5,
            "repairType": None,
            "serveCategory": 4,
            "serveCategoryName": "卫浴",
            "serviceInfo": None,
            "status": 1,
            "supportServiceModelIds": None,
            "supportServiceTypeIds": None,
            "thirdLabel": "platform",
            "tipDoorNum": None,
            "ugId": 6486673,
            "updateTime": 1667530548,
            "useCount": 58,
            "userGoodsImageList": [{
                "aid": 61021314823,
                "path": "https://qncdn.wanshifu.com/1450a6fd529e7b5aaa4bdbef017499bd"
            }, {
                "aid": 61021314826,
                "path": "https://qncdn.wanshifu.com/e38b6154ec1f43b9948af11f4d482e29"
            }, {
                "aid": 61021314829,
                "path": "https://qncdn.wanshifu.com/f225513315c79a7843b092a3c9ff6f50"
            }, {
                "aid": 61021314831,
                "path": "https://qncdn.wanshifu.com/f55474a26b695f60330702a791207acb"
            }, {
                "aid": 61021314833,
                "path": "https://qncdn.wanshifu.com/13fa49fbc5de1a15e3d3ecf19de19c64"
            }],
            "userVideo": {},
            "wallFixed": None,
            "weight": None,
            "uniKey": "lagfolje",
            "installNum": 1,
            "installRequireNum": [],
            "goodsName": "钻石形",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": 61021314823
                }, {
                    "attachmentId": 61021314826
                }, {
                    "attachmentId": 61021314829
                }, {
                    "attachmentId": 61021314831
                }, {
                    "attachmentId": 61021314833
                }],
                "environmentImageList": [{
                    "fileType": "image",
                    "updateType": "",
                    "attachmentId": 61021314840,
                    "fileName": "",
                    "fileUrl": "https://qncdn.wanshifu.com/b8279123161cfcd5cd80617419a061a1"
                }, {
                    "fileType": "image",
                    "updateType": "",
                    "attachmentId": 61021314842,
                    "fileName": "",
                    "fileUrl": "https://qncdn.wanshifu.com/aa704a9a13b3f39448442c5b79b84d8b"
                }, {
                    "fileType": "image",
                    "updateType": "",
                    "attachmentId": 61021314844,
                    "fileName": "",
                    "fileUrl": "https://qncdn.wanshifu.com/53e4e1bc986b0d4b61fed85a09a929e6"
                }, {
                    "fileType": "image",
                    "updateType": "",
                    "attachmentId": 61021314846,
                    "fileName": "",
                    "fileUrl": "https://qncdn.wanshifu.com/9dcb44011c1dd8684de7b4512f18b14b"
                }],
                "goodsInventoryImageList": []
            },
            "goodsCategory": 22
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "185b033997d84ab9b0d8aeaa2b44baa5",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 159,
            "categoryId": 4,
            "serveType": 17
        },
        "isDefinitePrice": "0",
        "payTradeMode": "tob_pay",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "expeditedType": "normal",
            "buyerAddress": "新安街道某街道某某路某花园232134",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-11-14 15:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": "5cba6edc28059af3d22f11a7f8bb8fbe",
            "registerChannel": None,
            "origin": "web"
        },
        "sign": "F654FE0E91B29F801B502DA8DC2CC6A8",
        "timestamp": 1668409084906
    }
}
#卫浴-报价-维修
user_publish_master_weiyu_repair={
    "name": "卫浴-下单-报价-维修",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 22,
            "categoryChild": 149,
            "bulkUnit": None,
            "ancillaryGoods": {},
            "weight": None,
            "environmentalImgLists": [],
            "note": "漏水",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "处",
            "userGoodsImageList": [{
                "aid": "61021703635",
                "height": None,
                "iid": "61021703634",
                "name": "file_1662459495000",
                "path": "https://qncdn.wanshifu.com/0b1720c29f95a33987fe2a8c2d5db14f",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {
                "waggle": ""
            },
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "repairPartsDesc": [],
            "isNeedSendBack": None,
            "repairAttrNumber": 1,
            "repareInfo": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61021703635",
                "height": None,
                "iid": "61021703634",
                "name": "file_1662459495000",
                "path": "https://qncdn.wanshifu.com/0b1720c29f95a33987fe2a8c2d5db14f",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61021703635"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "1fad7e5d2f1943dc86061daf03a2ffe8",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 16,
            "categoryId": 4,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-09-06 19:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        },
        "sign": "647D7C06F75255C233CB557F520693CBE",
        "timestamp": 1662459517306
    }
}
#卫浴-报价-送货到家
user_publish_master_weiyu_home={
    "name": "卫浴-下单-报价-送货到家",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "个",
            "category": None,
            "goodsCategory": 22,
            "categoryChild": 277,
            "doorHoleInfoList": [],
            "goodsName": "商品型号",
            "name": "商品型号",
            "userGoodsImageList": [{
                "aid": "6098282679",
                "height": None,
                "iid": "6098282678",
                "name": "file_1655705099000",
                "path": "https://qncdn.wanshifu.com/6aee52a200cc607fce579a142550baa6",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "repairPartsDesc": [],
            "isNeedSendBack": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098282679"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "1b81a776472a48db90651d36563c32f3",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 13,
            "categoryId": 4,
            "serveType": 2
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderLogisticsInfo": {
            "logistics": "",
            "isArrived": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-20 15:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#卫浴-报价-送货到家并安装
user_publish_master_weiyu_home_and_install={
    "name": "卫浴-下单-报价-送货到家并安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "个",
            "category": None,
            "goodsCategory": 22,
            "categoryChild": 149,
            "userGoodsImageList": [{
                "aid": "6098283262",
                "height": None,
                "iid": "6098283260",
                "name": "file_1655705336000",
                "path": "https://qncdn.wanshifu.com/275a4535423a56837de46ba5ad079465",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {
                "needDemolish": {
                    "demolishGlass": ""
                }
            },
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {
                "ordinary": ""
            },
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "repairPartsDesc": [],
            "isNeedSendBack": None,
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098283262"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "0fb69abf49494859beb34fa3dc486f01",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 14,
            "categoryId": 4,
            "serveType": 3
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderLogisticsInfo": {
            "logistics": "",
            "isArrived": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-20 15:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#卫浴-报价-返货
user_publish_master_weiyu_return={
    "name": "卫浴-下单-报价-送货到家并安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "个",
            "category": None,
            "goodsCategory": 22,
            "categoryChild": 149,
            "userGoodsImageList": [{
                "aid": "6098285898",
                "height": None,
                "iid": "6098285897",
                "name": "file_1655706107000",
                "path": "https://qncdn.wanshifu.com/211e4bc3b589aad64934d648d8af9a61",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {
                "ordinary": ""
            },
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "repairPartsDesc": [],
            "isNeedSendBack": None,
            "isDisassemble": "1",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "6098285898"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "9687971d1d2a4b86906896cbdf559532",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 18,
            "categoryId": 4,
            "serveType": 6
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerWangwang": "旺旺",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderReturnLogistics": {
            "receiverAddress": "广东省深圳市宝安区某街道某某路某花园",
            "company": "顺丰速运",
            "needMasterPack": "1",
            "needWoodpack": "0",
            "needPack": "1",
            "deliveryMode": "1",
            "insuredAmount": 0,
            "payMethod": "1",
            "receiverPhone": "15841236985",
            "receiverName": "老王"
        },
        "initPayLcsfee": "",
        "rateAwardData": {},
        "autoReleaseTime": "2022-06-20 15:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#晾衣架-报价-安装
user_publish_master_liangyijia_install={
    "name": "晾衣架-下单-报价-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "userGoodsImageList": [{
                "aid": "61000477172",
                "height": None,
                "iid": "61000477171",
                "name": "file_1658719854000",
                "path": "https://qncdn.wanshifu.com/eb619e4e22b15d6876797d982cab91aa",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 323,
            "installRequire": {
                "noNeedDemolish": "",
                "noCeiling": "",
                "floorThreePointFiveMeter": ""
            },
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": 325,
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000477172"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "87c180f957d0455ca4774600ae11f63b",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 45,
            "categoryId": 17,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#晾衣架-报价-维修
user_publish_master_liangyijia_repaire={
    "name": "晾衣架-下单-报价-维修",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 323,
            "categoryChild": 325,
            "number": 1,
            "bulkUnit": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "故障描述故障描述",
            "userVideo": {},
            "goodsUnit": "台",
            "userGoodsImageList": [{
                "aid": "61000477419",
                "height": None,
                "iid": "61000477418",
                "name": "file_1658720456000",
                "path": "https://qncdn.wanshifu.com/0ba2a2de169127f5a5b45e6b7adfa420",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {
                "noNeedReplaceAccessories": ""
            },
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "repairAttrNumber": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61000477419",
                "height": None,
                "iid": "61000477418",
                "name": "file_1658720456000",
                "path": "https://qncdn.wanshifu.com/0ba2a2de169127f5a5b45e6b7adfa420",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000477419"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "cf4f982b4f5349128f45924bf8e0b529",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 46,
            "categoryId": 17,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#晾衣架-报价-测量
user_publish_master_liangyijia_measure={
    "name": "晾衣架-下单-报价-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 323,
            "categoryChild": 325,
            "doorHoleInfoList": [],
            "userGoodsImageList": [{
                "aid": "61000477609",
                "height": None,
                "iid": "61000477607",
                "name": "file_1658720819000",
                "path": "https://qncdn.wanshifu.com/be097a2c103a47d189660702ed086fa5",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000477609"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "6c9198cd7bfc40d88fd8365ffdd21cd7",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 59,
            "categoryId": 17,
            "serveType": 9
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#晾衣架-报价-拆机
user_publish_master_liangyijia_dismantle={
    "name": "晾衣架-下单-报价-拆机",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
        "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 323,
            "categoryChild": 325,
            "goodsName": "商品型号",
            "name": "商品型号",
            "userGoodsImageList": [{
                "aid": "61000477868",
                "height": None,
                "iid": "61000477867",
                "name": "file_1658721133000",
                "path": "https://qncdn.wanshifu.com/649086bf46ae3aade1bf1e63609dc608",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [{
                "key": "disassemRequire",
                "option": {
                    "key": "floorHeightLS35"
                }
            }],
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000477868"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "3248f55499ec44b1ba5f1199979b39f1",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 60,
            "categoryId": 17,
            "serveType": 11
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 12:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#晾衣架-报价-拆机并返货
user_publish_master_liangyijia_dismantle_and_return={
    "name": "晾衣架-下单-报价-拆机",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "goodsName": "商品型号商品型号",
            "name": "商品型号商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "台",
            "category": None,
            "goodsCategory": 323,
            "categoryChild": 325,
            "userGoodsImageList": [{
                "aid": "61000481670",
                "height": None,
                "iid": "61000481669",
                "name": "file_1658729420000",
                "path": "https://qncdn.wanshifu.com/33454dff20e05a78b52780dc5e585f29",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [{
                "key": "disassemRequire",
                "option": {
                    "key": "floorHeightLS35"
                }
            }],
            "isSelectCategory": None,
            "bulkUnit": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000481670"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "64db62089d2a4bfb81d458b727f425e9",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 61,
            "categoryId": 17,
            "serveType": 12
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "lift": "y"
        },
        "orderReturnLogistics": {
            "receiverAddress": "广东省深圳市宝安区某街道某某路某花园",
            "company": "顺丰速运",
            "needMasterPack": "1",
            "needPack": "1",
            "deliveryMode": "1",
            "insuredAmount": 0,
            "payMethod": "1",
            "receiverPhone": "15180181336",
            "receiverName": "老王"
        },
        "initPayLcsfee": "0",
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 15:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#窗帘-报价-安装
user_publish_master_chuanglian_install={
    "name": "窗帘-下单-报价-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": "m",
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "幅",
            "userGoodsImageList": [{
                "aid": "61000483123",
                "height": None,
                "iid": "61000483122",
                "name": "file_1658731375000",
                "path": "https://qncdn.wanshifu.com/87fa0df60aec154ef7bd7b85ba7b295b",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 329,
            "fixedWallAttr": {},
            "installRequire": {
                "noNeedDemolish": "",
                "floorThreePointFiveMeter": "",
                "noNeedCeramicOpenHole": ""
            },
            "installRequireNum": [],
            "goodsAttr": {
                "canopyCurtain": ""
            },
            "repairAttr": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "categoryChild": 332,
            "installNum": 1,
            "bulk": "100",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000483123"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "1fd3a097cbf947a8828d1fffdc249f92",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 47,
            "categoryId": 18,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 15:00:00",
        "orderSpecificInfo": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#窗帘-报价-维修
user_publish_master_chuanglian_repaire={
    "name": "窗帘-下单-报价-维修",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "故障描述",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "幅",
            "userGoodsImageList": [{
                "aid": "61000483899",
                "height": None,
                "iid": "61000483898",
                "name": "file_1658731885000",
                "path": "https://qncdn.wanshifu.com/e5bc2436701bf0ee5f757740ef00a91d",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 329,
            "fixedWallAttr": {},
            "installRequire": {},
            "installRequireNum": [],
            "goodsAttr": {},
            "repairAttr": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "categoryChild": 331,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61000483899",
                "height": None,
                "iid": "61000483898",
                "name": "file_1658731885000",
                "path": "https://qncdn.wanshifu.com/e5bc2436701bf0ee5f757740ef00a91d",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000483899"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "9fa32758ec1143ddb6c9a730406a0946",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 48,
            "categoryId": 18,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 15:00:00",
        "orderSpecificInfo": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#窗帘-报价-测量
user_publish_master_chuanglian_measure={
    "name": "窗帘-下单-报价-测量",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "category": None,
            "goodsCategory": 329,
            "categoryChild": 333,
            "doorHoleInfoList": [],
            "bulkUnit": "m",
            "goodsConditionDetail": [{
                "key": "windowsNumber",
                "option": {
                    "number": 1,
                    "unit": "个"
                }
            }, {
                "key": "measureType",
                "option": {
                    "key": "generalMeasurement"
                }
            }],
            "userGoodsImageList": [{
                "aid": "61000484171",
                "height": None,
                "iid": "61000484170",
                "name": "file_1658732127000",
                "path": "https://qncdn.wanshifu.com/17134b7bf7c70e8e6913f0f6d93a0457",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "fixedWallAttr": {},
            "installRequire": {},
            "installRequireNum": [],
            "goodsAttr": {},
            "repairAttr": {},
            "haveCabinet": None,
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61000484171",
                "height": None,
                "iid": "61000484170",
                "name": "file_1658732127000",
                "path": "https://qncdn.wanshifu.com/17134b7bf7c70e8e6913f0f6d93a0457",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000484171"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "1db75bf9bbb34a2ebe18054ab9d16964",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 57,
            "categoryId": 18,
            "serveType": 9
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 15:00:00",
        "orderSpecificInfo": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#窗帘-报价-测量并安装
user_publish_master_chuanglian_measure_and_install={
    "name": "窗帘-下单-报价-测量并安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsConditionDetail": [{
                "key": "windowsNumber",
                "option": {
                    "number": 1,
                    "unit": "个"
                }
            }, {
                "key": "measureType",
                "option": {
                    "key": "accurateMeasurement"
                }
            }],
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "category": None,
            "goodsCategory": 329,
            "categoryChild": 356,
            "doorHoleInfoList": [],
            "userGoodsImageList": [{
                "aid": "61000484323",
                "height": None,
                "iid": "61000484322",
                "name": "file_1658732260000",
                "path": "https://qncdn.wanshifu.com/22fdbcb34981bd086ac4386aba5ada0c",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "fixedWallAttr": {},
            "installRequire": {},
            "installRequireNum": [],
            "goodsAttr": {},
            "repairAttr": {},
            "haveCabinet": None,
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61000484323",
                "height": None,
                "iid": "61000484322",
                "name": "file_1658732260000",
                "path": "https://qncdn.wanshifu.com/22fdbcb34981bd086ac4386aba5ada0c",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000484323"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "measureOrderId": None,
            "isAfterOrder": 0,
            "reminderTime": "",
            "followServeType": 0
        },
        "reOrderToken": "156acc0c6b684582a84620d48f726804",
        "orderBase": {
            "thirdOrderNo": "SF1321934960512",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 154,
            "categoryId": 18,
            "serveType": 10
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 15:00:00",
        "orderSpecificInfo": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#智能锁-安装-报价
user_publish_master_zhinengsuo_install={
    "name": "智能锁-下单-报价-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "goodsName": "商品型号",
            "name": "商品型号",
            "environmentalImgLists": [],
            "note": "特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "把",
            "userGoodsImageList": [{
                "aid": "61000472706",
                "height": None,
                "iid": "61000472705",
                "name": "file_1658714865000",
                "path": "https://qncdn.wanshifu.com/c3406c0f04d1981d42d6b811b50ccd78",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 341,
            "fixedWallAttr": {},
            "installRequire": {
                "noNeedOpenHole": ""
            },
            "installRequireNum": [],
            "goodsAttr": {},
            "repairAttr": {},
            "haveCabinet": None,
            "goodsConditionDetail": [{
                "key": "lockBodyType",
                "option": {
                    "key": "ChineseStandardLockBody"
                }
            }, {
                "key": "HeavenEarthHookCondition",
                "option": {
                    "key": "with"
                }
            }],
            "isSelectCategory": None,
            "doorCategoryAttr": {
                "securityDoor": ""
            },
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000472706"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "b2f82bfc79ce4a7bb0ef252e99cdf3c8",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 39,
            "categoryId": 15,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 11:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#智能锁-维修-报价
user_publish_master_zhinengsuo_repaire={
    "name": "智能锁-下单-报价-维修",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 340,
            "categoryChild": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "故障描述",
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "userGoodsImageList": [{
                "aid": "61000472950",
                "height": None,
                "iid": "61000472949",
                "name": "file_1658715331000",
                "path": "https://qncdn.wanshifu.com/03adc088ee0468c85b59899db571bf44",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "fixedWallAttr": {},
            "installRequire": {},
            "installRequireNum": [],
            "goodsAttr": {},
            "repairAttr": {},
            "haveCabinet": None,
            "goodsConditionDetail": [{
                "key": "lockBodyType",
                "option": {
                    "key": "ChineseStandardLockBody"
                }
            }, {
                "key": "HeavenEarthHookCondition",
                "option": {
                    "key": "with"
                }
            }],
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61000472950",
                "height": None,
                "iid": "61000472949",
                "name": "file_1658715331000",
                "path": "https://qncdn.wanshifu.com/03adc088ee0468c85b59899db571bf44",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000472950"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "e8fc9dfae9af4ae59666424f114f94a7",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 40,
            "categoryId": 15,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 11:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#智能锁-安装-一口价
user_publish_master_zhinengsuo_fixed_install={
    "name": "智能锁-下单-安装-一口价",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
        "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 339,
            "categoryChild": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": None,
            "userVideo": {},
            "number": 1,
            "goodsUnit": "把",
            "bulkUnit": None,
            "goodsName": "商品型号",
            "name": "商品型号",
            "subTotal": "94.34",
            "userGoodsImageList": [{
                "aid": "61000473271",
                "height": None,
                "iid": "61000473270",
                "name": "file_1658716035000",
                "path": "https://qncdn.wanshifu.com/2ca8a611bd1c2b8ebc89a116dea0bb87",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "fixedWallAttr": {},
            "installRequire": {
                "noNeedChangeHoleSlot": ""
            },
            "installRequireNum": [],
            "goodsAttr": {},
            "repairAttr": {},
            "haveCabinet": None,
            "goodsConditionDetail": [{
                "key": "lockBodyType",
                "option": {
                    "key": "ChineseStandardLockBody"
                }
            }, {
                "key": "HeavenEarthHookCondition",
                "option": {
                    "key": "with"
                }
            }],
            "isSelectCategory": None,
            "doorCategoryAttr": {
                "solidWoodDoor": ""
            },
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61000473271"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "1431ce6b0e13457c86b586072d3253dc",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 39,
            "categoryId": 15,
            "serveType": 4
        },
        "isDefinitePrice": "1",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 11:00:00",
        "orderSpecificInfo": {},
        "definiteTotalPrice": "94.34",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#门-测量并安装(新)-报价
user_publish_master_door_measure_and_install={
    "name": "门-下单-测量并安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": 846,
            "categoryChild": 648,
            "userGoodsImageList": [{
                "aid": 5169462188,
                "path": "https://qncdn.wanshifu.com/446b262550d2188ff9dd69de6ac7b7fb"
            }],
            "isDefaultImg": 1,
            "uniKey": "l7q0qhsy",
            "ancillaryGoods": {},
            "goodsName": None,
            "name": None,
            "doorHoleNumber": 1,
            "environmentalImgLists": [],
            "note": None,
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "installAttr": {
                "doorOpenMethod": {
                    "key": "singleDoor"
                }
            },
            "isSelectCategory": None,
            "addedService": [{
                "key": "addButtress",
                "option": {
                    "unit": "处",
                    "number": 1
                }
            }, {
                "key": "lockHoleType",
                "option": {
                    "key": "NoneKeyHole"
                }
            }],
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": 5169462188
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            },
            "goodsCategory": 846
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "ba9323c0104c43c797489aa924588e35",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 160,
            "categoryId": 6,
            "serveType": 17
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        },
        "sign": "8249D88197F50D7D8B2C773CAD23A03A",
        "timestamp": 1662458296392
    }
}
#门-安装-报价
user_publish_master_door_install={
    "name": "门-下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "doorHoleInfoList": [{
                "customerGroup": 0,
                "doorHoleHigh": "2000",
                "doorHoleWide": "2000",
                "doorHoleThickness": "1000",
                "doorHoleNo": 1
            }],
            "doorHoleNumber": 1,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "userGoodsImageList": [{
                "aid": "61189970501",
                "height": None,
                "iid": "61189970500",
                "name": "file_1675247129000",
                "path": "https://qncdn.wanshifu.com/b4f9bd39d8701e7df298f453d089f394",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 652,
            "installRequire": {},
            "installRequireNum": [],
            "category": 652,
            "fixedWallAttr": {},
            "categoryChild": 653,
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "addedService": [{
                "key": "demolish",
                "option": {
                    "unit": "套",
                    "number": 1
                }
            }, {
                "key": "setType",
                "option": {
                    "key": "singlePackage",
                    "unit": "套",
                    "number": 1
                }
            }],
            "installAttr": {},
            "doorNormalNum": None,
            "doorAllNum": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "goodsIncludeDetail": [],
            "bulk": None,
            "bulkUnit": None,
            "goodsName": None,
            "name": None,
            "note": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61189970501"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "4b28106c8ffb494ab36c554cc106efe5",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 46,
            "categoryId": 16,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "isConvenientOrder": 0,
        "payTradeMode": "tob_pay",
        "orderExtraData": {
            "contactPhone": "15478965412",
            "contactName": "小王",
            "expeditedType": "normal",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "orderCreateSourceInfo": {
            "deviceId": "5cba6edc28059af3d22f11a7f8bb8fbe",
            "registerChannel": None,
            "origin": "web"
        },
        "accessoriesInfo": [],
        "sign": "2451D01E4AB040644851510ABA683FE9",
        "timestamp": 1675247165368
    }
}
#门-测量-报价
user_publish_master_door_measure={
    "name": "门-下单-测量",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
        "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 652,
            "categoryChild": 653,
            "doorHoleInfoList": [],
            "doorHoleNumber": 1,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "userGoodsImageList": [{
                "aid": "61003037924",
                "height": None,
                "iid": "61003037923",
                "name": "file_1658733445000",
                "path": "https://qncdn.wanshifu.com/37aed21af21c817cadcbb3c0854b14e2",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "addedService": [],
            "installAttr": {},
            "doorNormalNum": None,
            "doorAllNum": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "bulkUnit": None,
            "note": "特殊要求",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61003037924"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "measureOrderId": None,
            "isAfterOrder": 0,
            "reminderTime": "",
            "followServeType": 0
        },
        "reOrderToken": "696a52fc10ff4a849a10e5647b7d1d9d",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 51,
            "categoryId": 6,
            "serveType": 9
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        },
        "sign": "8249D88197F50D7D8B2C773CAD23A03A",
    }
}
#门-维修-报价
user_publish_master_door_repaire={
    "name": "门-下单-维修",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 652,
            "categoryChild": 653,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "userVideo": {},
            "number": 1,
            "goodsUnit": "处",
            "userGoodsImageList": [{
                "aid": "61003038064",
                "height": None,
                "iid": "61003038063",
                "name": "file_1658733589000",
                "path": "https://qncdn.wanshifu.com/4dfea1b9ed3d5e713c5904c194debcbc",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": None,
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "addedService": [],
            "installAttr": {},
            "doorHoleInfoList": [],
            "doorNormalNum": None,
            "doorHoleNumber": 1,
            "doorAllNum": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "bulkUnit": None,
            "note": "故障描述故障描述",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61003038064",
                "height": None,
                "iid": "61003038063",
                "name": "file_1658733589000",
                "path": "https://qncdn.wanshifu.com/4dfea1b9ed3d5e713c5904c194debcbc",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61003038064"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "90c12ab6b11f432bab473253dcfae294",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 58,
            "categoryId": 6,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#全屋定制-安装-报价
user_publish_master_customization_install={
    "name": "全屋定制-下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "createTime": 1635317490000,
            "imageId": 5171245868,
            "imageUrl": "https://qncdn.wanshifu.com/3fdac64e5adff9514ebd04c0e80d882a",
            "isMaintenance": 1,
            "isMeasure": None,
            "isNewAdd": None,
            "isOption": 1,
            "isSupportServerType": 1,
            "supportFixPrice": None,
            "categoryName": "定制柜",
            "goodsCategory": 700,
            "categoryChild": 701,
            "categoryChildName": "衣柜",
            "uniKey": "lg0kacdc",
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "number": 1,
            "goodsUnit": "套",
            "texture": {
                "key": "plateType"
            },
            "isSelectCategory": None,
            "bulk": "20",
            "bulkUnit": "平米",
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": 5171245868
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "isAfterOrder": 0,
            "followServeType": ""
        },
        "reOrderToken": "ebe1053b8b5b44299f87e9d144e87f54",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 52,
            "categoryId": 7,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "isConvenientOrder": 0,
        "payTradeMode": "tob_pay",
        "toAccountType": "",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactPhone": "15478965412",
            "contactName": "小王",
            "expeditedType": "normal",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "1"
        },
        "rateAwardData": {},
        "orderFileRelaList": [{
            "fileId": "61252172915",
            "url": "https://qncdn.wanshifu.com/490f7f4afbe3ffc9f9e31f470f87b6ed",
            "relaType": "drawing_file",
            "fileName": "file_1680510047000",
            "fileType": "image"
        }],
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        },
        "accessoriesInfo": [],
        "sign": "CFC7AE18285891508C1311F00B355D4F",
        "timestamp": 1680510059914
    }
}
#全屋定制-测量-报价
user_publish_master_customization_measure={
    "name": "全屋定制-下单-测量",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "createTime": 1635317490000,
            "imageId": 5171245868,
            "imageUrl": "https://qncdn.wanshifu.com/3fdac64e5adff9514ebd04c0e80d882a",
            "isMaintenance": 1,
            "isMeasure": None,
            "isNewAdd": None,
            "isOption": 1,
            "isSupportServerType": 1,
            "supportFixPrice": 1,
            "categoryName": "定制柜",
            "goodsCategory": 700,
            "categoryChild": 701,
            "categoryChildName": "衣柜",
            "uniKey": "l60icfg5",
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "number": 1,
            "goodsUnit": "套",
            "note": "特殊要求",
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": 5171245868
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "doorNeedAfterService": {
            "measureOrderId": None,
            "isAfterOrder": 0,
            "reminderTime": "",
            "followServeType": 0
        },
        "reOrderToken": "3bfacf2cdab6493b8b7c68a2cff16245",
        "orderBase": {
            "thirdOrderNo": "SF2313696958",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 53,
            "categoryId": 7,
            "serveType": 9
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0",
            "measureWay": "initial_survey"
        },
        "rateAwardData": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#浴霸-安装-报价
user_publish_master_yuba_install={
    "name": "浴霸-下单-安装",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "bulkUnit": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "特殊要求特殊要求",
            "userVideo": {},
            "number": 1,
            "goodsUnit": "套",
            "userGoodsImageList": [{
                "aid": "61003044774",
                "height": None,
                "iid": "61003044773",
                "name": "file_1658741251000",
                "path": "https://qncdn.wanshifu.com/6db2527124b255068ae7551aa332b10a",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "goodsCategory": 450,
            "installRequire": {
                "noNeedDemolish": ""
            },
            "installRequireNum": [],
            "fixedWallAttr": {},
            "categoryChild": None,
            "goodsBrand": "美的",
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "installNum": 1,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61003044774"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "011ec593c96c478397864f32e978420d",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 31,
            "categoryId": 12,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerWangwang": "客户旺旺号",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 18:00:00",
        "orderSpecificInfo": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}
#浴霸-维修-报价
user_publish_master_yuba_repaire={
    "name": "浴霸-下单-维修",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "category": None,
            "goodsCategory": 450,
            "categoryChild": None,
            "bulkUnit": None,
            "ancillaryGoods": {},
            "environmentalImgLists": [],
            "note": "故障描述",
            "userVideo": {},
            "number": 1,
            "goodsUnit": None,
            "userGoodsImageList": [{
                "aid": "61003045007",
                "height": None,
                "iid": "61003045006",
                "name": "file_1658741611000",
                "path": "https://qncdn.wanshifu.com/d6875f88419f5b2bd7454c38af786d7c",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "installRequire": {},
            "installRequireNum": [],
            "fixedWallAttr": {},
            "goodsBrand": "美的",
            "repairAttr": {},
            "goodsAttr": {},
            "cabinetIncludeConfig": {},
            "haveCabinet": None,
            "goodsConditionDetail": [],
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "path": [{
                "aid": "61003045007",
                "height": None,
                "iid": "61003045006",
                "name": "file_1658741611000",
                "path": "https://qncdn.wanshifu.com/d6875f88419f5b2bd7454c38af786d7c",
                "status": 1,
                "width": None,
                "type": "image"
            }],
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": "61003045007"
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            }
        }],
        "toAccountId": None,
        "reOrderToken": "a4df0906bd964928b8440bfdec948900",
        "orderBase": {
            "thirdOrderNo": "SF2721205279",
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 32,
            "categoryId": 12,
            "serveType": 5
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "buyerNote": "请师傅耐心认真的安装",
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "18741023658",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-07-25 18:00:00",
        "orderSpecificInfo": {},
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        }
    }
}

#墙纸-安装-报价
user_publish_master_qiangzhi_install={
    "name": "墙纸-安装-报价",
    "url": user_site + '/order/publish/create',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderGoodsList": [{
            "addedService": None,
            "ancillaryGoods": {},
            "bulk": None,
            "bulkAttr": {},
            "bulkExtra": {},
            "bulkUnit": None,
            "category": 31,
            "categoryChild": None,
            "categoryChildName": None,
            "categoryName": "墙纸",
            "checkStatus": 1,
            "closingDemand": None,
            "createTime": 1662454289,
            "detailedCategory": None,
            "doorCategory": None,
            "doorCategoryAttr": {},
            "doorHoleInfoList": None,
            "environmentalImgLists": [],
            "fixedWallAttr": {},
            "goodsAttr": {},
            "goodsBrand": None,
            "goodsConditionDetail": [],
            "goodsInfo": None,
            "goodsUnit": "㎡",
            "installAttr": None,
            "installRequire": {
                "stickWall": "",
                "noNeedMembrane": ""
            },
            "isDefaultImg": None,
            "isDefinitePrice": 1,
            "isDisassemble": "0",
            "isMaintenance": 1,
            "isMeasure": None,
            "isNeedSnCode": None,
            "isOption": 1,
            "isShowSnButton": None,
            "maintainType": None,
            "name": "墙纸",
            "note": "特殊要求特殊要求特殊要求",
            "number": "100",
            "otherInfo": None,
            "picNum": 1,
            "repairType": None,
            "serveCategory": 8,
            "serveCategoryName": "墙纸",
            "status": 1,
            "thirdLabel": "platform",
            "tipDoorNum": None,
            "ugId": 6486974,
            "updateTime": 1662459106,
            "useCount": 4,
            "userGoodsImageList": [{
                "aid": 61021701633,
                "path": "https://qncdn.wanshifu.com/1a7ea461d8f86bff713edcfaa0ecaf10"
            }],
            "userVideo": {},
            "wallFixed": None,
            "weight": None,
            "uniKey": "l7u4xwji",
            "installNum": 1,
            "installRequireNum": [],
            "goodsName": "墙纸",
            "isSelectCategory": None,
            "videoType": None,
            "videoUrl": None,
            "videoId": None,
            "orderGoodsImage": {
                "goodsImageList": [{
                    "attachmentId": 61021701633
                }],
                "environmentImageList": [],
                "goodsInventoryImageList": []
            },
            "goodsCategory": 31
        }],
        "toAccountId": None,
        "reOrderToken": "a6babcf668724f29ae44f278d6ebe503",
        "orderBase": {
            "fourthDivisionId": 440306001,
            "thirdDivisionId": 440306,
            "serveTypeId": 21,
            "categoryId": 8,
            "serveType": 4
        },
        "isDefinitePrice": "0",
        "orderExtraData": {
            "contactName": "小王",
            "contactPhone": "15478965412",
            "buyerAddress": "新安街道某街道某某路某花园",
            "buyerPhone": "13612345678",
            "buyerName": "万某某",
            "floorNum": "0"
        },
        "orderLogisticsInfo": {
            "trackingIsIdentified": 0,
            "customArriveStatus": "2"
        },
        "rateAwardData": {},
        "autoReleaseTime": "2022-09-09 16:00:00",
        "orderSpecificInfo": {},
        "autoAppointRuleId": "",
        "orderCreateSourceInfo": {
            "deviceId": None,
            "registerChannel": None,
            "origin": "web"
        },
        "sign": "AFD001CBDC17CEC4058B64A",
        "timestamp": 1662707230652
    }
}


#查询报价师傅列表
user_offerList={
    "name": "查询报价师傅列表",
    "url": user_site + '/orders/normal/masterOfferSpecific',
    "method": "post",
    "headers": user_headers_www,
    "data": "id=9219239438"
}
#用户指派师傅
user_hireMaster={
    "name": "用户指派师傅",
    "url": user_site+'/orders/normal/hiremaster',
    "method": "post",
    "headers": user_headers_www,
    "data": {
        "orderId=12184399621&masterId=5168231414&masterPrice=50"
    }
}
#获取支付金额
user_payInfo={
    "name": "获取支付金额",
    "url": user_site+'/orderPay/payinfo',
    "method": "post",
    "headers": user_headers,
    "data": {
        "orderId":"9219239158"
    }
}

user_postPayment={
    "name": "用户提交订单，获取支付id",
    "url": user_site + '/orderPay/postpayment',
    "method": "post",
    "headers": user_headers,
    "data": {
        "id":"9219239158",
        "amount":"37",
        "couponsCode":"",
        "frontCallbackUrl":"https://test-user.wanshifu.com/payment/result/",
        "isNoCancel":"False"
    }
}

user_payConfirm={
    "name": "用户支付订单",
    "url": user_cashier + '/payment/payConfirm',
    "method": "post",
    "headers": user_headers,
    "data": {
        "paymentId":"5177032502",
        "paymentToolNames":"wallet",
        "returnUrl":"https://test-cashier-desk.wanshifu.com/qrcode/jdpay?paymentId=5177032502",
        "walletPwd":walletPwd
    }
}

user_realPayPrice={
    "name": "用户实际验收价格",
    "url": user_site + '/order/normal/confirmPayToMasterBefore',
    "method": "post",
    "headers": user_headers_www,
    "data":"orderId=12184428415&masterId=5168231414&masterType=master"
}

user_confirmOrder={
    "name": "用户验收订单",
    "url": user_site + '/order/normal/confirmPayToMaster',
    "method": "post",
    "headers": user_headers_www,
    "data":"orderId=12184401626&masterId=5168231414&amount=50&masterType=master&collection=1"
}

user_orderList={
    "name": "查询用户订单列表",
    "url": user_site + '/order/merge/list',
    "method": "post",
    "headers": user_headers_www,
    "data": 'orderStatus=wait_offer&subUserId=all&startTime=2021-06-02&endTime=2021-11-29'
}


user_closeOrder={
    "name": "用户关闭订单",
    "url": user_site + '/order/closeorder',
    "method": "post",
    "headers": user_headers_www,
    "data": 'orderId="9219241068"&reason="订单下错了"'
}

master_login={
    "name": "师傅端登录",
    "url": master_app + "/account/login",
    "method": "post",
    "headers": master_headers,
    "data":{
        "apkChannel":"default",
        "phoneType":"android",
        "device_id":"1507bfd3f7351f34ad0",
        "phoneSystemVersion":"11",
        "phoneBrandModel":"realme",
        "signature":"5bb3adde59daede90c9c7786e48386b4",
        "loginCode":"72A1CE33684FA987A59FEB5CC61CC493",
        "deviceId":"1507bfd3f7351f34ad0",
        "province_name":"",
        "timeStamp":"1650252357103",
        "jpushRegId":"1507bfd3f7351f34ad0",
        "password":"72A1CE33684FA987A59FEB5CC61CC493",
        "phoneModel":"RMX3361",
        "phone":master_account,
        "loginWay":"password",
        "regId":"1507bfd3f7351f34ad0"
    }
}

master_offerPrice={
    "name": "师傅端报价招标报价",
    "url": master_order+'/task/ordinaryService/offerPrice',
    "method": "post",
    "headers": master_headers,
    "data":{
        "offerPrice": 80,
        "orderId": "5172235533",
        "offerNote": "",
        "belongUserShare": "0",
        "orderServeType": "4",
        "includeFitting": "False",
        "orderModifyTime": "2021-10-28 15:33:45"
    }
}

master_grabOrder_offerPrice={
    "name": "师傅端一口价报价",
    "url": master_order+'/task/definiteService/grabOrder',
    "method": "post",
    "headers": master_headers,
    "data":{
        "timeStamp":"1650252357103",
        "apkChannel":"default",
        "phoneType":"android",
        "orderId":"5263419968",
        "signature":"5bb3adde59daede90c9c7786e48386b4",
        "belongUserShare":"0",
        "orderModifyTime":"2022-04-18 09:56:02",
        "orderServeType":"4"
    }
}
from datetime import datetime
from datetime import timedelta
tomorrow = (datetime.now()+timedelta(1)).strftime("%Y-%m-%d")
# 师傅预约客户
master_appointClient={
    "name": "师师傅预约客户",
    "url": master_order+'/order/reserveService/addReserveCustomer',
    "method": "post",
    "headers": master_headers,
    "data":{
      "timeStamp": int(round(time.time()*1000)),
      "apkChannel": "default",
      "phoneType": "android",
      # "reserveStartTime": time.strftime("%Y-%m-%d") + " 20:00",
      "reserveStartTime": tomorrow +' 08:00' ,
      # "reserveEndTime": time.strftime("%Y-%m-%d") + " 22:00",
      "reserveEndTime": tomorrow + ' 10:00',
      "teamVisitMasterIds": [
        "5168231414"
      ],
      "orderId": "61021863500",
      "reserveResult": "confirmed_door_time",
      "followSubMasterIds": ""
    }
}
# 师傅上门签到
master_doorInService={
    "name": "师傅上门签到",
    "url": master_order+'/order/doorInService/saveDoorPositionInfo',
    "method": "post",
    "headers": master_headers,
    "data":{
        "apkChannel":"default",
        "phoneType":"android",
        "phoneSystemVersion":"10",
        "orderId":"646545456",
        "phoneBrandModel":"Redmi K30",
        "signature":"4654564546",
        "distanceDifference":"0.0",
        "positionLongitude":"0.0",
        "customerPositionLatitude":"22.555259",
        "customerPositionLongitude":"113.88402",
        "positionCity":"",
        "positionLatitude":"0.0",
        "timeStamp":int(round(time.time()*1000)),
        "positionAddress":"广东省深圳市宝安区某街道某某路某花园",
        "aroundFlag":True,
        "customerPositionMatchLevel":"区县",
        "wearWorkClothes":"0",
        "teamVisitMasterIds": [
            "5168231414"
        ]
    }
}
# 师傅上门拆包验货--有sn
master_examineGoods_sn={
    "name": "师傅上门拆包验货，有sn",
    "url": master_order+'/order/doorInService/addExamineGoods',
    "method": "post",
    "headers": master_headers,
    "data":{
      "timeStamp": int(round(time.time()*1000)),
      "apkChannel": "default",
      "phoneType": "android",
      "examineGoodsReceiptIid": "61245106358",
      "orderId": "61021872154",
      "examineGoodsIids": "1245106213,61245106216,61245106220",
      "signature": "765a71d049170f25d72777daf1acf6dd",
      "snType": "barCode",
      "examineGoodsStatus": "normal",
      "snBarCodeIids": "61021872209",
      "rnFlag":1,
      "snCodeList": [
        {
            "orderGoodsId": 428897,
            "snType": "barCode",
            "snBarCodeIids": "61245106311",
            "snBarCodeNumber": "7898495493895"
        }
      ]
    }
}
# 师傅上门拆包验货--无sn
master_examineGoods={
    "name": "师傅上门拆包验货,无sn",
    "url": master_order+'/order/doorInService/addExamineGoods',
    "method": "post",
    "headers": master_headers,
    "data":{
      "timeStamp": int(round(time.time()*1000)),
      "apkChannel": "default",
      "phoneType": "android",
      "examineGoodsReceiptIid": "61115459989",
      "orderId": "61115459435",
      "examineGoodsIids": "61115459962,61115459963,61115459961",
      "signature": "b018ee7c1ad38f73f0c71887f8f49130",
      "snType": "none",
      "examineGoodsStatus": "normal"
    }
}
master_comfirmInfo={
    "name": "师傅现场确认签名",
    "url": master_order+'/order/doorInService/saveConstructConfirmInfo',
    "method": "post",
    "headers": master_headers,
    "data":{
        "timeStamp": int(round(time.time()*1000)),
        "apkChannel": "default",
        "protocolId": 15,
        "phoneType": "android",
        "signTime": int(round(time.time()*1000)),
        "orderId": "6011428161",
        "signature": "186bddeab57db92d9c4e5461b2ce0d74",
        "confirmStatus": "normal",
        "signImgIid": "61145784045"
        }
}

# 师傅确认完工
master_confirmFinish={
    "name": "师傅确认完工,无好评返现",
    "url": master_order+'/order/finishService/addConfirmFinish',
    "method": "post",
    "headers": master_headers,
    "data":{
        "timeStamp":int(round(time.time()*1000)),
        "apkChannel":"default",
        "phoneType":"android",
        "verifyCode":"123456",
        "orderId":"465456456",
        "serveFinishIids":"5148200475,5148200474",
        "serveSignIids":"5148200484",
        "wearWorkClothes":0,
        "rateAwardFlag":False
    }
}
# 师傅确认完工-有好评返现
master_confirmFinish_rateAward={
    "name": "师傅确认完工-有好评返现",
    "url": master_order+'/order/finishService/addConfirmFinish',
    "method": "post",
    "headers": master_headers,
    "data":{
      "apkChannel": "default",
      "phoneType": "android",
      "verifyCode": "164708",
      "orderId": "61115291330",
      "serveFinishIids": "61115291653,61115291654",
      "timeStamp": int(round(time.time()*1000)),
      "awardImageIids": "61115291666",
      "serveSignIids": "61115291659",
      "wearWorkClothes": 0,
      "rateAwardFlag": True
    }
}

# 总包系统-登录
enterprise_login = {
    "name": "总包系统-登录",
    "url": enterprise_url+'/auth/login',
    "method": "post",
    "headers": user_headers_www,
    "data":"account="+enterprise_account+"&pwd=dGVzdEAxMjM0NTY%3D"
}

#总包-查询订单详情
enterprise_orderDetail = {
    "name": "总包系统-查询订单详情",
    "url": enterprise_url+'/order/orderDetails?orderId=61189831766',
    "method": "get",
    "headers": user_headers_www,
    "data":"orderId=61189831766"
}

# 总包-报价接口
enterprise_offerPrice = {
    "name": "总包系统-报价",
    "url": enterprise_url+'/order/editInnerOrder',
    "method": "post",
    "headers": user_headers,
    "data":{
        "orderId": 61189831766,
        "globalOrderTraceId": 61189831764,
        "offerStatus":True,
        "serveType": 4,
        "orderPayStatus": "unpaid",
        "ownerName": "崔敏萍",
        "offerChoice": False,
        "isAutoAppoint": False,
        "categoryId": 1,
        "serveTypeId": 4,
        "ownerId": 147,
        "orderInitFee": "0",
        "sellerName": "shouqian",
        "contactName": "8",
        "contactPhone": "15915468082",
        "goodsInfo": [{
            "ogId": 382269,
            "thirdOgId": 505889492,
            "noteType": "noUseModule",
            "note": ""
        }],
        "detailedAddress": "广东省深圳市宝安区顺昌路梧桐岛23638",
        "buyerName": "鱼小七518",
        "buyerPhone": "15136721317",
        "provinceId": 440000,
        "cityId": 440300,
        "regionId": 440306,
        "buyerAddress": "顺昌路梧桐岛23638",
        "logisticsInfo": {
            "isArrived": "2",
            "expectArriveTime": "",
            "packageNum": "",
            "trackingId": "",
            "toArrive": False
        },
        "buyerNote": "",
        "userNote": "",
        "type": "update",
        "orderNo": "P61189831765"
        }

}


