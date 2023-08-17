# -*- coding: UTF-8 -*-
# class Foo:
#     def __del__(self):
#         print('执行我啦')
#
# print('------->')
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("del...")


stu1 = Student("jack", 19)
del stu1  # 触发执行 __del__


def foo():
    print("----- 函数内")
    stu2 = Student("jack", 19)
    print(stu2.__dict__)


x = '1'
print(x)
del x
print(x)

foo()  # foo函数执行结束，触发执行 __del__
