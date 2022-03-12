"""
request 信号接收器
"""
import datetime
import logging
from django.core.signals import request_finished, request_started, got_request_exception
from django.dispatch import receiver

@receiver(request_started)
def get_request_ip(sender, **kwargs):
    logger = logging.getLogger("collect")
    request = kwargs.get("environ")
    if request.get('HTTP_X_FORWARDED_FOR'):
        ip = request.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.get("REMOTE_ADDR")
    logger.info(f"{datetime.datetime.now()}\n{ip}\n{request.get('PATH_INFO')}\n{request}")
