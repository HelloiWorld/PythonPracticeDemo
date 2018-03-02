# -*- coding: utf-8 -*-

# 函数式编程->装饰器
# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start_time = time.time()
        fn(*args, **kw)
        end_time = time.time()
        runtime = end_time - start_time
        print('%s executed in %s ms' % (fn.__name__, runtime * 1000))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print('f =', f)
print('s =', s)
