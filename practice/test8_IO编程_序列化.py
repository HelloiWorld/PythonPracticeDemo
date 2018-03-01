#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# IO编程->序列化
# 练习
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)  #默认，中文会转成Unicode编码
s2 = json.dumps(obj, ensure_ascii=False)

print('s = %s' % s)
print('s2 = %s' % s2)



# 一个通用Json转Model的例子

def jsonToClass(class_name, json_str):
    # <class '__main__.Student'> 其实就是根据一个示例找到它的类，然后截取出类名而已
    class_name_str = str(type(class_name))[str(type(class_name)).find('.') + 1:-2]
    obj = eval(class_name_str + '()')
    for key, value in json.loads(json_str).items():
        setattr(obj, key, value)
    return obj

class Student(object):
    pass

s = jsonToClass(Student(),'{"name":"123","age":16}')
print(s)