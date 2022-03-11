import datetime
import logging

def get_request_ip(request):
    logger = logging.getLogger("collect")
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    logger.info(f"{datetime.datetime.now()}\n{ip}\n{request.__dict__}")

