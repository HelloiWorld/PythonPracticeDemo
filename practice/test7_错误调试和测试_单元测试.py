#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#错误调试和测试->单元测试
#练习
#对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
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

#修改后
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

#测试
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
