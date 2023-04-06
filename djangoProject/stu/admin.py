# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from stu.models import Student, Post, Img

admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Img)
