# from multiprocessing import Process
#
# def run(name):
#     print('子进程启动成功 %s' % name)
#
# if __name__ == "__main__":
#     print('父进程启动')
#     p = Process(target=run, args=('test',))
#     print('子进程执行')
#     p.start()
#     print(p.name)
#     print(p.pid)
#     print('父进程等待子进程结束')
#     p.join()
#     print('子进程结束')
# #全局变量在多个进程中不共享：进程之间额数据是独立的，默认情况下互不影响
# import multiprocessing,time
# class clock(multiprocessing.Process):
#     def run(self):
#         n = 5
#         while n > 0:
#             print(n)
#             n -= 1
# if __name__ == "__main__":
#     p = clock()
#     p.start()
#     p.join()
#
# #进程池
# from multiprocessing import Pool
# import random,time
# def work(num):
#     print(random.random()*num)
#     time.sleep(3)
# if __name__ == "__main__":
#     po = Pool(3)
#     for i in range(10):
#         po.apply_async(work,(i,)) #非阻塞
#     po.close()
#     po.join() #必须放在close后面
#
# from multiprocessing import Queue
# #Queue实现多进程之间的数据传递
# qu = Queue(3) #空值表示没有上限
# qu.put('haha')
# qu.put('hehe')
# qu.put('xixi')
# print(qu.full())
# print(qu.qsize())
#
# from multiprocessing import Queue,Process
# import time
# def write(q):
#     for value in ['a','b','c']:
#         q.put(value)
#         time.sleep(1)
# def read(q):
#     while True:
#         if not q.empty():
#             print("read   "+q.get())
#             print(q.get)
#             time.sleep(1)
#         else:
#             break
#
# if __name__ == '__main__':
#     qu = Queue()
#     pw = Process(target=write,args=(qu,))
#     pr = Process(target=read,args=(qu,))
#     pw.start()
#     pw.join()
#     pr.start()
#     pr.join()
#     print('success')
#
# #进程池通信
# from multiprocessing import Manager,Pool
# import time
# def write(q):
#     for value in ['a','b','c']:
#         q.put(value)
#         time.sleep(1)
# def read(q):
#     while True:
#         if not q.empty():
#             print("read   "+q.get())
#             print(q.get)
#             time.sleep(1)
#         else:
#             break
# if __name__ == '__main__':
#     print('main start')
#     q = Manager().Queue()
#     po = Pool()
#     po.apply_async(write,(q,))
#     po.apply_async(read,(q,))
#     po.close()
#     po.join()
#     print('success')
#
# import threading
# import time
# def say():
#     print(threading.current_thread().name+"    gggg")
#     time.sleep(5)
#     print('hahahahaha')
#
# if __name__ == "__main__":
#     print(threading.current_thread().name)
#     for i in range(5):
#         th = threading.Thread(target=say)
#         th.start()
#
# import threading,time
# class mythread(threading.Thread):
#     def run(self):
#         for i in range(10):
#             time.sleep(1)
#             print(self.name+"  "+str(i))
# if __name__ == "__main__":
#     t = mythread()
#     t.start()
#
# #线程数据2共享  互斥锁 线程同步
# import threading,time
# num = 0
# def test1():
#     global num
#     if mu.acquire():
#         for i in range(1000000):
#             num += 1
#     mu.release()
#     print("test1 %d" %num)
# def test2():
#     global  num
#     if mu.acquire():
#         for i in range(1000000):
#             num += 1
#     mu.release()
#     print("test2 %d" % num)
# mu = threading.Lock()
# p1 = threading.Thread(target=test1)
# p2 = threading.Thread(target=test2)
# p1.start()
# p2.start()
# # p1.join()
# # p2.join()
# print(num)
#
# #线程同步-队列
# import threading,time
# from queue import Queue
# class Pro(threading.Thread):
#     def run(self):
#         global queue
#         count = 0
#         while True:
#             if queue.qsize()<1000:
#                 for i in range(10):
#                     count = count + 1
#                     msg = '生成产品' + str(count)
#                     queue.put(msg)#队列中添加新产品
#                     print(msg)
#             time.sleep(1)
# class Con(threading.Thread):
#     def run(self):
#         global queue
#         while True:
#             if queue.qsize() > 15:
#                 for i in range(3):
#                     msg = self.name + '消费了' + queue.get()
#                     print(msg)
#             time.sleep(1)
# if __name__ == "__main__":
#     queue = Queue()
#     #创建一个队列。线程中能用，进程中不能使用
#     for i in range(5):#创建500个产品放到队列里
#         queue.put('初始产品' + str(i))#字符串放进队列
#     for i in range(2):#创建了两个线程
#         p = Pro()
#         p.start()
#     for i in range(5):#5个线程
#         c = Con()
#         c.start()
#
# #threadlocal变量
# import threading
# #创建一个全局的对象
# local_school = threading.local()
# def process_student():
#     #获取当前线程关联的student
#     std = local_school.student
#     print("Hello %s (in %s)" %(std,threading.current_thread().name))
# def process_thread(name):
#     #绑定ThreadLocal的Student
#     local_school.student = name
#     process_student()
# t1 = threading.Thread(target=process_thread,args=('haha',),name='t1')
# t2 = threading.Thread(target=process_thread,args=('hehe',),name='t2')
# t1.start()
# t2.start()
#
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # s.bind('',8081)
# addr = ('10.60.2.187',8080)
# data = '你好？'
# s.sendto(data.encode('gbk'),addr)
# data = s.recvfrom(1024)
# print(data[0])
# s.close()
#
# from socket import *
# s = socket(AF_INET,SOCK_DGRAM)
# a = ("",8081)
# s.bind(a)
# num = 0
# while True:
#     recv = s.recvfrom(1024)
#     print(recv[0])
#     print(recv[1])
#     print(recv[0][:4])
#     a = input("请输入")
#     s.sendto(a.encode('gb2312'),recv[1])
#     num += 1
#     print("第%d个数据返回给对方" %num)
# s.close()

