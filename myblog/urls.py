"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite import views
from comment.views import comment
from django.conf import settings
from django.conf.urls.static import static

# 在其他地方注册 会出现程序启动前调用模型的错误 所以在根路由下注册信号
from common_util.model_receiver import *
from common_util.request_receiver import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('read/art_<int:id>/', views.read),
    path('article/', views.article, name="article_list"),
    path('diary/', views.diary),
    path('link/', views.link),
    path('message/', views.message),
    path('index/', views.index),
    path('about/', views.about),
    path('userprofile/', include('userprofile.urls')),
    path('comment/', comment),
    path('api/', include('openapi.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
