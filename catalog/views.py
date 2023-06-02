import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def offerprice(request):
    response = {}
    data = request.body
    json_data = json.loads(data)["orderNo"]

    response['data'] = json_data
    return JsonResponse(response)