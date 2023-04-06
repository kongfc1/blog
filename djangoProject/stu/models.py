# -*- coding: utf-8 -*-

from django.db import models
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
# django.setup()

class Img(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='imgs')

class Clazz(models.Model):
    cname = models.CharField(max_length=30)

# Create your models here.
class Student(models.Model):
    xh = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,unique=True)

    score = models.PositiveIntegerField()
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE) #外键 一对多 即一个班级有多名学生

    def __unicode__(self):
        return u'Student:%s,%s'%(self.name,self.score)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        try:
            self.cls = Clazz.objects.get(cname=self.cls.cname)
        except Clazz.DoesNotExist:
            self.cls = Clazz.objects.create(cname=self.cls.cname)
        #学生表的插入
        models.Model.save(self, force_insert=False, force_update=False, using=None, update_fields=None)

# Student.save()

class Scard(models.Model):
    student = models.OneToOneField(Student,primary_key=True,on_delete=models.CASCADE)
    major = models.CharField(max_length=100)


class Post(models.Model):
    pid = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    birth = models.DateTimeField()
    email = models.EmailField()
    isdelete = models.BooleanField(default=False)
    access_count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    file = models.ImageField(upload_to='upload/images')

    def __unicode__(self):
        return u'Post:%s,%s'%(self.title,self.access_count)
























