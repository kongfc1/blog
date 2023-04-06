# Create your views here.
import datetime

from stu.models import Img,Student
import hashlib,inspect
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

md5 = hashlib.md5()

# request.session['uname']='zhangsan'
# request.session.set_expiry(3*24*60*60)
# del request.session['uname']
# request.session.clear();
# request.session.flush()

class User(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd
    def __getstate__(self):
        data = self.__dict__.copy()
        del data['pwd']
        return data


def redict_view(request):
    # return HttpResponseRedirect('/student/showall') #重定向 302 不永久
    # return redirect('/student/showall/',permanent=True) #重定向 301 永久
    response = HttpResponse()
    response.status_code = 302
    response.setdefault('Location','/student/showall')
    return response

def upload_view(request):
    uname = request.POST.get('uname', '')
    photo = request.FILES.get('photo', '')
    Img.objects.create(sname=uname,photo=photo)
    return HttpResponse('上传成功')

def showall_view(request):
    stus = Img.objects.all()
    return render(request,'show1.html',{'stus':stus})

def download_view(request):
    photo = request.GET.get('photo','')
    filename = photo[photo.rindex('/')+1:]
    print(photo+'   '+filename+"  "+str(photo.rindex('/')))

    import os
    path = os.path.join(os.getcwd(), 'media', photo.replace('/','\\'))
    print(path)
    with open(path,'rb') as fr:
        response = HttpResponse(fr.read())
        response['Content-Type']='image/png'
        #预览模式
        response['Content-Disposition']='attachment;filename='+filename #浏览器下载效果不一样，解释器导致的

    return response

def index_view(request):
    if request.method=='GET':
        # return render(request, 'index.html')
        return render(request,'login.html');
    elif request.method == 'POST':
        name = request.POST.get('uname','')
        photo = request.FILES.get('photo','')
        print(photo.name)
        # fra = inspect.stack()
        # ca = fra[0] #当前views.py 路径
        # cfp = ca.filename
        # print(f"cfp: {cfp}")

        import os
        if not os.path.exists('media'):
            os.mkdir('media')
            print('创建成功')
        print(os.getcwd())
        # file1 = os.path.join(os.getcwd(),'media',photo.name)
        # print(file1)
        # file1= file1.replace('\\','/')
        # print(file1)
        # file = open(file1,'wb')
        # file.write(photo.read())
        with open(os.path.join(os.getcwd(),'meida',photo.name),'wb') as fw: #No such file or directory
            re = photo.read()
            fw.write(re)
        # with open(os.path.join(os.getcwd(),'media',photo.name),'wb') as fw:
        #     for ck in photo.chuncks():#似乎不支持
        #         fw.write(ck)

        return HttpResponse('上传成功')
    else:
        return HttpResponse('bugeixianshi')


def login_view(request):
    uname = request.POST.get('uname','')
    pwd = request.POST.get('pwd','')
    if uname and pwd:
        count = Student.objects.filter(sname=uname,pwd=pwd).count()
        if count ==1:
            return HttpResponse('登录成功')
    return HttpResponse('登录失败')


def register_view(request):
    m = request.method; #获取当前请求方式 post get
    if 'GET' == m:
        return render(request,'register.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        md5.update(pwd.encode('utf-8'))
        pwd = md5.hexdigest()
        if pwd and uname:
            stu = Student(sname=uname,pwd=pwd)
            stu.save()
        return HttpResponse('注册成功')
    return HttpResponse('注册失败')

# CREATE TABLE "stu_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
# "sname" varchar(30) NOT NULL UNIQUE, "pwd" varchar(30) NOT NULL);
# COMMIT;

def show_view(request):
    print('11111')
    stus = Student.objects.all()
    return render(request,'show.html',{'students':stus})


def movie_view(request):
    return None


def query_views(request,num):
    return HttpResponse('hello_%s'%num)


def query1_views(request,month,year):
    return HttpResponse('hello_%s_%s'%(year,month))


def query2_views(request,month,year,uname):
    return HttpResponse('hello_%s_%s_%s'%(year,month,uname))


def query3_views(request):
    return HttpResponse('hello')


def cookie_view(request):
    res = HttpResponse() #创建响应对象
    # 数据存储在cookie中 保存一天 然后添加 expires
    # res.set_cookie('uname','zhangsan',max_age=24*60*60,#expires=datetime.datetime.today(),
    #  path='/student/hello')
    res.set_signed_cookie('uname','zhangsan',salt='haha') #加盐
    return res


def getcookie(request):
    # str = request.COOKIES.get('uname')
    # # uname = request.get_signed_cookie('uname',salt='haha')
    # return HttpResponse(str)
    if 'uname' in request.COOKIES:
        uname = request.get_signed_cookie('uname',salt='haha')
        return HttpResponse(uname)
    else:
        return HttpResponse('当前Cookie不存在')

from django.views import View

class INdexView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('get请求')

    def post(self,request,*args,**kwargs):
        return HttpResponse('Post请求')


def GetView(request):
    uname = request.GET.get('uname')
    pwd = request.GET.get('pwd')
    print(uname+'   '+pwd)
    return JsonResponse({'flag':True})