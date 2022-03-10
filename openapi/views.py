import json

import requests
from django.shortcuts import render

# Create your views here.

def get_all_articels(request):
    return json.dumps({})

def send_mobile_msg(request):
    """
    借用HCM公有云短信服务进行发送短信
    :param request:
    :return:
    """
    data = request.POST
    message, phone = data.get("meassage"), data.get("phone")
    if not message or not phone:
        return json.dumps({"success": 0, "msg": "手机号、短信内容均为必填"})
    hcm_common_url = r"https://wzkem.hcmcloud.cn/api/private.sendMobileMessage?private_token=hcmff138d064250e4a07cbdf44f62e77f0a1f092055"
    rep = requests.post(hcm_common_url, json={"message": message, "phone": phone, "sender": "Syc"}).json()
    code, msg = 1, "发送成功"
    if rep.get("success") is not True:
        code, msg = 0, "发送失败，请重试！"
    return json.dumps({"success": code, "msg": msg})
