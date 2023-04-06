# coding=utf-8

# 子路由
# from django.template.defaulttags import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('stu', views.index_view),
    path('login', views.login_view),
    path('register', views.register_view),
    path('show', views.show_view),
    path('movie', views.movie_view),
    path('upload', views.upload_view),
    path('showall', views.showall_view),
    path('redict', views.redict_view),
    path('cookie', views.cookie_view),
    path('hello', views.getcookie),

    re_path(r'^$',views.INdexView.as_view()), #调用请求方式
    re_path(r'^get/$', views.GetView),
    re_path(r'^download/$', views.download_view),
    re_path(r'query1/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})',views.query1_views),#关键字定位 P month和year位置不固定
    re_path(r'query2/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})',views.query2_views,{'uname':'zhangsan'}),#传参名称相同
    re_path(r'query/(\d{2})', views.query_views),  #path不支持正则表达式
    re_path(r'query3/', views.query3_views,name='q'),
]






