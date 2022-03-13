"""
request 信号接收器
"""
import datetime
import logging
from django.core.signals import request_finished, request_started, got_request_exception
from django.dispatch import receiver

@receiver(request_started)
def get_request_ip(sender, **kwargs):
    request = kwargs.get("environ")
    # 访问静态文件、媒体文件、后台的请求都不记录
    for path in ['/static/', 'media', '/admin/']:
        if path in request.get("PATH_INFO"):
            break
    else:
        logger = logging.getLogger("collect")
        if request.get('HTTP_X_FORWARDED_FOR'):
            ip = request.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.get("REMOTE_ADDR")
        logger.info(f"{datetime.datetime.now()}\n{ip}\n{request.get('PATH_INFO')}\n{request}")
