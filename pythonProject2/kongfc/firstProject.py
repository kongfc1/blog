# # coding=utf-8
# # 单行注释
# """   多行注释
# """
# # 变量的定义及使用
# # 命名和java差不多
# count = 2.2183
# print(count)
# print("count = %g"%count)
# count_1 = 1
# print("count=%g\t count1=%g" % (count, count_1))  # \t 制表符  \n 回车
#
# import keyword
# # 关键字
# print(keyword.kwlist)
# # 关键字的个数
# print(len(keyword.kwlist))
#
# # 数据类型 弱语言  int float
# print(type(count))
# print(type(count_1))
#
# print("%d" % count)
# print("%.2f" % count) #四舍五入
#
# count_2 = input("请输入数字\n")
# count_2 = int(count_2)
# print(type(count_2))
# print("%d" % count_2)
#
# #1.4 算术运算符的使用
# print(5/2)
# print(5//2) #取整数
# print(2**8) #2的8次方
# print(8**-1) #8的一次方分之一
# print(5%2) #余数
#
# #1.5 赋值运算符的使用 a += b
# #1.6 实现两个数值的交换 t=a a=b b=t 或者 a,b=b,a
# #1.7 if语句的使用
# import random
# num = random.randint(1,10)
# if num <= 5:
#     print('小')
# else:
#     print('哈哈')
#
# if num > 5:
#     print('大')
#
# #1.8比较与逻辑运算符（用户登录验证）
# result = 1 > 2
# print(result)
# print(type(result))
# print(1 and 5)
# #2.1 if-else的使用
# #2.2 多分支
# if num <=2:
#     print('A')
# elif num > 2 and num <=5:
#     print('B')
# else:
#     print('C')
# #2.3分支嵌套 if if elif 。。。
# while num < 8:
#     print('hello world')
#     print(num)
#     num = random.randint(1, 10)
#
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum) #已跳出while循环
#
# #2.4 while循环使用
# #2.5 循环嵌套多重分支 猜字游戏
# end = True
#
# while end:
#     count_3 = input("猜数字")
#     count_3 = int(count_3)
#     if count_3 == num:
#         print("猜对了")
#         end = False
#     elif count_3 > num:
#         print("猜大了")
#     else:
#         print("猜小了")
# #2.6 嵌套循环的使用
# ii=0
# while ii < 3:
#     print("外循环%d" %ii)
#     j=0
#     while j < 2:
#         print() # 回车
#         print("内循环%d" %j)
#         j += 1
#     ii += 1
#
# #3.2 for循环的使用  99乘法表
# i1 = 1
# while i1 <= 9:
#     j1 = 1
#     while j1 <= i1:
#         print("%d * %d = %d" %(j1,i1,i1*j1),end="\t")
#         j1 += 1
#     print()
#     i1 += 1
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d * %d = %d" % (j, i, i * j), end="\t")
#     print()
#
# for i in range(1, 10).__reversed__():
#     for j in range(1, i+1):
#         print("%d * %d = %d" % (j, i, i * j), end="\t")
#     print()
#
# #3.3 break与continue的使用
# for o in range(10):
#     if o == 1:
#         continue  #跳过当前循环 即后续代码
#     print(o)
#     if o == 3:
#         break  #结束当前循环
#
# #3.5 字符串基本使用
# str = "\n"
# str1 = "qqqwww"
# print(str+"sdsdfsd")
# print(str1[0])
# print(str1[-1])
# print(str1[len(str1)-1])
#
# #3.6 字符串的切片操作
# str_num = ' 0123d345678\n9 '
# print(str_num[1:6])
# print(str_num[::2])
#
# #3.7 字符串常用操作
# print(dir(str_num))
# print(str_num.find('4'))
# print(str_num.index('4'))
# print(str_num.replace('0','d'))
# print(str_num.split("3"))
# print(str_num.splitlines())
# print(str_num.title())
# print(str_num.startswith('0'))
# print(str_num.endswith('9'))
# print(str_num.upper())
# print(str_num.lower())
# print(str_num.ljust(15,'*'))
# print(str_num.rjust(15,'*'))
# print(str_num.center(15,'*'))
# print(str_num.lstrip())
# print(str_num.rstrip())
# print(str_num.strip())
#
# #4.2 字符串方法的使用
# str2 = 'ni hao ma hao ma'
# print(str2.partition('hao'))
# print(str2.isalpha())
# print(str2.isalnum())
# print(str2.isdigit())
# str3 = '_'
# print(str3.join(str2))
#
# #4.3 list的基本使用
# score= [4,2,6,8,1,3]
# print(score[3])
# for score in score:
#     print(score)
#
# #4.4 list的增删查改
# names = [ '孔小宝','孔万三' ]
# names.append('孔太白')
# names.insert(0,'孔仲景')
# print(names)
# name1 = ['张三丰']
# names.extend(name1)
# print(names)
# names.pop(3)
# print(names)
# del names[0]
# print(names)
# print(names.index('孔万三'))
# print(names.count('孔万三'))
# names.clear()
# print(names)
# print('孔万三' in names)
# print('孔万三' not in names)
#
# #4.5嵌套列表的内容及遍历
# list1 = [3,55,23,14,89,45]
# list2 = list1.sort()
# print(list2)
# print(list1)
# list1.sort(reverse=False)
# print(list1)
#
# list3 = [[1,2,3],4,5,[6,7,8,9]]
# print(type(list3))
# for v in list3:
#     if type(v) == list:
#         for i in v:
#             print(i)
#     else:
#         print(v)
#
# #5.1 学生管理系统修改功能
# #5.3 tuple的基本使用 数组
# tuple1 = ('学生1',99)
# print(type(tuple1))
# print(tuple1[0])
# 5.4 dict的定义使用 字典  key唯一
# dict1 = {'china':'shandong','china1':'qufu','china2':'txc'}
# print(type(dict1))
# print(dict1)
# #5.5 dict的增删改查
# china3 = 'china3'
# dict1[china3] = 'kongfc'
# print(dict1)
# dict1.pop('china3')
# print(dict1)
# for key in dict1.keys():
#     print(key)
#     print(dict1[key])
#
# #6.1 学生管理系统（字典版）
# for key,dict1[key] in dict1.items():
#     print(key)
#     print(dict1[key])
#
# #6.2 函数的定义与调用
# def print99(self):
#     for i in range(1, self+1):
#         for j in range(1, i+1):
#             print("%d * %d = %d" % (j, i, i * j), end="\t")
#         print()
#     return self+1
#
# #6.3 函数参数的使用
# print99(9)
# #6.4 函数的返回值问题
# sum1 = print99(5)
# print(sum1)
# 6.5 局部变量与全局变量
# 1，如果全局变量是基本类型（int、float、bool）,修改之前需要使用global
# 2，如果全局变量是引用类型，可以直接修改，不用声明
# 3，优先访问局部变量（同名时）
# c = 100
# def test1():
#     a = 10
#     print("%d" %a)
#     global c
#     c += 100
#     print(c)
# def test2():
#     c = 1000
#     print(c)
#
# test1()
# test2()
# #6.6 可变参数的使用
# def test3(*args):
#     print(type(args))
#     print(args)
#     return 0
#
# print(test3(1,2,3))
# 6.7 可变参数常见问题
# def test4(a,b,*args):
#     print('哈哈，我是天才')
# test4(1,2)
# #引用类型基本讲解
# #7.1 质数的判断
# #7.2水仙花的判断
# def isShuiFl(num):
#     if num < 100 | num > 999:
#         return  False
#     a = num % 10
#     b = num // 10 % 10
#     c = num // 100
#     return a ** 3 + b ** 3 + c ** 3 == num
# print(isShuiFl(88))
# print(isShuiFl(153))
#
# #7.3 可变参数的补充
# def test4(*args,**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# test4(a=1,b=2,c=3,d={1,2,3})
#
# #7.4 递归的使用
# co = 0
# sum = 0
# def digui():
#     global co
#     co += 1
#     global sum
#     sum += co
#     print('haha %g' %sum)
#     if co == 100:
#         return sum
#     digui()
# print(digui())
#
# # 7.5  匿名函数 lambda
#
# def get(a, b):
#     return a + b
#
#
# print(type(get))
# test = lambda :print("engine")
# get1 = lambda a, b: a + b
# print(type(get1))
# print(get1)
#
# # 7.6 文件的写入操作 E:\Desktop\111.txt
# import locale
# print(locale.getpreferredencoding()) # gbk
# print('%c' % 20010)
# file = open('111.txt','w',encoding='utf-8')
# file.write('HelloWorld\n')
# file.write('kongfc\n')
# file.flush()
# file.close()
# #7.7 文件的读取操作
# file1 = open('111.txt','r',encoding='utf-8')
# if file1.readable():
#     # content = file1.read()
#     # print(type(content))
#     # print(content)
#     # content1 = file1.readline()
#     # print(content1)
#     content2 = file1.readlines()
#     print(type(content2))
#     print(content2)
#     file1.close()
# 8.1 文件的复制操作
# import io
#
# rfile = open('111.txt','r',encoding='utf-8')
# wfile = open('123.txt','w',encoding='utf-8')
# con1 = rfile.read()
# con2 = wfile.write(con1)
# rfile.close()
# wfile.close()
# #8.2 封装文件复制函数
# #8.3文件指针偏移处理
# rfile = open('123.txt','rb')
# # print(rfile.tell()) #查看光标位置
# # rfile.read(2)
# # print(rfile.tell())
# # rfile.seek(5,io.SEEK_SET) #偏移5个位置
# # print(rfile.read())
# #如果从文件末尾往前偏移，需要使用'rb'的形式打开文件
# rfile.seek(-8,io.SEEK_END)
# print(rfile.read())
# rfile.close()
# # 8.4 文件夹及文件的常用方法
# import os
# # os.rename('111.txt','aaa.txt')
# os.chdir('E:/Desktop/')
# print(os.getcwd())
# print(os.listdir())
# # os.remove('1234.txt')
# os.mkdir('1234')
# os.path.isfile('1234.txt')
# # 8.5 文件代码行数统计算法
# # 8.6 递归实现某个文件夹中。。。
# # 8.7 批量修改文件名
# # 9.2 面向过程与面向对象
# # 9.3 类与对象
# # 9.4 面向对象分析
# # 9.5 类的封装
# class Driver():
#     def __init__(self,id_):
#         print('我是init方法')
#         self.id = id_
#
#     def driver_car(self):
#         print("1、hahahah %d" % self.id)
#
# driver = Driver(100)
# driver.id = 100
# driver.driver_car()
# # 9.6 对象初始化_int_()的使用
# driver1 = Driver(1001)
# driver1.driver_car()
# #10.2 私有属性的使用
# class Student():
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.setAge(age)
#         # self.__age = age
#         self.gender = gender
#     #对私有属性提供设置值以及获取值的方法
#     def getAge(self):
#         return self.__age
#     def setAge(self,age):
#         if 0 < age < 120:
#             self.__age = age
#         else:
#             print("年龄设置范围不合理，默认为0")
#             self.__age = 0
#     def study(self):
#         print("学习使我快乐，一天不写代码会死")
#     def playGame(self):
#         print("玩把游戏，嗨皮一下")
#     def sleep(self):
#         print("闭上眼睛就睡觉,感觉在打雷")
#     def eat(self):
#         print("吃饭使我快乐")
#     def introduce(self):
#         print("我叫:%s 性别：%s 年龄:%d"%(self.name,self.gender,self.__age))
# #创建对象
# stu1 = Student("胡了",10,'男')
# #获取属性值
# # print(stu1.name)
# # #设置值
# # stu1.name = '宋行'
# # print(stu1.name)
# # stu1.introduce()
# # stu1.age = 1000
# # # stu1.age = -10
# # stu1.introduce()
# #私有属性无法在外部访问
# # print(stu1.__age)
# # stu1.setAge(30)
# # print(stu1.getAge())
# stu1.introduce()
# stu1.sleep()
#
# #10.3 面向对象练习
#heroBoss.py
# 11.1 魔法方法
# 不手动调用，会自动执行的方法
#studentManager.py
#11.2 单继承的使用
# # 11.3 设置属性的快捷方式
# class Student(object):
#     def __init__(self, name, age, gender, id, score, address, tel, height, weight):
#         # self.name = name
#         # pass
#         dic = locals()
#         print(type(dic))
#         print(dic)
#         dic.pop('self')
#         print(dic)
#         for k, v in dic.items():
#             # 设置属性的函数
#             setattr(self, k, v)
#
#     def showInfo(self):
#         print("name:%s age:%d 性别:%s" % (self.name, self.age, self.gender))
#
#
# stu = Student('学生1', 18, '男', '1001', 89, '北京天安门', '15888888888', 130, 130)
#
# stu.showInfo()
#
# #11.4 多继承的使用
# class B():
#     def testA(self):
#         print('testB的A方法')
#     def testB(self):
#         print("B方法")
# class A():
#     def testA(self):
#         print('A方法')
# # class C(A,B):
# #     # pass
# class C(B,A):
#     def testA(self):
#         print('C中A方法')
# class D(C):
#       pass
# c = C()
# c.testA()
# c.testB()
# d = D()
# d.testA()
# print(D.mro()) #打印查找顺序
#
# class A():
#     def __init__(self,a,aa):
#         self.a = a
#         self.aa = aa
# class B():
#     def __init__(self,b):
#         self.b = b
# class C(A,B):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c = c
# # c = C(1,2)
# # print(c.a)
# # print(c.aa)
# # print(c.b)
# c = C(1,2,3)
# # print(c.a)
# print(c.a)
# print(c.aa)
# print(c.c)
#
# print(C.mro())
# print(C.__mro__)
#
# #11.5 方法重写的过程
# #父类中存在某个方法，子类中将该方法重写实现一遍
# #11.6 多态的使用
# # 多态(鸭子类型)：
# #     不是判断对象本身是什么类型，而是根据对象具备某个能力，就认为是什么类型
# class F1(object):
#     def show(self):
#         print("F1.show")
# class S1(F1):
#     def show(self):
#         print("S1.show")
# class S2(S1):
#     def show(self):
#         print("S2.show")
#
# def func(obj):
#     #obj有前提条件， 判断某个对象属于某个类
#     # isinstance(对象，类)
#     # if isinstance(obj,S2) or isinstance(obj,S1) or isinstance(obj,F1):
#     #     obj.show()
#     # else:
#     #     print("%s 不能响应show方法"%obj)
#     # issubclass: 判断某个类是否为另外一个类的子类（包含本身）
#     # obj.__class__ ：获取对象obj所属的类
#     if issubclass(obj.__class__,F1):
#         obj.show()
#     else:
#         print("%s 不能响应show方法" % obj)
# f1 = F1()
# s1 = S1()
# s2 = S2()
#
# func(f1)
# func(s1)
# func(s2)
#
# func('123')
#
# #12.1 对象属性与类属性
# class studen():
#     class_id = 210
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.class_id = 100
# stu1 = studen('haha',12)
# stu2 = studen('hehe',18)
# print("%s所在教室:%d"%(stu1.name,stu1.class_id))
# print("%s所在教室:%d"%(stu1.name,studen.class_id))
# #将教室id更改为211
# studen.class_id = 211
# #这种方式等于是给对象stu1中增加一个成员变量class_id
# stu1.class_id = 212
# print("更改教室后:")
# print("%s所在教室:%d"%(stu1.name,studen.class_id))
# print("%s所在教室:%d"%(stu1.name,stu1.class_id))
#
# #12.2 类方法与静态方法的使用
# class Student():
#     #类变量定义类内，方法外
#     class_id = 210
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     #在成员方法中能否访问类方法
#     def test(self):
#         Student.test1()
#         self.test1()
#         self.__class__.test1()
#         # cls.test1()
#     @classmethod
#     def test1(cls):
#         print("我是类方法")
#         print("class_id:%d"%Student.class_id)
#         print("class_id:%d"%cls.class_id)
#         # print("name:%s"%self.name)
#         # print("age:%s"%self.name)
#         # Student('学生1',19).test()
#     @staticmethod
#     def test2():
#         print("我是静态方法")
# # Student.test1()
# #使用对象访问类方法
# stu1 = Student('学生1',18)
# # stu1.__class__.test1()
# stu1.test()
# # Student.test2()
# # stu1.test2()
#
# #12.3 单例模式对象的唯一性  全局对象唯一
# #  __new__()    作用： 分配内存空间
# class Data():
#     __single = None
#     __firstInit = False
#     def __new__(cls, *args, **kwargs):
#         print('new方法')
#         if cls.__single == None:
#             cls.__single = super().__new__(cls)
#         return cls.__single
#     def __init__(self):
#         if Data.__firstInit == False:
#             print('init方法')
#             self.students = [] #self.data = list()
#             Data.__firstInit = True
# def saveData(stu):
#     data = Data()
#     data.students.append(stu)
# def showData():
#     data = Data()
#     for stu in data.students:
#         print(stu)
# saveData('1')
# saveData('2')
# showData()
# # data1 = Data()
# # data2 = Data()
# # print(id(data1))
# # print(id(data2))
#
# #12.4 单例模式初始化唯一性
# #12.5 异常处理的引入
# a = input('被除数')
# b = input('除数')
# try:
#     a = int(a)
#     b = int(b)
#     c = a/b
#     print("商为：%d"%c)
# except Exception as e:
#     print('有错误')
#     print(type(e))
#     print(e)
#
# #12.6 异常处理的其他方法
# #13.1 try-except-else-finally
# try:
#     file = open('111.txt','r',encoding='utf-8')
#     content  = file.read()
#     print(content)
# except Exception as e:
#     print(e.args)
# else:
#     print('正常')
# finally:
#     file.close()
#     print('谢谢使用')
#
# #13.2 异常传递过程
# def test1():
#     print("-" * 10 + "test1开始" + "-" * 10)
#     try:
#         print(aa)
#     except:
#         pass
#     print("-" * 10 + "test1结束" + "-" * 10)
# def test2():
#     print("-" * 10 + "test2开始" + "-" * 10)
#     test1()
#     print("-" * 10 + "test2结束" + "-" * 10)
# def test3():
#     print("-" * 10 + "test3开始" + "-" * 10)
#     test2()
#     print("-" * 10 + "test3结束" + "-" * 10)
# test3()
#
# #13.3 raise自定义异常
# class GenderError(Exception):
#     def __init__(self):
#         self.errMsg = '性别异常'
# class student():
#     def __init__(self,name,gender):
#         self.name = name
#         # self.__gender = gender
#         self.setGender(gender)
#     def setGender(self,gender):
#         if gender == '1' or gender == '0':
#             self.gender = gender
#         else:
#             raise GenderError()
#     def getGender(self):
#         return self.__gender
# try:
#     stu1 = student('liu','2')
# except Exception as e:
#     print(e.args)
#     print(e.errMsg)
#
# #13.4\5 模块的使用 py后缀结束的文件
# # import heroBoss
# # print(heroBoss.Hero)
#
# from heroBoss import Boss
# print('11111')
# # __all__ = ['变量名', '类名', '函数名']
# # from 模块 import *
# # 只导入__all__列表中包含的

#13.6 包的使用
import package.studenManager
print('111')

#13.7 自定义模块的构建发布安装
# python setup.py build #构建模块
# python setup.py sdist #打包
#解压
#进入解压后的文件夹
# python setup.py install
# 外部库--site-packages能找到安装的自定义模块




























































