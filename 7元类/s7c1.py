# -*- coding: utf-8 -*-
def __init__(self, name, age):
    self.name = name
    self.age = age


def talk(self):
    print('hello')


class_name = "Student"
class_bases = (object, )
class_dict = {"__init__": __init__, "talk": talk}


Student = type(class_name, class_bases, class_dict)

stu = Student("jack", 18)
print(stu.talk())