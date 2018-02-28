#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#错误调试和测试->错误处理
#练习
#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        try:
            return float(s)
        except:
            raise ValueError('not a number')

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
