"""
自定义信号
"""

class pre_edit_data(object):
    def __init__(self, model, func):
        self.model = model
        self.func_ = func
