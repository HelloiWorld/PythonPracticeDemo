# -*- coding: utf-8 -*-

#面向对象编程->访问限制
#练习
#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
#class Student(object):
#    def __init__(self, name, gender):
#        self.name = name
#        self.gender = gender

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
        #if gender in ('male','female'):
            self.__gender = gender
        else:
            raise ValueError('bad gender')
#测试
bart = Student('Bart', 'male')
print('bart.get_gender() =', bart.get_gender())
bart.set_gender('female')
print('after bart.set_gender(\'female\'), bart.get_gender() =', bart.get_gender())

