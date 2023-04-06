import math

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from post.models import Post

@cache_page(60*1) #views层级缓存
def queryAll(request,num=1):  #渲染主页面
    # num = request.GET.get('num',1)
    print(num)
    num = int(num)
    postlist = Post.objects.all().order_by('created')
    #创建分页器对象
    pageObj = Paginator(postlist,1)
    #获取当前页的数据
    perPageList = pageObj.page(num)
    #生成页码数列表
    #每页开始页码
    begin = (num - int(math.ceil(10.0/2)))
    if begin <1:
        begin = 1
    #每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pagelist = range(begin,end+1)
    return render(request,'index.html',{'postlist':perPageList,'pagelist':pagelist,'num':num})


def detail(request,postid):
    postid = int(postid)
    post = Post.objects.get(id=postid)
    return render(request,'detail.html',{'post':post})


def queryPostByCid(request,cid):
    postList = Post.objects.filter(category_id=cid)
    return render(request,'article.html',{'postList':postList})


def queryPostByCreated(request,year,month):
    postList = Post.objects.filter(created__year=year,created__month=month) #USE_TZ = False #时区
    print(postList)

    return render(request,'article.html',{'postList':postList})

























