from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.template import Template,RequestContext
import datetime

from stu1.my_context_processors import getData


class getTempView(View):
    def get(self,request):

        return render(request,'gettemp.html',{'user':{'uname':'zhangsan'},'numlist':[1,2,3,4,5],'current':datetime.datetime.today()})


class getglqView(View):
    def get(self,request):
        content = "### 自定义过滤器"
        import datetime
        d = datetime.datetime.today()
        return render(request,'index1.html',{'glq':content,'num':8,'str':'明天ab cd ef','d':d,'list':[1,2,3,4,5],'urlstr':'<h3>北京</h3>'})


class getqjsxwView(View):
    def get(self,request):
        return render(request,"index2.html")


class getqjsxw1View(View):
    def get(self,requet):
        t = Template('{{uname}}')  #底层渲染
        str = t.render(RequestContext(requet,dict_=None,processors=(getData,)))
        return HttpResponse(str)


class mbjcView(View):
    def get(self,request):
        return render(request,'query.html')














