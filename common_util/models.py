from django.db import models

# Create your models here.

class OperateRecord(models.Model):
    OPERATION = (
        ("新增", "新增"),
        ("修改", "修改"),
        ("删除", "删除"),
        ("history", "history")
    )

    dataId = models.IntegerField(default=0)
    modelName = models.CharField(max_length=64)
    info = models.TextField()
    operate = models.CharField(max_length=16, default="history", choices=OPERATION)
    createTime = models.DateTimeField(auto_now_add=True)
    editList = models.CharField(blank=True, null=True, max_length=64)

    class Meta:
        ordering = ['-createTime']
        verbose_name = "操作记录"
        verbose_name_plural = "操作记录"

    def __str__(self):
        str_tmp = "{}: {} {} ".format(self.modelName, self.dataId, self.operate)
        if self.operate == "修改":
            str_tmp += ",".join(eval(self.editList))
        return str_tmp
