from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from .forms import *


class  flogin(View):
    def get(self,request):
        loginForm = LoginForm()
        return render(request,'flogin.html',{'loginForm':loginForm})

    def post(self,request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            data = loginForm.cleaned_data
            user = authenticate(username=data['sname'],password=data['spwd']) #和数据库表中数据进行匹配
            if user:
                login(request,user) #用户数据存放到session
                return HttpResponse('seccuss')
        return HttpResponse('fail')


class fregister(View):
    def get(self,request):
        clsForm = Clazz2Form()
        stuForm = Stu2Form()
        return render(request,'register2.html',{'clsForm':clsForm,'stuForm':stuForm})

    def post(self,request):
        clsForm = Clazz2Form(request.POST)
        stuForm = Stu2Form(request.POST)

        if clsForm.is_valid()*stuForm.is_valid():
            cls = clsForm.save()
            stu = stuForm.save(commit=False)
            stu.Clazz2 = cls
            stu.password = stuForm.clean_password2()
            stu.save()
            return HttpResponse('sucess')
        return render(request,'register2.html',{'clsForm':clsForm,'stuForm':stuForm})






















