"""
MODEL 信号接收器(模型插件)
"""
import datetime
import json
import logging
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver


# todo post_save信号不稳定,加了dispatch_uid还是会调用多次，操作记录通过复写create,save,delete方法实现
# @receiver(post_save, dispatch_uid="operate_unique_identifier")
# def operateInfoRecord(sender, **kwargs):
#     """操作记录"""
#     from .models import OperateRecord
#     if sender.__dict__.get("__MODEL__"):
#         # logging.info(sender)
#         # logging.info(kwargs)
#         # print(kwargs)
#         inst = kwargs.get('instance').__dict__
#         OperateRecord.objects.create(
#             dataId=inst.get("id"),
#             # info=json.dumps({_k: _v} for _k, _v in inst.items() if not isinstance(_v, object)),
#             modelName=sender.__dict__.get("__MODEL__")
#         )

def create_func(func):
    pass
