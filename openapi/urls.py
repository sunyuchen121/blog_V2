

from django.urls import path
from openapi import views
urlpatterns = [
    path('get_all_articels/', views.get_all_articels)
]