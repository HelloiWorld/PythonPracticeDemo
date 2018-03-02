#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象高级编程->使用枚举类
# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique

#class Gender(Enum):
#    Male = 0
#    Female = 1
#
#class Student(object):
#    def __init__(self, name, gender):
#        self.name = name
#        self.gender = gender

@unique
class Gender(Enum):
    Male = 'male'   # 并不一定非要用数字
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

