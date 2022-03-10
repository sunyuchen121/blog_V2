import json
import logging

from django.http import HttpResponse, JsonResponse
import django.middleware.csrf
import requests
from django.shortcuts import render
from django.middleware.csrf import get_token
# Create your views here.



# /api/gettoken  这个是地址 url路由的配置就是这个，我下面就不介绍怎么配置路由了，比较简单
def getToken(request):
    token = django.middleware.csrf.get_token(request)
    return JsonResponse({'success': 1, "token": token})


def get_all_articels(request):
    return json.dumps({})


def send_mobile_msg(request):
    """
    借用HCM公有云短信服务进行发送短信
    :param request:
    :return:
    """
    data = json.loads(request.body)
    logging.info(data)
    message, phone = data.get("message"), data.get("phone")
    if not message or not phone:
        return JsonResponse({"success": 0, "msg": "手机号、短信内容均为必填"})
    hcm_common_url = r"https://wzkem.hcmcloud.cn/api/private.sendMobileMessage?private_token=hcmff138d064250e4a07cbdf44f62e77f0a1f092055"
    rep = json.loads(requests.post(hcm_common_url, json={"message": message, "phone": phone, "sender": "Syc"}).content)
    code, msg = 1, "发送成功"
    if rep.get("result").get("success") is not True:
        code, msg = 0, "发送失败，请重试！"
    return JsonResponse({"success": code, "msg": msg})
