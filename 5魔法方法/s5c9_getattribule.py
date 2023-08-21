# -*- coding: UTF-8 -*-
class Foo:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, item):
        print('执行的是我')

    def __getattribute__(self, item):
        print('不管是否存在,我都会执行')
        raise AttributeError('哈哈')


f1 = Foo(10)

# f1.x  # 存在
# f1.y # 不存在
a = 2
# print(a.__class__)
# print(f1.__module__)
print(f1.__name__)
