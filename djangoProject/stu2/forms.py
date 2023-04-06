# coding=utf-8

from django import forms

from stu2.models import *


class LoginForm(forms.Form):
    sname = forms.CharField(max_length=30, label=u'姓名')
    spwd = forms.CharField(label=u'密码')

class Clazz2Form(forms.ModelForm):
    class Meta:
        model = Clazz2
        fields = ('cname',)

class Stu2Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=30,label=u'密码')
    password2 = forms.CharField(widget=forms.PasswordInput,max_length=30,label=u'确认密码')
    class Meta:
        model = Stu2
        fields = ('sname',)
    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            self.errors['password2'] = ['密码不一致']
        return data['password']














