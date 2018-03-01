#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 正则表达式
# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

import re

reg_email = r'^([0-9a-zA-Z]+[\.\_]?[0-9a-zA-Z]*)@[0-9a-zA-Z\.\-]+\.[a-zA-Z]{2,4}$'

def is_valid_email(addr):
    m = re.compile(reg_email)
    if m.match(addr) is None:
        return False
    return True

# 测试:
print('is_valid_email(\'1234567890@qq.com\') = %s' % is_valid_email('1234567890@qq.com'))
print('is_valid_email(\'someone@163.com\') = %s' % is_valid_email('someone@163.com'))
print('is_valid_email(\'someone@gmail.com\') = %s' % is_valid_email('someone@gmail.com'))
print('is_valid_email(\'bill.gates@microsoft.com\') = %s' % is_valid_email('bill.gates@microsoft.com'))
print('is_valid_email(\'bob#example.com\') = %s' % is_valid_email('bob#example.com'))
print('is_valid_email(\'mr-bob@example.com\') = %s' % is_valid_email('mr-bob@example.com'))
# assert is_valid_email('1234567890@qq.com')
# assert is_valid_email('someone@163.com')
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')


# 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

reg_name_of_email = r'^<([\w\s]+)>[\s]*([0-9a-zA-Z]+[\.\_]?[0-9a-zA-Z]*)@[0-9a-zA-Z\.\-]+\.[a-zA-Z]{2,4}$'

def name_of_email(addr):
    m = re.match(reg_email, addr)
    if m:
        return m.group(1)
    m = re.match(reg_name_of_email, addr)
    if m:
        return m.group(1)
    return None

# 测试:
print('name_of_email(\'<Tom Paris> tom@voyager.org\') = %s' % name_of_email('<Tom Paris> tom@voyager.org'))
print('name_of_email(\'tom@voyager.org\') = %s' % name_of_email('tom@voyager.org'))
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')