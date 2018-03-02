# -*- coding: utf-8 -*-

# 函数式编程->返回函数
# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

# 使用生成器迭代
def createCounter():
    def g():
        n = 1
        while True:
            yield n
            n = n + 1
    it = g()
    def counter():
        return next(it)
    return counter

## python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量
## 内层函数能访问外层函数的变量，但不能修改它的指向
def createCounter2():
    count = [0]
    def counter():
        count[0] += 1   # 用list存储，这样地址不变就可以修改其内容了
        return count[0]
    return counter

## nonlocal关键字用来在函数或其他作用域中修改外层(非全局)变量
## global关键字则是用于修改全局变量
def createCounter3():
    count = 0
    def counter():
        nonlocal count  # 允许修改外部变量，在我的理解相当于__block关键字
        count += 1
        return count
    return counter

# 测试
counterA = createCounter()
print('counterA: ', counterA(), counterA(), counterA(), counterA(), counterA())

counterB = createCounter2()
print('counterB: ', counterB(), counterB(), counterB(), counterB(), counterB())

counterC = createCounter3()
print('counterC: ', counterC(), counterC(), counterC(), counterC(), counterC())
