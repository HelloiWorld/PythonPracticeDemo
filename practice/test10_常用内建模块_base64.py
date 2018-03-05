#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 常用内建模块->base64
# 练习
# 请写一个能处理去掉=的base64解码函数：

import base64

def safe_base64_decode(s):
    while len(s) % 4 != 0:
        # python3中必须要对类型作判断 https://thief.one/2017/04/18/1/
        if isinstance(s, bytes):
            s = s + b'='
        else:
            s = s + '='
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')