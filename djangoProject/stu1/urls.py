# coding=utf-8

# 子路由
# from django.template.defaulttags import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^stu1',views.getTempView.as_view()),
    re_path(r'^stu2', views.getglqView.as_view()),
    re_path(r'^qjsxw',views.getqjsxwView.as_view()),
    re_path(r'^qjsxw1', views.getqjsxw1View.as_view()),
    re_path(r'^mbjc', views.mbjcView.as_view()),
]











