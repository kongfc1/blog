# #17.2 重复引入问题
# import sys
# value = sys.path
# print(value)
# print(type(value))
# for path in value:
#     print(type(path))
#     print(path)
# sys.path.append('./Tank')
# import tank
# # games = tank.MainGame()
# # games.startGame()
#
# #17.3 ==与is之小整数问题
# # [-5,256] 小整数
# a = 200
# b = 200
# if a==b:
#     print('222')
# elif a is b:  #地址
#     print('111')
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(b))
#
# #17.4 浅复制
# list1 = [1,2,3]
# list2 = list1.copy()
#
# import copy
# list3 = copy.copy(list1)
# print(list3)
# print(list2)
# print(id(list3))
# print(id(list2))
#
# #17.5 shallowcory_deepcopy 深复制
# list4 = copy.deepcopy(list1)
# print(list4)
# print(id(list4))
#
# list5 = [[1,2],[3,4]]
# list6 = copy.copy(list5)
# list7 = copy.deepcopy(list5)
# print(list7)
# print(list6)
# print(id(list6))
# print(id(list7))
# print(list6[0] is list5[0])
# print(list7[0] is list5[0])
#
# #17.6 进制转换问题
# print(bin(10)) #转换成二进制
# print(oct(100)) #八进制
# print(hex(200)) #十六进制
# num = int('0b1010',2)
# print(num)
# num = int('0o127',8)
# print(num)
# num = int('0x2ab',16)
# print(num)
#
# #17.8 源码反码补码
# # 18.1 位运算的操作 二进制
# print(2 << 2) # 8 = 2*2^2
# print(8 >> 2)
# print(5 & 4) # 4
# print(5 | 4)
# print(5 ^ 4)
# password = 123
# my = 2
# password = password ^ my
# print(password)
# print(password ^ my)
# print(~5)
#
# #18.2 属性问题
# class student():
#     def __init__(self,age,name):
#         self.age = age
#         self.__name = name
# stu = student(18,'haha')
# print(dir(stu))
# stu._student__name = 100
# print(stu._student__name) #名字重整
#
# #18.3 property装饰器的基本使用
# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.setAge(age)
#     @property
#     def getAge(self):
#         return self.__age
#     @age.setter
#     def setAge(self,age):
#         if isinstance(age,int):
#             self.__age = age
#         else:
#             raise TypeError('年龄必须是int类型')
#     # age = property(getAge,setAge)
# stu = Student('aaa',10)
# # stu.setAge(20)
# stu.age = 20
# # print(stu.getAge())
# print(stu.age)
#
# #18.4 列表推导式及生成器
# list1 = []
# #循环操作
# for i in range(2,101,2):
#     list1.append(i)
# print(list1)
# #列表推导式 generator
# list2 = [x for x in range(2,101,2)]
# list3 = [x for x in range(101) if x % 2 == 0 if x!=0 if x >= 50]
# g = (x for x in range(101) if x % 2 == 0 if x!=0 if x <= 50)
# print(list2)
# print(list3)
# print(type(g))
# for v in g:
#     print(v)
#
# #18.5 生成器的使用
# def test():
#     for i in range(10):
#         yield i
#         print('-------------')
#         print(i)
# g = test()
# print(type(g))
# print(g.send(None))
# print(next(g))
# print(g.__next__())
# print(g.send(""))
#
# def save_money():
#     while True:
#         print('存入1000')
#         yield None
# def draw_money():
#     while True:
#         print('取出1000')
#         yield None
#
# g_save = save_money()
# g_draw = draw_money()
#
# while True:
#     g_save.__next__()
#     g_draw.__next__()
#
# #18.6 迭代器的使用
# list = [x for x in range(10)]
#
# from collections.abc import Iterable,Iterator
# if isinstance(list,Iterable):
#     for x in list:
#         print(x)
#
# str1 = 'helloworld'
# if isinstance(str1,Iterable):
#     for ch in str1:
#         print(ch,end=" ")
# print('\n')
#
# tuple = tuple(list)
# if isinstance(tuple,Iterable):
#     for tu in tuple:
#         print(tu,end=" ")
# dict = {'one':1,'two':2}
# print('\n')
#
# if isinstance(dict.values(),Iterable):
#     for k in dict.values():
#         print(k)
#
# g = (x for x in range(101) if x % 2 == 0 if x!=0 if x <= 10)
# if isinstance(g,Iterable):
#     print('生成器就是迭代器')
#     for i in g:
#         print(i)
# #能够使用next()函数调用，并不断返回下一个值的对象，称为迭代器
# from collections.abc import Iterable,Iterator
# dict = {'one':1,'two':2}
# all_items = dict.items()
# print(type(all_items))
# if isinstance(all_items,Iterable):
#     for k,v in all_items:
#         print(k,v)
#
# all_items = iter(all_items)
# print(type(all_items))
# if isinstance(all_items,Iterator):
#     print("是迭代器")
# else:
#     print('No')
#
# #18.7 闭包的使用
# def func_out(num1):
#     def func_in(num2):
#         return num1 + num2
#     return func_in
# result = func_out(10)
# print(type(result))
# result1 = result(20)
# print(result1)
# result1 = result(220)
# print(result1)
#
# import math
# def get_dis(x,y,x1,y1):
#     return math.sqrt((x - x1) ** 2 + ((y - y1) ** 2))
# print(get_dis(0,0,10,10))
#
# def get_dis_out(x,y):
#     def get_dis_in(x1,y1):
#         return math.sqrt((x - x1) ** 2 + ((y - y1) ** 2))
#     return get_dis_in
# out = get_dis_out(0,0)
# disin = out(100,100)
# print(disin)
#
# #19.1 写日志文件
# #19.2 使用闭包解决添加功能问题
# #19.3 装饰器的使用
# import time
# def write_log(file_name,func_name):
#     # 记录当前时间，记录访问方法，写入日志文件
#     try:
#         file = open(file_name, 'a', encoding='utf-8')
#         time_str = time.ctime()
#         func_name = func_name
#         content = time_str + '\t' + func_name + '\n'
#         file.write(content)
#     except Exception as e:
#         print(e)
#     finally:
#         file.close()
# #使用闭包完成功能的添加
# #1.函数嵌套定义  2.内部函数访问外部函数作用域中的变量  3.外部函数必须有返回值，返回内部函数
# def func_out(func):
#     def func_in():
#         #新增功能(写入日志文件)
#         write_log('log.txt',func.__name__)
#         #func是传进来的一个函数,调用函数
#         func()
#     return func_in
# @func_out
# #func1 = func_out(func1)
# def func1():
#     print("功能1")
# @func_out
# #func2 = func_out(func2)
# def func2():
#     print("功能2")
# # func1 = func_out(func1,'log.txt')
# # func1()
# # func2 = func_out(func2,'log.txt')
# # func2()
# func1()
# func2()
#
# #19.4 一个函数拥有多个装饰器的问题
#
# def add_out(func):
#     print('装饰器开始')
#     def add_in():
#         return '《' + func() + '》'
#     return add_in
# def add_out1(func):
#     print('装饰器开始1')
#     def add_in1():
#         return '*' + func() + '*'
#     return add_in1
# @add_out #装饰 @add_out1
# @add_out1
# def book_name():
#     print('haha')
#     return 'seven man and one woman is gushi'
# # book_name = add_out(book_name)
# print(book_name())
#
# #19.装饰器-装饰固定参数函数以及不固定参数函数
# def func_out(func):
#     print('aaaa')
#     def func_in(*args):
#         func(*args)
#     return func_in
# @func_out
# def func_1(*args):
#     print('222')
#     print(*args)
#
# func_1(10,20,10,233)
#
# #19.6 装饰器-通用装饰器
# def func_out(func):
#     def func_in(*args,**kwargs):
#         print("日志记录")
#         return func(*args,**kwargs)
#     return func_in
# @func_out
# def func1(a):
#     print(a)
# @func_out
# def func2(a,b):
#     return a + b
# # print(func1(10))
# @func_out
# #b,c为缺省参数
# def func3(a,b=2,c=3):
#     print(a,b,c)
#
# # result = func2(10,20)
# # print(result)
#
# func3(1,5,9)
#
# #19.7python 动态添加属性
# class sudents():
#     def __init__(self,name):
#         self.name = name
# stu = sudents('haha')
# stu.age = 18  #动态添加属性
# sudents.cls_id = 210 #添加类属性
# stu1 = sudents('hehe')
# print(sudents.cls_id)
# print(stu1.cls_id)
#
# #19.8 python 动态添加方法
# def study(self):
#     print('study make me happy')
#
# import types
# stu1.study = types.MethodType(study,stu1)
# stu1.study()
#
# @classmethod
# def testClsMethod(cls):
#     print(cls.cls_id)
#     print('I am class method')
#
# sudents.testClsMethod = testClsMethod
# sudents.testClsMethod()
#
# @staticmethod
# def testStaMethod():
#     print('I am static class method')
#
# sudents.testStaMethod = testStaMethod
# sudents.testStaMethod()
#
# #19.9 type动态创建类
# class person():
#     def __init__(self,name):
#         self.name = name
# print(person)
# print(type(person))
# def study(self):
#     print('study make me happy')
# age = 10
# Students = type('Student',(),{'age':age,'study':study})
# stu = Students()
# print(dir(stu))
# print(stu.age)
# stu.study()
#
# #20.1类装饰器
# def func_out(func):
#     def func_in(*args,**kwargs):
#         print('new add gongengn')
#         return func(*args,**kwargs)
#     return func_in
# @func_out
# def test():
#     print('I am test function ')
# test()
#
# class test1():
#     def __init__(self,func):
#         print('I am Init method')
#         self.func = func
#         self.func()
#     def __call__(self, *args, **kwargs):
#         print('I am call method')
#         pass
# @test1
# def test1():
#     print('I am test function')
# test1()
#
# #20.2 内存管理-引用计数机制
# import gc,sys
# class AAA(object):
#     def __int__(self):
#         print('init')
#         print("object: born at:%s" % hex(id(self)))
#
#     def __new__(cls, *args, **kwargs):
#         print("new")
#         return super(AAA,cls).__new__(cls)
#     def __del__(self):
#         print("bye bye")
# a = AAA()
# print(sys.getrefcount(a))
# list1 = []
# list1.append(a)
# print(sys.getrefcount(a))
# list1.remove(a)
# print(sys.getrefcount(a))
# print("-"*50)
#
# #20.3 内存管理-隔代回收机制
# import gc,sys,time
#
# class AAA(object):
#     def __init__(self):
#         print("object: born at:%s" % hex(id(self)))
#
#     def __new__(cls, *args, **kwargs):
#         print("new")
#         return super(AAA, cls).__new__(cls)
#     def __del__(self):
#         print("bye bye")
# def start():
#     while True:
#         a = AAA()
#         b = AAA()
#         #给a添加成员变量
#         a.v = b
#         #给b添加成员变量
#         b.v = a
#         #无法删除  只是减少引用计数
#         del a
#         del b
#         print(gc.get_count())
#         print(gc.get_threshold())
#         time.sleep(0.5)
# # 手动调用垃圾回收器回收一次
# gc.collect()
# # 设置隔代回收阈值
# gc.set_threshold(100,5,5)
# #手动关闭垃圾回收机制(开发过程禁用)  python3 默认开启
# # gc.disable()
# start()
#
# #20.4 属性拦截控制
# class sutents():
#     """
#        文档注释：111111111111111111
#     """
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __getattribute__(self, item):
#         if item == 'name':
#             return 'kongfc'
#         if item == 'age':
#             return 24
#
# list1 = []
# print(list1.__doc__)
# print('----------------------------')
# stu = sutents('hhh',19)
# print(stu.__doc__)
# print('-'*50)
# stu1 = sutents('jjj',20)
# print(stu1.name)
# print(stu1.age)
#
#
# #20.5 内建函数
# for x in range(10):
#     print(x,end=" ")
# for x in range(10,0,-1):
#     print(x,end=" ")
#
# from collections.abc import Iterator
# list5 = [1,2,3,4,5]
# def func(x):
#     return x * 2
# result = map(func,list5)
# if isinstance(result,Iterator):
#     print('yes')
# print(type(result))
# for x in result:
#     print(x)
#
# #20.6 内建函数 -filter,reduce,sorted
# list6 = [x for x in range(1,10)]
# it = filter(lambda x:x%2==0,list6)
# for i in it:
#     print(i)
#
# from functools import reduce
# list7 = [x for x in range(1,101)]
# re = reduce(lambda x,y:x+y,list7)
# print(re)
#
# list8 = ['1','2','3']
# re1 = reduce(lambda x,y:x+y,list8)
# print(type(re1))
# print(re1)
#
# list9 = [1,4,44,6,2,8,20]
# print(list9.sort())
# re2 = sorted(list9,reverse=True)
# print(re2)
#
# class sutents():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return self.name+"  "+str(self.age)
#
# stud1 = sutents('a111',11)
# stud2 = sutents('b222',22)
# stud3 = sutents('c333',33)
# list10 = [stud1,stud2,stud3]
# # list11 = sorted(list10,key=lambda x:x.name)
# list11 = sorted(list10,key=lambda x:x.age)
# for i in list11:
#     print(i)
#
# #20.7 集合的使用
# var = {1,2,3,2}
# var1 = {3,4,5}
# print(type(var))
# print(var)
# print(var & var1)
# print(var | var1)
# print(var ^ var1)
# print(var - var1)
# var.remove(1)
# # print(var[0])
# print(var)

#20.8 常见内置模块
# builtins 内建函数默认加载
# os       操作系统接口
# sys      python自身运行环境
# functools 常用工具
# json      编解码json对象
# logging   记录日志
# time      时间
# datetime  日期和时间
# calendar  日历
# multiprocessing 进程
# threading       线程
# copy            复制
# hashlib         加密
# re              正则
# socket          标准bsd socket API
from hashlib import *
m = md5()
mob = '13793178913'
pw = 'qw_Q123@'
m.update(pw.encode())
print(m.hexdigest())














