# -*- coding: utf-8 -*-

#高级特性->切片
#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if s == '':
        return s
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s

#利用递归思路的写法
def trim2(s):
    if s == '':
        return s
    if s[0] == ' ':
        return trim2(s[1:])
    if s[-1] == ' ':
        return trim2(s[:-1])
    return s

#测试
print('trim(\'hello  \') =', trim('hello  '))
print('trim(\'  hello\') =', trim('  hello'))
print('trim(\'  hello  \') =', trim('  hello  '))
print('trim(\'  hello  world  \') =', trim('  hello  world  '))
print('trim(\'\') =', trim(''))
print('trim(\'    \') =', trim('    '))
