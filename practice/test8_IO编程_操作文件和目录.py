#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# IO编程->操作文件和目录
# 练习

# 1.利用os模块编写一个能实现dir -l输出的程序。
import os
from datetime import datetime

def output_dir_detail(pwd = os.path.abspath('.')):
    for i in os.listdir(pwd):
        fname = i
        fsize = os.path.getsize(i)
        fmtime = str(datetime.fromtimestamp(os.path.getmtime(i))).split('.')[0]
        flag = '/' if os.path.isdir(i) else ''
        print('%10d   %s   %s%s' % (fsize, fmtime, fname, flag))

output_dir_detail()


# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os

def find_file_with_name(name, dir = '.', result = []):
    for x in os.listdir(dir):
        if os.path.isdir(x):
            find_file_with_name(name, os.path.join('%s' % dir, os.path.relpath(x)))
            continue
        if name in x: #加了条件os.path.isfile(x)就搜不到？？？
            result.append(os.path.join('%s' % dir, os.path.relpath(x)))
    return result

# 测试
for i in find_file_with_name('test8'):
    print(i)
