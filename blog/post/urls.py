#coding=utf-8
from django.contrib import admin
from django.urls import path, re_path, include

from post import views

urlpatterns = [
    re_path(r'^$',views.queryAll),
    re_path(r'^page/(\d+)$',views.queryAll),
    re_path(r'^post/(\d+)$',views.detail),
    re_path(r'^category/(\d+)$',views.queryPostByCid),
    re_path(r'archive/(\d+)/(\d+)$',views.queryPostByCreated),
]


















