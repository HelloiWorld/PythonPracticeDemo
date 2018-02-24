> 本demo练习题目来源[廖雪峰老师的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)</br>
  学习资源: [Crossin的编程教室](http://res.crossincode.com/wechat/index.html)

## Python基础
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
的两个解。
提示：计算平方根可以调用math.sqrt()函数：    
    
    import math

    def quadratic(a, b, c):
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
           raise TypeError('bad operand type')
        if b == 0:
            if a * c < 0:
                x1 = math.sqrt(-(a / c))
                x2 = -math.sqrt(-(a / c))
                return x1, x2
            elif c == 0:
                return 0
            else:
                raise TypeError('no answer')
        elif a == 0:
            x = -(c / b)
            return x
        else:
            x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            return x1, x2
    
测试

    print('quadratic(0, 2, 1) =', quadratic(0, 2, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

-->
    
    quadratic(0, 2, 1) = -0.5
    quadratic(1, 3, -4) = (1.0, -4.0)
    
#### 函数的参数
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

    def product(*numbers):
    product = 1;
    for number in numbers:
        product = product * number
    return product
    
测试

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
    
测试

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
        return ''
    head = 0
    headStr = s[head]
    while headStr == ' ':
        head = head + 1
        if head >= len(s):
            return ''
        headStr = s[head]
    tail = -1
    tailStr = s[tail]
    while tailStr == ' ':
        tail = tail - 1
        tailStr = s[tail]
    tailIndex = len(s) + tail + 1   #向右偏移一个元素，防止最后一个取不到
    return s[head:tailIndex]

测试

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
    
测试

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
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str)]
    print('lower([\'Hello\', \'World\', 18, \'Apple\', None]) =' , L2)

#### 生成器
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
        #print('befor yield: L =', L)
        L.append(0)
        #print('after yield: L =', L)
        #print('[L[i-1] for i in range(len(L))] =', [L[i - 1] for i in range(len(L))])
        #print('[L[i] for i in range(len(L))] =', [L[i] for i in range(len(L))])
        L = [L[i - 1] + L[i] for i in range(len(L))]]
        #print('after triangles: L =', L)
        
 测试
 
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
    print(results)
    
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
    [[1, 0], [1, 1, 0], [1, 2, 1, 0], [1, 3, 3, 1, 0], [1, 4, 6, 4, 1, 0], [1, 5, 10, 10, 5, 1, 0], [1, 6, 15, 20, 15, 6, 1,  0], [1, 7, 21, 35, 35, 21, 7, 1, 0], [1, 8, 28, 56, 70, 56, 28, 8, 1, 0], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
    
> 思考：为什么t的打印结果与append到results后显示结果不同?

# to be continued...
