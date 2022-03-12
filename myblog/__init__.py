import pymysql

from django.core.signals import request_started
# from django.db.models.signals import post_save, post_delete, post_init
from common_util.request_receiver import get_request_ip
# from common_util.model_receiver import operateInfoRecord

pymysql.install_as_MySQLdb()

# request_start目前来看是相对稳定的，都是只调用一次
request_started.connect(get_request_ip)

# todo post_save信号不稳定,加了dispatch_uid还是会调用多次，操作记录通过复写create,save,delete方法实现
# post_save.connect(operateInfoRecord)
