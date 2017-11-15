#!/usr/local/bin/python
#-*- coding:utf-8 -*-
from socket import *
from time import ctime

server = socket() #获得socket实例
server.bind(("localhost",9998)) #绑定ip port
server.listen(5)  #开始监听
print("等待客户端的连接...")
while True:
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:
        data = conn.recv(1024)
        print("收到消息:",data)
        if not data:break
        conn.send('[%s] %s' %(ctime(),data))

server.close()

