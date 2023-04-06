#coding=utf-8
from django.urls import re_path,path

from . import views
from django.contrib import admin

urlpatterns = [
    re_path(r'^flogin',views.flogin.as_view()),
    re_path(r'^fregister', views.fregister.as_view())
]