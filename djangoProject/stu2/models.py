from django.db import models

# Create your models here.

class Clazz2(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=20,verbose_name=u'班级')

class Stu2(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30,verbose_name=u'姓名')
    password = models.CharField(max_length=30)
    Clazz2 = models.ForeignKey(Clazz2,on_delete=models.CASCADE)










