# -*- coding: utf-8 -*-

#面向对象编程->实力属性和类属性
#练习
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0 #这里是类变量，是静态变量(只初始化一次，然后存在内存中便于修改访问)，类似于oc中的static关键字
    
    def __init__(self, name):
        self.name = name
        Student.count += 1 #修改时必须修改类属性

print('Student.count =', Student.count)
bart = Student('Bart')
print('Student.count =', Student.count)
lisa = Student('Bart')
print('Student.count =', Student.count)