# tftp格式
# import struct
# from socket import *
# cb = struct.pack("!H8sb5sb",1,b"jd-gui.cfg",0,b"octet",0)
# uc = socket(AF_INET,SOCK_DGRAM)
# uc.sendto(cb,("10.60.2.187",8080))
# uc.close()
#
# import struct
# from socket import *
# filename = '111.txt'
# server_ip = '10.60.2.187'
# send_data = struct.pack("!H%dsb5sb"%len(filename),1,filename.encode(),0,'octet'.encode(),0)
# s  = socket(AF_INET,SOCK_DGRAM)
# s.sendto(send_data,(server_ip,69))
# f = open(filename,'ab')
# while True:
#     recv = s.recvfrom(1024)
#     czm,ack_num = struct.unpack('!HH',recv[0][:4])
#     print(recv)
#     print(recv[0][:4])
#     print(recv[0][4:])
#     print(recv[1][1])
#     rand_port = recv[1][1]
#
#     if int(czm) == 5:
#         print('文件不存在')
#         break
#     print('操作码：%d,ACk:%d,服务器随机端口：%d,数据长度：%d'%(czm,ack_num,rand_port,len(recv[0])))
#     f.write(recv[0][4:])
#     if len(recv[0]) < 516:
#         break
#     ack_data = struct.pack("!HH",4,ack_num)
#     s.sendto(ack_data,(server_ip,rand_port))
#     print('success')
# s.close()
#
# import socket
# dest = ('<broadcast>',8080)
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
# s.sendto(b'HI',dest)
# print('回复')
# while True:
#     (buf,address) = s.recvfrom(2048)
#     print(buf)
#     print(address,'    ',buf.decode('gbk'))

#tcp
# from socket import *
# tcpsocket = socket(AF_INET,SOCK_STREAM)
# addr = ('10.60.2.187',8080)
# tcpsocket.bind(addr)
# tcpsocket.listen(5) # 设置最大连接数
# newSocket,clientAddr = tcpsocket.accept()
# print(clientAddr,"   哈哈")
# recvdata = newSocket.recv(1024)
# newSocket.send(b"thank you")
# print(recvdata.decode('gbk'))
# newSocket.close()
# tcpsocket.close()
#
# #并发服务器
# from socket import *
# from multiprocessing import *
# from time import sleep
# def dealWithClient(newSocket,destAddr):
#     while True:
#         recvdata = newSocket.recv(1024)
#         if len(recvdata) > 0:
#             print('recv[%s]:%s'%(str(destAddr),recvdata.decode('gbk')))
#         else:
#             print('[%s]客户端已经关闭'%str(destAddr))
#     newSocket.close()
# def main():
#     serSocket = socket(AF_INET,SOCK_STREAM)
#     serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#     localAddr = ('10.60.2.187',8080)
#     serSocket.bind(localAddr)
#     serSocket.listen(5)
#     try:
#         while True:
#             print('---主进程，，等待新客户端的到来---')
#             newSocket, destAddr = serSocket.accept()
#             print('---主进程，，接下来创建一个新的进程负责数据处理')
#             client = Process(target=dealWithClient,args=(newSocket,destAddr))
#             client.start()
#             newSocket.close() #使用thread不用关闭，因为子程序又关闭代码
#     finally:
#         serSocket.close()
# if __name__ == '__main__':
#     main()

# #协程
# import time
# def A():
#     while True:
#         print('---A----')
#         yield
#         time.sleep(0.5)
# def B(c):
#     while True:
#         print('--B---')
#         c.next()
#         time.sleep(0.5)
# if __name__ == '__main__':
#     a = A()
#     B(a)
#
# #协程 greenlet
# from greenlet import greenlet
# import time
# def t1():
#     while True:
#         print("........A........")
#         gr2.switch()
#         time.sleep(1)
# def t2():
#     while True:
#         print("........b........")
#         gr1.switch()#调到上次执行的地方继续执行
#         time.sleep(1)
# gr1 = greenlet(t1)#创建一个greenlet对象
# gr2 = greenlet(t2)
# gr1.switch()#此时会执行1函数
#
# import gevent
# def A():
#     while True:
#         print(".........A.........")
#         gevent.sleep(1)#用来模拟一个耗时操作
#         #gevent中：当一个协程遇到耗时操作会自动交出控制权给其他协程
# def B():
#     while True:
#         print(".........B.........")
#         gevent.sleep(1)#每当遇到耗时操作，会自用转到其他协程
# g1 = gevent.spawn(A) # 创建一个gevent对象（创建了一个协程），此时就已经开始执行A
# g2 = gevent.spawn(B)
# g1.join()  #等待协程执行结束
# g2.join()  #会等待协程运行结束后再退出
























