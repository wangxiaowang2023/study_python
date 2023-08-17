# -*- coding: utf-8 -*-
# class Foo(object):
#     staticField = "HAHA"
#
#     def __init__(self):
#         self.name = 'jack'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
#
#
# # getattr(Foo, 'staticField')
# # getattr(Foo, 'func')
# # getattr(Foo, 'bar')
# # print(dir(Foo))
# print(getattr(Foo, 'func2',"13123"))
# print(hasattr(Foo, "bar"))

# class MyClass:
#     def __init__(self, x):
#         self.x = x
#     def my_method(self):
#         # print("My method is called")
#         return "asdas"
#
# obj = MyClass(10)
# attr_value = getattr(obj, "x") # 获取属性值
# method = getattr(obj, "my_method") # 获取方法
# method() # 调用方法
# print(method())
class Foo:
    def __del__(self):
        print('执行我啦')

print('------->')
a = Foo()
