# -*- coding: utf-8 -*-

#函数式编程->匿名函数
#练习
#请用匿名函数改造下面的代码：
#def is_odd(n):
#    return n % 2 == 1
#L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
