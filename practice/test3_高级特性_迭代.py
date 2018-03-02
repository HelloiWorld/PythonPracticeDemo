# -*- coding: utf-8 -*-

# 高级特性->迭代
# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) > 0:
        min = L[0]
        max = L[0]
        for v in L:
            if v < min:
                min = v
            if v > max:
                max = v
        return min, max
    return (None, None)

# 测试
print('findMinAndMax([]) =', findMinAndMax([]))
print('findMinAndMax([7]) =', findMinAndMax([7]))
print('findMinAndMax([7, 1]) =', findMinAndMax([7, 1]))
print('findMinAndMax([7, 1, 3, 9, 5]) =', findMinAndMax([7, 1, 3, 9, 5]))
