import json
from catalog.wsf import testScenario
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def offerprice(request):
    response = {}
    param = json.loads(request.body)
    orderNo = param["orderNo"]
    price = param["price"]
    offerNumber = param["offerNumber"]
    auto = param["auto"]
    try:
        testScenario.TestScenario.auto_offerPrice(orderNo,offerNumber,[price,price],auto)
        response['msg'] = "success"
    except Exception as e:
        print(e)
        response ['msg'] = "fail"

    return JsonResponse(response)