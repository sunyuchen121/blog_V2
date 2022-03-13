"""
自定义插件
"""

from .models import OperateRecord

def model_plugins(mark):
    """操作记录模型插件"""
    def pre():
        pass

    def post():
        pass

    def execute(func):
        return func

    return execute
