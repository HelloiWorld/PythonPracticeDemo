# -*- coding: utf-8 -*-

#高级特性->列表生成式
#练习
#使用列表生成式将英文字母全部转换为小写，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print('lower([\'Hello\', \'World\', 18, \'Apple\', None]) =' , L2)


#高级特性->生成器
#练习
#杨辉三角定义如下：
#          1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    L = [1]
    while True:
        yield L
        #print('previous yield: L =', L)
        L.append(0)
        #print('after append(0): L =', L)
        #print('[L[i-1] for i in range(len(L))] =', [L[i - 1] for i in range(len(L))])
        #print('[L[i] for i in range(len(L))] =', [L[i] for i in range(len(L))])
        L = [L[i - 1] + L[i] for i in range(len(L))]
        #print('L = L[i-1] + L[i] = ', L)

#不使用列表生成式的写法:
def triangles2():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

#测试
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
print('results =', results)
