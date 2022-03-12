import pymysql

from django.core.signals import request_started
from django.db.models.signals import post_save, post_delete, post_init
from common_util.request_receiver import get_request_ip

pymysql.install_as_MySQLdb()

request_started.connect(get_request_ip)
