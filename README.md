> 本demo练习题目来源[廖雪峰老师的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

# 目录
* [Python基础](#Python基础)
  - [字符串和编码](#字符串和编码)
  - [条件判断](#条件判断)
  - [循环](#循环)
* [函数](#函数)
  - [调用函数](#调用函数)
  - [定义函数](#定义函数)
  - [函数的参数](#函数的参数)
  - [递归函数](#递归函数)
* [高级特性](#高级特性)
  - [切片](#切片)
  - [迭代](#迭代)
  - [列表生成式](#列表生成式)
  - [生成器](#生成器)
* [函数式编程](#函数式编程)
  - [高阶函数](#高阶函数)
    - [map/reduce](#mapreduce)
    - [filter](#filter)
    - [sorted](#sorted)
  - [返回函数](#返回函数)
  - [匿名函数](#匿名函数)
  - [装饰器](#装饰器)
* [面向对象编程](#面向对象编程)
  - [访问限制](#访问限制)
  - [实例属性和类属性](#实例属性和类属性)
* [面向对象高级编程](#面向对象高级编程)
  - [使用@property](#使用property)
  - [使用枚举类](#使用枚举类)
* [错误调试和测试](#错误调试和测试)
  - [错误处理](#错误处理)
  - [单元测试](#单元测试)
  - [文档测试](#文档测试)
* [IO编程](#IO编程)
  - [文件读写](#文件读写)
  - [操作文件和目录](#操作文件和目录)
  - [序列化](#序列化)
* [正则表达式](#正则表达式)
* [常用内建模块](#常用内建模块)
  - [datetime](#datetime)
  - [base64](#base64)
  - [struct](#struct)
  - [hashlib](#hashlib)
  - [hmac](#hmac)
  - [itertools](#itertools)
  - [urllib](#urllib)
  - [XML](#xml)
  - [HTMLParser](#htmlparser)
* [常用第三方模块](#常用第三方模块)
* [图形界面](#图形界面)
* [网络编程](#网络编程)
  - [TCP编程](#tcp编程)
  - [UDP编程](#udp编程)
* [电子邮件](#电子邮件)
  - [SMTP发送邮件](#smtp发送邮件)
  - [POP3收取邮件](#pop3收取邮件)
* [访问数据库](#访问数据库)
  - [使用SQLite](#使用sqlite)
  - [使用MySQL](#使用mysql)
  - [使用SQLAlchemy](#使用sqlalchemy)
* [Web开发](#web开发)
  - [使用Web框架](#使用web框架)
  - [使用模板](#使用模板)
* [异步IO](#异步io)
  - [async/await](#asyncawait)
  - [aiohttp](#aiohttp)
* [实战](#实战)
  - [webapp](#webapp)
   

<h2 id="Python基础">Python基础</h2>

#### 字符串和编码
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

    s1 = 72
    s2 = 85
    r = 100 * (s2 - s1) / s1
    print('%.1f%%' % r)

#### 条件判断
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
    
    height = 1.75
    weight = 80.5
    bmi = weight / (height * height)
    print("bmi %f" % bmi)
    if bmi < 18.5:
       print("过轻")
    elif bmi < 25:
        print("正常")
    elif bmi < 28:
        print("过重")
    elif bmi < 32:
       print("肥胖")
    else:
      print("严重肥胖")
    
-->
    
    bmi 26.285714
    过重
      
#### 循环
请利用循环依次对list中的每个名字打印出Hello, xxx!：
    
    L = ['Bart', 'Lisa', 'Adam']
    for name in L:
        print("Hello, %s!" % name)
    
-->

    Hello, Bart!
    Hello, Lisa!
    Hello, Adam!
 
## 函数
#### 调用函数
请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

    n1 = 255
    n2 = 1000
    print("hex n1: %s" % hex(n1))
    print("hex n2: %s" % hex(n2))
    
-->

    hex n1: 0xff
    hex n2: 0x3e8

#### 定义函数
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0
的两个解。<br>
提示：计算平方根可以调用`math.sqrt()`函数：    
    
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
    
    # 测试   
    print('quadratic(1.5, 3, 1) =', quadratic(1.5, 3, 1))
    print('quadratic(0, 2, 1) =', quadratic(0, 2, 1))
    print('quadratic(1, 2, 2) =', quadratic(1, 2, 2))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

-->
    
    quadratic(1.5, 3, 1) = (-0.42264973081037427, -1.5773502691896255)
    quadratic(0, 2, 1) = -0.5
    quadratic(1, 2, 2) = no answer
    quadratic(1, 3, -4) = (1.0, -4.0)
    
#### 函数的参数
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

    def product(*numbers):
    product = 1;
    for number in numbers:
        product = product * number
    return product
    
    # 测试
    print('product(5) =', product(5))
    print('product(5, 6) =', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
    print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

-->
    
    product(5) = 5
    product(5, 6) = 30
    product(5, 6, 7) = 210
    product(5, 6, 7, 9) = 1890

#### 递归函数
汉诺塔的移动可以用递归函数非常简单地实现。 
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

    def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1,a,c,b) #将A柱的n-1个盘移到B柱
    print(a, '-->', c)
    move(n-1,b,a,c) #将过渡柱子B上n-1个圆盘B移动到目标柱子C
    
    # 测试
    # 期待输出:
    # A --> C
    # A --> B
    # C --> B
    # A --> C
    # B --> A
    # B --> C
    # A --> C
    move(3, 'A', 'B', 'C')
    
-->

    A --> C
    A --> B
    C --> B
    A --> C
    B --> A
    B --> C
    A --> C
    
## 高级特性
#### 切片
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
    
    def trim(s):
        if s == '':
            return s
        while s != '' and s[0] == ' ':
            s = s[1:]
        while s != '' and s[-1] == ' ':
            s = s[:-1]
        return s
    
    # 利用递归思路的写法
    def trim2(s):
        if s == '':
            return s
        if s[0] == ' ':
            return trim2(s[1:])
        if s[-1] == ' ':
            return trim2(s[:-1])
        return s
    
    # 测试
    print('trim(\'hello  \') =', trim('hello  '))
    print('trim(\'  hello\') =', trim('  hello'))
    print('trim(\'  hello  \') =', trim('  hello  '))
    print('trim(\'  hello  world  \') =', trim('  hello  world  '))
    print('trim(\'\') =', trim(''))
    print('trim(\'    \') =', trim('    '))

-->

    trim('hello  ') = hello
    trim('  hello') = hello
    trim('  hello  ') = hello
    trim('  hello  world  ') = hello  world
    trim('') =
    trim('    ') =
    
#### 迭代
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
    
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

-->
    
    findMinAndMax([]) = (None, None)
    findMinAndMax([7]) = (7, 7)
    findMinAndMax([7, 1]) = (1, 7)
    findMinAndMax([7, 1, 3, 9, 5]) = (1, 9)

#### 列表生成式
使用列表生成式将英文字母全部转换为小写，通过添加if语句保证列表生成式能正确地执行：

    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print('lower([\'Hello\', \'World\', 18, \'Apple\', None]) =' , L2)
    
-->
    
    lower(['Hello', 'World', 18, 'Apple', None]) = ['hello', 'world', 'apple']

#### 生成器
> 包含`yield`关键字的函数表明是一个generator，在调用`next()`时遇到`yield`会中断，在下次运行时再从上次返回的`yield`处继续执行

杨辉三角定义如下：

              1
             / \
            1   1
           / \ / \
          1   2   1
         / \ / \ / \
        1   3   3   1
       / \ / \ / \ / \
      1   4   6   4   1
     / \ / \ / \ / \ / \
    1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
    
    def triangles():
        L = [1]
        while True:
            yield L
            #print('previous yield: L =', L)
            L = L + [0,] # L.append(0)这样写会导致输出每一项都多一个0
            #print('after append(0): L =', L)
            #print('[L[i-1] for i in range(len(L))] =', [L[i - 1] for i in range(len(L))])
            #print('[L[i] for i in range(len(L))] =', [L[i] for i in range(len(L))])
            L = [L[i - 1] + L[i] for i in range(len(L))]]
            #print('after triangles: L =', L)
        
    # 不使用列表生成式的写法:
    def triangles2():
        ret = [1]
        while True:
            yield ret
            for i in range(1, len(ret)):
                ret[i] = pre[i] + pre[i - 1]
            ret.append(1)
            pre = ret[:]

    # 测试
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
    
  -->
  
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    results = [[1, 0], [1, 1, 0], [1, 2, 1, 0], [1, 3, 3, 1, 0], [1, 4, 6, 4, 1, 0], [1, 5, 10, 10, 5, 1, 0], [1, 6, 15, 20, 15, 6, 1,  0], [1, 7, 21, 35, 35, 21, 7, 1, 0], [1, 8, 28, 56, 70, 56, 28, 8, 1, 0], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]

## 函数式编程
### 高阶函数
#### map/reduce
> map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。<br>
  reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
  `reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
> `lower()`、`upper()`、`capitalize()`、`title()`、`swapcase()`这几个方法分别用来将字符串转换为小写、大写字符串、将字符串首字母变为大写、将每个首字母变为大写以及大小写互换，这几个方法都是生成新字符串，并不对原字符串做任何修改<br/>
  `replace()`用来替换字符串中指定字符或子字符串的所有重复出现，每次只能替换一个字符或字符串。该方法并不修改原字符串，而是返回一个新字符串。
    
    def normalize(name):
        return name.title()

    # 测试
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
    
-->  

    ['Adam', 'Lisa', 'Bart']
    
    
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

    from functools import reduce
    def prod(L):
        def fn(x, y):
            return x * y
        return reduce(fn, L)
    #    return reduce(lambda x, y: x * y, L)
    
    # 测试
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9])) 
    
-->

    3 * 5 * 7 * 9 = 945
    
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

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
    
-->

    str2float('123.456') = 123.456

#### filter
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
    
    def is_palindrome(n):
        int2str = str(n)
        str2int = int(int2str[::-1])
        return n == str2int
    
    # 测试
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))

-->
    
    1~1000: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]
    
#### sorted
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：<br>
再按成绩从高到低排序：

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

-->
    
    按名字排序: [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
    按成绩从高到低排序: [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]

#### 返回函数
利用闭包返回一个计数器函数，每次调用它返回递增整数：
    
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
    
-->
    
    counterA:  1 2 3 4 5
    counterB:  1 2 3 4 5
    counterC:  1 2 3 4 5

#### 匿名函数
请用匿名函数改造下面的代码：

    def is_odd(n):
        return n % 2 == 1
    L = list(filter(is_odd, range(1, 20)))

改造后：

    L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
    print(L)

-->

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
#### 装饰器
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

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
    
-->

    fast executed in 1.5931129455566406 ms
    slow executed in 123.92115592956543 ms
    f = 33
    s = 7986

## 面向对象编程
#### 访问限制
请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.gender = gender
    
修改后：
    
    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.__gender = gender

        def get_gender(self):
            return self.__gender

        def set_gender(self, gender):
            if gender == 'male' or gender == 'female':
            # if gender in ('male','female'):
                self.__gender = gender
            else:
                raise ValueError('bad gender')

    # 测试
    bart = Student('Bart', 'male')
    print('bart.get_gender() =', bart.get_gender())
    bart.set_gender('female')
    print('after bart.set_gender(\'female\'), bart.get_gender() =', bart.get_gender())
    
-->

    bart.get_gender() = male
    after bart.set_gender('female'), bart.get_gender() = female

#### 实例属性和类属性
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

    class Student(object):
        count = 0 # 这里是类变量，是静态变量(只初始化一次，然后存在内存中便于修改访问)，类似于oc中的static关键字
        def __init__(self, name):
            self.name = name
            Student.count += 1 # 修改时必须修改类属性
    
    # 测试
    print('Student.count =', Student.count)
    bart = Student('Bart')
    print('Student.count =', Student.count)
    lisa = Student('Bart')
    print('Student.count =', Student.count)
    
-->

    Student.count = 0
    Student.count = 1
    Student.count = 2        

## 面向对象高级编程
#### 使用@property
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

    class Screen(object):
        @property
        def width(self):
            return self._width

        @width.setter
        def width(self, value):
            self._width = value

        @property
        def height(self):
            return self._height
    
        @height.setter
        def height(self, value):
            self._height = value

        @property
        def resolution(self):
            return self._width * self._height
    
    # 测试
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)

-->
    
    resolution = 786432

#### 使用枚举类
把Student的gender属性改造为枚举类型，可以避免使用字符串：

    from enum import Enum, unique
    
    class Gender(Enum):
        Male = 0
        Female = 1

    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.gender = gender

改造后，只允许通过枚举类设置gender

    @unique
    class Gender(Enum):
        Male = 'male'   #并不一定非要用数字
        Female = 'female'

    class Student(object):
        def __init__(self, name, gender):
            self.name = name
            self.gender = gender

        @property
        def gender(self):
            return self._gender

        @gender.setter
        def gender(self, value):
            if isinstance(value, Gender):
                self._gender = value
            else:
                raise TypeError('bad type gender')
    
    # 测试
    bart = Student('Bart', Gender.Male)
    print('bart.gender =', bart.gender)
    print('bart.gender.value =', bart.gender.value)
    
    bart2 = Student('Bart2', 'Gender.Male')
    
-->
    
    bart.gender = Gender.Male
    bart.gender.value = male
    
    Traceback (most recent call last):
    ...
    TypeError: bad type gender

## 错误调试和测试
#### 错误处理
运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
    
    from functools import reduce

    def str2num(s):
        return int(s)

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
 
 错误：
 
      File "test7_错误调试和测试_错误处理.py", line 10, in str2num
        return int(s)
    ValueError: invalid literal for int() with base 10: ' 7.6'
    
 说明是将7.6转成int类型出错，修改`str2num():`方法即可
 
    def str2num(s):
        try:
            return int(s)
        except ValueError as e:
            try:
                return float(s)
            except:
                raise ValueError('not a number')
 
#### 单元测试
对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：

    import unittest

    #class Student(object):
    #    def __init__(self, name, score):
    #        self.name = name
    #        self.score = score
    #    def get_grade(self):
    #        if self.score >= 60:
    #            return 'B'
    #        if self.score >= 80:
    #            return 'A'
    #        return 'C'

    # 修改后
    class Student(object):
        def __init__(self, name, score):
            self.name = name
            self.score = score
        def get_grade(self):
            if self.score < 0 or self.score > 100:
                raise ValueError('bad value of score')

            if self.score >= 80:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'

    # 测试
    class TestStudent(unittest.TestCase):
        def test_80_to_100(self):
            s1 = Student('Bart', 80)
            s2 = Student('Lisa', 100)
            self.assertEqual(s1.get_grade(), 'A')
            self.assertEqual(s2.get_grade(), 'A')
    
        def test_60_to_80(self):
            s1 = Student('Bart', 60)
            s2 = Student('Lisa', 79)
            self.assertEqual(s1.get_grade(), 'B')
            self.assertEqual(s2.get_grade(), 'B')
    
        def test_0_to_60(self):
            s1 = Student('Bart', 0)
            s2 = Student('Lisa', 59)
            self.assertEqual(s1.get_grade(), 'C')
            self.assertEqual(s2.get_grade(), 'C')
    
        def test_invalid(self):
            s1 = Student('Bart', -1)
            s2 = Student('Lisa', 101)
            with self.assertRaises(ValueError):
                s1.get_grade()
            with self.assertRaises(ValueError):
                s2.get_grade()

    if __name__ == '__main__':
        unittest.main()
        
-->

    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.000s

    OK

#### 文档测试
对函数fact(n)编写doctest并执行：

    def fact(n):
        '''
        Calculate 1*2*...*n
        
        >>> fact(1)
        1
        >>> fact(10)
        3628800
        >>> fact(-1)
        Traceback (most recent call last):
            ...
        ValueError
        '''
        if n < 1:
            raise ValueError()
        if n == 1:
            return 1
        return n * fact(n - 1)
    
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

测试：将
    
    if n < 1:   
        raise ValueError()

注释，打印结果如下：

    **********************************************************************
    File "test7_错误调试和测试_文档测试.py", line 15, in __main__.fact
    Failed example:
        fact(-1)
    Expected:
        Traceback (most recent call last):
            ...
        ValueError
    Got:
        Traceback (most recent call last):
        File "/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/doctest.py", line 1330, in __run
            compileflags, 1), test.globs)
        File "<doctest __main__.fact[2]>", line 1, in <module>
            fact(-1)
        File "test7_错误调试和测试_文档测试.py", line 24, in fact
            return n * fact(n - 1)
        File "test7_错误调试和测试_文档测试.py", line 24, in fact
            return n * fact(n - 1)
        File "test7_错误调试和测试_文档测试.py", line 24, in fact
            return n * fact(n - 1)
        [Previous line repeated 990 more times]
        File "test7_错误调试和测试_文档测试.py", line 22, in fact
            if n == 1:
        RecursionError: maximum recursion depth exceeded in comparison
    **********************************************************************
    1 items had failures:
        1 of   3 in __main__.fact
    ***Test Failed*** 1 failures.

<h2 id="IO编程">IO编程</h2>

#### 文件读写
请将本地一个文本文件读为一个str并打印出来：

    # 绝对路径
    fpath = r'/Users/pengzk/Desktop/PythonPracticeDemo/practice/test8_IO编程_文件读写.py'
    # 相对路径
    # fpath = r'./test8_IO编程_文件读写.py'
    
    with open(fpath, 'r') as f:
    s = f.read()
    print(s)
    
-->

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    # IO编程->文件读写
    # 练习
    # 请将本地一个文本文件读为一个str并打印出来：

    # 绝对路径
    fpath = r'/Users/pengzk/Desktop/PythonPracticeDemo/practice/test8_IO编程_文件读写.py'
    # 相对路径
    # fpath = r'./test8_IO编程_文件读写.py'

    with open(fpath, 'r') as f:
        s = f.read()
        print(s)

#### 操作文件和目录
1.利用os模块编写一个能实现dir -l输出的程序。

    import os
    from datetime import datetime

    def output_dir_detail(pwd = os.path.abspath('.')):
        for i in os.listdir(pwd):
            fname = i
            fsize = os.path.getsize(i)
            fmtime = str(datetime.fromtimestamp(os.path.getmtime(i))).split('.')[0]
            flag = '/' if os.path.isdir(i) else ''
            print('%10d   %s   %s%s' % (fsize, fmtime, fname, flag))

    # 测试
    output_dir_detail()
    
-->

    6148   2018-02-28 18:41:58   .DS_Store
    1048   2018-02-25 18:53:05   test1_基础.py
    2477   2018-02-25 18:52:57   test2_函数.py
     820   2018-02-26 10:52:36   test3_高级特性_切片.py
    1740   2018-02-26 10:51:34   test3_高级特性_生成器.py
     615   2018-02-26 10:53:04   test3_高级特性_迭代.py
     249   2018-02-27 10:01:41   test4_函数式编程_匿名函数.py
     720   2018-02-27 10:01:33   test4_函数式编程_装饰器.py
    1427   2018-02-26 10:52:27   test4_函数式编程_返回函数.py
    2106   2018-02-27 16:29:25   test4_函数式编程_高阶函数.py
     657   2018-02-27 10:02:01   test5_面向对象编程_实例属性和类属性.py
     908   2018-02-26 18:28:30   test5_面向对象编程_访问限制.py
     683   2018-02-27 12:10:18   test6_面向对象高级编程_使用@property.py
    1015   2018-02-27 15:20:26   test6_面向对象高级编程_使用枚举类.py
    1790   2018-02-28 11:17:43   test7_错误调试和测试_单元测试.py
     503   2018-02-28 11:07:53   test7_错误调试和测试_文档测试.py
     656   2018-02-28 11:02:13   test7_错误调试和测试_错误处理.py
     914   2018-03-02 10:10:55   test8_IO编程_序列化.py
    1160   2018-02-28 18:49:26   test8_IO编程_操作文件和目录.py
     376   2018-02-28 18:50:24   test8_IO编程_文件读写.py
     
2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

    import os

    def find_file_with_name(name, dir = '.', result = []):
        for x in os.listdir(dir):
            if os.path.isdir(x):
                find_file_with_name(name, os.path.join('%s' % dir, os.path.relpath(x)))
                continue
            if name in x: #加了条件os.path.isfile(x)就搜不到？？？
                result.append(os.path.join('%s' % dir, os.path.relpath(x)))
        return result
        
    # 测试
    for i in find_file_with_name('test8'):
        print(i)
    
-->
    
    ./test8_IO编程_序列化.py
    ./test8_IO编程_操作文件和目录.py
    ./test8_IO编程_文件读写.py

#### 序列化
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

    import json

    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=True)  #默认，中文会转成Unicode编码
    s2 = json.dumps(obj, ensure_ascii=False)

    # 测试
    print('s = %s' % s)
    print('s2 = %s' % s2)
    
-->

    s = {"name": "\u5c0f\u660e", "age": 20}
    s2 = {"name": "小明", "age": 20}

## 正则表达式
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：<br>
`someone@gmail.com`<br>
`bill.gates@microsoft.com`
    
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

-->

    is_valid_email('1234567890@qq.com') = True
    is_valid_email('someone@163.com') = True
    is_valid_email('someone@gmail.com') = True
    is_valid_email('bill.gates@microsoft.com') = True
    is_valid_email('bob#example.com') = False
    is_valid_email('mr-bob@example.com') = False
    

版本二可以提取出带名字的Email地址：<br/>
`<Tom Paris> tom@voyager.org => Tom Paris` <br/>
`bob@example.com => bob`
    
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

-->
    
    name_of_email('<Tom Paris> tom@voyager.org') = Tom Paris
    name_of_email('tom@voyager.org') = tom
    
    
## 常用内建模块
#### datetime
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
    
    import re
    from datetime import datetime, timezone, timedelta

    def to_timestamp(dt_str, tz_str):
        m_dt = re.match(r'\d{4}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2}', dt_str) # 没判断时间超过60的情况，太长了
        if m_dt is None:
            raise AttributeError('bad arg dt_str')
        m_tz = re.match(r'UTC([+-])(\d+):([0-9]{2})', tz_str)
        if m_tz is None:
            raise AttributeError('bad arg tz_str')
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')  # 格式化输入字符串
        symbol = m_tz.group(1)
        hour = int(m_tz.group(2))
        hour_int = int(symbol + str(hour))
        minute = int(m_tz.group(3))
        minute_int = int(symbol + str(minute))
        tz_utc = timezone(timedelta(hours=hour_int, minutes=minute_int)) # 创建时区
        dt_utc = dt.replace(tzinfo=tz_utc)  # 设置为指定UTC时间
        return dt_utc.timestamp()  # 把datetime转换为timestamp

    # 测试:
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('ok')
    
#### base64
请写一个能处理去掉=的base64解码函数：

    import base64

    def safe_base64_decode(s):
        while len(s) % 4 != 0:
            # python3中必须要对类型作判断 https://thief.one/2017/04/18/1/
            if isinstance(s, bytes):
                s = s + b'='
            else:
                s = s + '='
        return base64.b64decode(s)

    # 测试:
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    print('ok')
    
#### struct
请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

    import base64, struct

    bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

    def bmp_info(data):
        head_data = data[:30]
        info = struct.unpack('<ccIIIIIIHH', head_data)
        is_windows_bmp = info[0] == b'B' and info[1] == b'M'
        width = info[-4] if is_windows_bmp else 0
        height = info[-3] if is_windows_bmp else 0
        color = info[-1] if is_windows_bmp else 0

        return {
            'width': width,
            'height': height,
            'color': color
        }

    # 测试
    bi = bmp_info(bmp_data)
    assert bi['width'] == 28
    assert bi['height'] == 10
    assert bi['color'] == 16
    print('ok')

#### hashlib
根据用户输入的口令，计算出存储在数据库中的MD5口令：

    import hashlib

    def calc_md5(password):
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    # 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
    db = {
        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9'
    }

    def login(user, password):
        if user in db:
            return db[user] == calc_md5(password)
        return False

    # 测试:
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
    
根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

    import hashlib, random

    def get_md5(s):
        return hashlib.md5(s.encode('utf-8')).hexdigest()

    class User(object):
        def __init__(self, username, password):
            self.username = username
            self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
            self.password = get_md5(password + self.salt)
    db = {
        'michael': User('michael', '123456'),
        'bob': User('bob', 'abc999'),
        'alice': User('alice', 'alice2008')
    }

    def login(username, password):
        if username in db:
            user = db[username]
            return user.password == get_md5(password + user.salt)
        return False

    # 测试:
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
    
#### hmac
将上一节的salt改为标准的hmac算法，验证用户口令：
    
    import hmac, random

    def hmac_md5(key, s):
        return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()
    
    class User(object):
        def __init__(self, username, password):
            self.username = username
            self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
            self.password = hmac_md5(self.key, password)
    
    db = {
        'michael': User('michael', '123456'),
        'bob': User('bob', 'abc999'),
        'alice': User('alice', 'alice2008')
    }
    
    def login(username, password):
        user = db[username]
        return user.password == hmac_md5(user.key, password)
    
    # 测试:
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
    
#### itertools
计算圆周率可以根据公式：<br/>
利用Python提供的itertools模块，我们来计算这个序列的前N项和：
    
    import itertools

    def pi(N):
        ' 计算pi的值 '
        # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
        odd_numbers_1 = itertools.count(1, 2)
        # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
        odd_numbers_2 = itertools.takewhile(lambda x: x <= 2 * N - 1, odd_numbers_1)
        # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
        # 先想到的方法，利用cycle方法有更好的写法
        # symbol = -1
        # def get_odd_number_3(x):
        #     nonlocal symbol
        #     symbol = -symbol
        #     return symbol * 4 / x
        # odd_numbers_3 = map(get_odd_number_3, odd_numbers_2)
        symbol_cycles = itertools.cycle([1, -1])
        odd_numbers_3 = map(lambda x: next(symbol_cycles) * 4 / x, odd_numbers_2)
        # step 4: 求和:
        return sum(odd_numbers_3)
    
    # 测试:
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')
    
-->

    3.0418396189294032
    3.1315929035585537
    3.140592653839794
    3.1414926535900345
    ok
    
#### urllib
利用urllib读取JSON，然后将JSON解析为Python对象：

    from urllib import request
    import json
    
    def fetch_data(url):
        req = request.Request(url)
        with request.urlopen(req) as f:
            # print('Status:', f.status, f.reason)
            # for k, v in f.getheaders():
            #     print('%s: %s' % (k, v))
            # print('Data:', f.read().decode('utf-8'))
            data = f.read().decode('utf-8')
        return json.loads(data)
    
    # 测试
    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
    data = fetch_data(URL)
    print(data)
    assert data['query']['results']['channel']['location']['city'] == 'Beijing'
    print('ok')
    
-->

    {'query': {'count': 1, 'created': '2018-03-05T10:56:02Z', 'lang': 'en-US', 'results': {'channel': {'units': {'distance': 'mi', 'pressure': 'in', 'speed': 'mph', 'temperature': 'F'}, 'title': 'Yahoo! Weather - Beijing, Beijing, CN', 'link': 'http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/', 'description': 'Yahoo! Weather for Beijing, Beijing, CN', 'language': 'en-us', 'lastBuildDate': 'Mon, 05 Mar 2018 06:56 PM CST', 'ttl': '60', 'location': {'city': 'Beijing', 'country': 'China', 'region': ' Beijing'}, 'wind': {'chill': '34', 'direction': '170', 'speed': '18'}, 'atmosphere': {'humidity': '29', 'pressure': '1023.0', 'rising': '0', 'visibility': '16.1'}, 'astronomy': {'sunrise': '6:41 am', 'sunset': '6:11 pm'}, 'image': {'title': 'Yahoo! Weather', 'width': '142', 'height': '18', 'link': 'http://weather.yahoo.com', 'url': 'http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif'}, 'item': {'title': 'Conditions for Beijing, Beijing, CN at 06:00 PM CST', 'lat': '39.90601', 'long': '116.387909', 'link': 'http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/', 'pubDate': 'Mon, 05 Mar 2018 06:00 PM CST', 'condition': {'code': '32', 'date': 'Mon, 05 Mar 2018 06:00 PM CST', 'temp': '41', 'text': 'Sunny'}, 'forecast': [{'code': '32', 'date': '05 Mar 2018', 'day': 'Mon', 'high': '48', 'low': '21', 'text': 'Sunny'}, {'code': '28', 'date': '06 Mar 2018', 'day': 'Tue', 'high': '42', 'low': '24', 'text': 'Mostly Cloudy'}, {'code': '28', 'date': '07 Mar 2018', 'day': 'Wed', 'high': '44', 'low': '28', 'text': 'Mostly Cloudy'}, {'code': '32', 'date': '08 Mar 2018', 'day': 'Thu', 'high': '46', 'low': '27', 'text': 'Sunny'}, {'code': '32', 'date': '09 Mar 2018', 'day': 'Fri', 'high': '53', 'low': '25', 'text': 'Sunny'}, {'code': '32', 'date': '10 Mar 2018', 'day': 'Sat', 'high': '58', 'low': '28', 'text': 'Sunny'}, {'code': '34', 'date': '11 Mar 2018', 'day': 'Sun', 'high': '54', 'low': '29', 'text': 'Mostly Sunny'}, {'code': '32', 'date': '12 Mar 2018', 'day': 'Mon', 'high': '62', 'low': '34', 'text': 'Sunny'}, {'code': '34', 'date': '13 Mar 2018', 'day': 'Tue', 'high': '66', 'low': '38', 'text': 'Mostly Sunny'}, {'code': '30', 'date': '14 Mar 2018', 'day': 'Wed', 'high': '64', 'low': '41', 'text': 'Partly Cloudy'}], 'description': '<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/32.gif"/>\n<BR />\n<b>Current Conditions:</b>\n<BR />Sunny\n<BR />\n<BR />\n<b>Forecast:</b>\n<BR /> Mon - Sunny. High: 48Low: 21\n<BR /> Tue - Mostly Cloudy. High: 42Low: 24\n<BR /> Wed - Mostly Cloudy. High: 44Low: 28\n<BR /> Thu - Sunny. High: 46Low: 27\n<BR /> Fri - Sunny. High: 53Low: 25\n<BR />\n<BR />\n<a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/">Full Forecast at Yahoo! Weather</a>\n<BR />\n<BR />\n<BR />\n]]>', 'guid': {'isPermaLink': 'false'}}}}}}
    ok
    
#### XML
请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：<br/>
https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml<br/>
参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。
    
    from xml.parsers.expat import ParserCreate
    from urllib import request
    
    class DefaultSaxHandler(object):
        def __init__(self):
            self.city = None
            self.forecast = []
    
        def start_element(self, name, attrs):
            # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
            if 'city' in attrs:
                self.city = attrs['city']
            if 'forecast' in name:
                fc = dict(date=attrs['date'], high=attrs['high'], low=attrs['low'])
                self.forecast.append(fc)
    
        def end_element(self, name):
            # print('sax:end_element: %s' % name)
            pass
    
        def char_data(self, text):
            # print('sax:char_data: %s' % text)
            pass
    
    def parseXml(xml_str):
        # print(xml_str)
    
        handler = DefaultSaxHandler()
        parser = ParserCreate()
        parser.StartElementHandler = handler.start_element
        parser.EndElementHandler = handler.end_element
        parser.CharacterDataHandler = handler.char_data
        parser.Parse(xml_str)
    
        return {
            'city': handler.city,
            'forecast': handler.forecast
        }
    
    # 测试:
    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
    
    with request.urlopen(URL, timeout=4) as f:
        data = f.read()
    
    result = parseXml(data.decode('utf-8'))
    print(result)
    assert result['city'] == 'Beijing'
    print('ok')

-->

    {'city': 'Beijing', 'forecast': [{'date': '05 Mar 2018', 'high': '48', 'low': '21'}, {'date': '06 Mar 2018', 'high': '42', 'low': '24'}, {'date': '07 Mar 2018', 'high': '44', 'low': '28'}, {'date': '08 Mar 2018', 'high': '46', 'low': '27'}, {'date': '09 Mar 2018', 'high': '53', 'low': '25'}, {'date': '10 Mar 2018', 'high': '58', 'low': '28'}, {'date': '11 Mar 2018', 'high': '54', 'low': '29'}, {'date': '12 Mar 2018', 'high': '62', 'low': '34'}, {'date': '13 Mar 2018', 'high': '66', 'low': '38'}, {'date': '14 Mar 2018', 'high': '64', 'low': '41'}]}
    ok

#### HTMLParser
找一个网页，例如https://www.python.org/events/python-events/ <br/>
用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

    from urllib import request
    from html.parser import HTMLParser
    from html.entities import name2codepoint
    
    def fetch_data(url):
        req = request.Request(url)
        with request.urlopen(req) as f:
            return f.read().decode('utf-8')
    
    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super(MyHTMLParser, self).__init__()
            self.flag = None
            self.event_info = {}
            self.event_list = []
    
        def handle_starttag(self, tag, attrs):
            # print('starttag: %s, attrs: %s' % (tag, str(attrs)))
            if ('class', 'event-title') in attrs:
                self.flag = 'title'
            if 'time' == tag:
                self.flag = 'time'
            if ('class', 'event-location') in attrs:
                self.flag = 'location'
    
        def handle_endtag(self, tag):
            # print('</%s>' % tag)
            # pass
            self.flag = ''
    
        def handle_startendtag(self, tag, attrs):
            # print('<%s/>' % tag)
            pass
    
        def handle_data(self, data):
            # print(data)
            if self.flag in ('title', 'time', 'location'):
                self.event_info[self.flag] = data
    
            if len(self.event_info) == 3:
                self.event_list.append(self.event_info)
                self.event_info = {}
    
            # if self.flag == 'title':
            #     self.event_info['title'] = data
            #     self.flag = 0
            #
            # if self.flag == 'time':
            #     self.event_info['time'] = data
            #     self.flag = 0
            #
            # if self.flag == 'location':
            #     self.event_info['location'] = data
            #     self.flag = 0
            #     self.event_list.append(self.event_info)
            #     self.event_info = {}
    
        def handle_comment(self, data):
            # print('<!--', data, '-->')
            pass
    
        def handle_entityref(self, name):
            # print('&%s;' % name)
            pass
    
        def handle_charref(self, name):
            # print('&#%s;' % name)
            pass
    
        def print_info(self):
            for n in self.event_list:
                print('title: %s' % n['title'])
                print('time: %s' % n['time'])
                print('location: %s' % n['location'])
                print('-----------------------------------------------------')
    
    # 测试:
    URL = 'https://www.python.org/events/python-events/'
    data = fetch_data(URL)
    # print(data)
    parser = MyHTMLParser()
    parser.feed(data)
    parser.print_info()

-->

    title: PyCon SK 2018
    time: 09 March – 12 March 
    location: Bratislava, Slovakia
    -----------------------------------------------------
    title: PythonCamp 2018 - Cologne
    time: 07 April – 09 April 
    location: GFU Cyrus AG, Am Grauen Stein 27, 51105 Köln, Germany
    -----------------------------------------------------
    title: PyCon IT 9
    time: 19 April – 23 April 
    location: Hotel Mediterraneo - Lungarno del Tempio, 44, 50121 Firenze FI, Italy
    -----------------------------------------------------
    title: PyDays Vienna
    time: 04 May – 06 May 
    location: FH Technikum Wien, Hoechstaedtplatz 6, Vienna, Austria
    -----------------------------------------------------
    title: GeoPython 2018
    time: 07 May – 10 May 
    location: Basel, Switzerland
    -----------------------------------------------------
    title: PyCon US 2018
    time: 09 May – 18 May 
    location: Cleveland, Ohio, USA
    -----------------------------------------------------
    title: PyCon Belarus 2018
    time: 24 Feb. – 25 Feb. 
    location: Minsk, Belarus
    -----------------------------------------------------
    title: PyCon PH 2018
    time: 24 Feb. – 26 Feb. 
    location: Makati City, Metro Manila, Philippines
    -----------------------------------------------------

## 常用第三方模块
#### Pillow
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test11_常用第三方模块_Pillow.py)

## 图形界面
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test12_图形界面.py)

## 网络编程
#### TCP编程
[服务端示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test13_网络编程_TCP编程_服务端.py)<br/>
[客户端示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test13_网络编程_TCP编程_客户端.py)

#### UDP编程
[服务端示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test13_网络编程_UDP编程_服务端.py)<br/>
[客户端示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test13_网络编程_UDP编程_客户端.py)

## 电子邮件
#### SMTP发送邮件
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test14_电子邮件_SMTP发送邮件.py)

#### POP3收取邮件
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test14_电子邮件_POP3收取邮件.py)

## 访问数据库
#### 使用SQLite
请编写函数，在Sqlite中根据分数段查找指定的名字：

    import os, sqlite3

    db_file = os.path.join(os.path.dirname(__file__), 'test15.db')
    if os.path.isfile(db_file):
        os.remove(db_file)
    
    # 初始数据:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    cursor.close()
    conn.commit()
    conn.close()
    
    def get_score_in(low, high):
        ' 返回指定分数区间的名字，按分数从低到高排序 '
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            cursor.execute(r'select name from user where score between ? and ? order by score', (low, high))
            names = [name[0] for name in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()
            return names
    
    # 测试:
    assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
    assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
    
    print('Pass')

#### 使用MySQL
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test15_访问数据库_使用MySQL.py)

#### 使用SQLAlchemy
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test15_访问数据库_使用SQLAlchemy.py)

## Web开发
#### 使用Web框架
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test16_Web开发_使用Web框架.py)

#### 使用模板
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test16_Web开发_使用模板.py)

## 异步IO
#### async/await
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test17_异步IO.py)

#### aiohttp
[示例代码](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/practice/test17_异步IO_aiohttp.py)

## 实战
### webapp
[example](https://github.com/HelloiWorld/PythonPracticeDemo/blob/master/example/webapp)

### to be continued...