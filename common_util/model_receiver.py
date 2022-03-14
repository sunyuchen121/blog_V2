"""
MODEL 信号接收器(模型插件)
"""
from django.db.models.base import ModelState
from django.contrib.auth.backends import ModelBackend
import datetime
import json
import logging
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from mysite.models import Article, Link, Message, Diary
from comment.models import Cccomment, TComment
from django.contrib.auth.models import User

from .models import OperateRecord

# receiver sender不能接收多个 在代码里判断是否需要写日志
operate_model_list = [
    Article, Message, Cccomment,
    TComment, User
]

# 对比修改前后数据时，屏蔽字段列表
unjudge_fields_list = ["create", "update", "extra_property_edit", "last_login", "read"]

@receiver(pre_save, dispatch_uid="update_extra_property")
def preSaveExpland(sender, instance, **kwargs):
    """填充extra_property_edit"""
    if sender in operate_model_list and instance.id is not None:
        extra_property = []
        before_edit = eval(f"{instance.__class__.__name__}.objects.get(id={instance.id})")
        for _k, _v in before_edit.__dict__.items():
            if _k not in unjudge_fields_list and not isinstance(_v, (ModelState, ModelBackend)) and instance.__dict__.get(_k) != _v:
                extra_property.append(_k)
        instance.extra_property_edit = str(extra_property)

@receiver(post_save, dispatch_uid="operate_unique_identifier")
def operateSaveRecord(sender, instance, **kwargs):
    """操作记录"""
    if sender in operate_model_list:
        if kwargs.get("created") is True:
            OperateRecord.objects.create(
                dataId=instance.id,
                info="\n".join([f"{_k}: {_v}" for _k, _v in instance.__dict__.items() if not isinstance(_v, (ModelState, ModelBackend))]),
                modelName=instance.__class__.__name__,
                operate="新增"
            )
        else:
            edit_list = eval(instance.extra_property_edit) if instance.extra_property_edit else []
            # User只保留新增记录
            if edit_list:
                edit_str = "\n".join([f"{_k}: {_v}" for _k, _v in instance.__dict__.items() if _k in edit_list])
                OperateRecord.objects.create(
                    dataId=instance.id,
                    info=edit_str,
                    modelName=instance.__class__.__name__,
                    editList=str(edit_list),
                    operate="修改"
                )

@receiver(post_delete, dispatch_uid="delete_unique_identifier")
def operateDeleteRecord(sender, instance, **kwargs):
    if sender in operate_model_list:
        OperateRecord.objects.create(
            dataId=instance.id,
            info="\n".join([f"{_k}: {_v}" for _k, _v in instance.__dict__.items() if not isinstance(_v, (ModelState, ModelBackend))]),
            modelName=instance.__class__.__name__,
            operate="删除"
        )

def create_func(func):
    pass
