"""
MODEL 信号接收器(模型插件)
"""
import datetime
import logging
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver
from mysite.models import OperateRecord

@receiver(post_save)
def operateInfoRecord(sender, **kwargs):
    """操作记录"""
    logging.info(sender)
    logging.info(kwargs)
