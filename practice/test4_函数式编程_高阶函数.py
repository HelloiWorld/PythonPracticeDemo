# -*- coding: utf-8 -*-

# 函数式编程->高阶函数->map/reduce
# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name.title()

# 测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn, L)
#    return reduce(lambda x, y: x * y, L)

# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    dot = s.find('.')
    def fn(x, y):
        return x * 10 + y
    def fd(x):
        return x / 10**(len(s)-dot-1)
    if dot == -1:
        return reduce(fn, map(int, s))
    return reduce(fn, map(int, s[:dot])) + fd(reduce(fn, map(int, s[dot+1:])))

# 测试
print('str2float(\'123.456\') =', str2float('123.456'))


# 函数式编程->高阶函数->filter
# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    int2str = str(n)
    str2int = int(int2str[::-1])
    return n == str2int

# 测试
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))


# 函数式编程->高阶函数->sorted
# 练习
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
# 再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[:][0]
def by_score(t):
    return t[:][-1]

# 测试
L2 = sorted(L, key=by_name)
print('按名字排序:', L2)
L3 = sorted(L, key=by_score, reverse=True)
print('按成绩从高到低排序:', L3)
