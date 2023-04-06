#coding=utf-8

from .models import *

def getData(request):
    return {'uname':'zhangsan'}

def getMeunInfo(request):
    meuns =Menu.objects.all().order_by('mid')
    return {'menu':meuns}