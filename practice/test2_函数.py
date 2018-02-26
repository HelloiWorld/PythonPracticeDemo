# -*- coding: utf-8 -*-

#函数->调用函数
#练习
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print("hex n1: %s" % hex(n1))
print("hex n2: %s" % hex(n2))


#函数->定义函数
#练习
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#的两个解。
#提示：计算平方根可以调用math.sqrt()函数：
import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if b == 0:
        if a * c < 0:
            x1 = math.sqrt(-(a / c))
            x2 = -math.sqrt(-(a / c))
            return x1, x2
        elif c == 0:
            return 0
        else:
            raise ValueError('no answer')
    elif a == 0:
        x = -(c / b)
        return x
    else:
        if b * b - 4 * a * c < 0:
            return ValueError('no answer')
        else:
            x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            return x1, x2

#测试
print('quadratic(1.5, 3, 1) =', quadratic(1.5, 3, 1))
print('quadratic(0, 2, 1) =', quadratic(0, 2, 1))
print('quadratic(1, 2, 2) =', quadratic(1, 2, 2))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))


#函数->函数的参数
#练习
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*numbers):
    product = 1;
    for number in numbers:
        product = product * number
    return product

#测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))


#函数->递归函数
#练习
#汉诺塔的移动可以用递归函数非常简单地实现。
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1,a,c,b) #将A柱的n-1个盘移到B柱
    print(a, '-->', c)
    move(n-1,b,a,c) #将过渡柱子B上n-1个圆盘B移动到目标柱子C

#测试
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
