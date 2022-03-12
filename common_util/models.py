from django.db import models

# Create your models here.

class OperateRecord(models.Model):
    dataId = models.IntegerField(default=0)
    modelName = models.CharField(max_length=64)
    info = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createTime']
        verbose_name = "操作记录"
        verbose_name_plural = "操作记录"
