#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# IO编程->文件读写
# 练习
# 请将本地一个文本文件读为一个str并打印出来：

# 绝对路径
fpath = r'/Users/pengzk/Desktop/PythonPracticeDemo/practice/test8_IO编程_文件读写.py'
# 相对路径
# fpath = r'./test8_IO编程_文件读写.py'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
