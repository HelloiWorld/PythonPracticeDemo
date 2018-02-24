> 本demo题目来源[廖雪峰老师的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)


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
      
#### 循环
请利用循环依次对list中的每个名字打印出Hello, xxx!：
    
    L = ['Bart', 'Lisa', 'Adam']
    for name in L:
        print("Hello, %s!" % name)
        
 
## 函数
#### 调用函数
请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

    n1 = 255
    n2 = 1000
    print("hex n1: %s" % hex(n1))
    print("hex n2: %s" % hex(n2))

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

    print('quadratic(0, 2, 1) =', quadratic(0, 2, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

#### 函数的参数
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

    def product(*numbers):
    product = 1;
    for number in numbers:
        product = product * number
    return product

    print('product(5) =', product(5))
    print('product(5, 6) =', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
    print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

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

    # 期待输出:
    # A --> C
    # A --> B
    # C --> B
    # A --> C
    # B --> A
    # B --> C
    # A --> C
    move(3, 'A', 'B', 'C')
    
    
    
# to be continued...
