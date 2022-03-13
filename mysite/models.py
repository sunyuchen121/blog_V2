from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    Label = (
        ('个人日记', '个人日记'),
        ('python', 'python'),
        ('django', 'django'),
    )
    State = (
        ('转载', '转载'),
        ('原创', '原创')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 跟自带表的User关联
    title = models.CharField(max_length=128)
    body = RichTextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    label = models.CharField(max_length=32, choices=Label, default='python')
    know = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=32, choices=State, default='原创')
    read = models.IntegerField(default=0)
    picture_url = models.ImageField(max_length=255, upload_to='article_img', blank=True, null=True)
    extra_property_edit = models.TextField(default="", null=True, blank=True)

    # 图片会自动上传到指定路径下，即 MEDIA_ROOT + upload_to
    class Meta:
        ordering = ['-create']
        verbose_name = "博文管理"
        verbose_name_plural = "博文管理"

    def __str__(self):
        return self.title


class Link(models.Model):
    name = models.CharField(max_length=64)
    about = models.CharField(max_length=128)
    url = models.URLField()
    create = models.DateTimeField(auto_now_add=True)
    img = models.URLField(default="https://www.yanshisan.cn/logo.png")

    class Meta:
        ordering = ['create']
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    extra_property_edit = models.TextField(default="", null=True, blank=True)

    class Meta:
        ordering = ['-create']


class Diary(models.Model):
    body = models.TextField()
    create = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-create']
        verbose_name = '日记'
        verbose_name_plural = '日记'
