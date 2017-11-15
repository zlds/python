#!/usr/local/bin/python
#-*- coding:utf-8 -*-
from  socket import *
client = socket()
client.connect(("localhost",9998))
while True:
    msg = raw_input('>>').strip()
    if len(msg) == 0:continue
    client.send(msg)
    data = client.recv(1024)
    print(data)

client.close()
