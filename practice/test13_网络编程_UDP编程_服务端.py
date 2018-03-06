#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 网络编程->UDP编程
# 例子

import socket

# 创建一个基于IPv4和UDP协议的Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)