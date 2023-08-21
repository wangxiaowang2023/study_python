# -*- coding: utf-8 -*-
class Mymeta(type):
    def __call__(cls, *args, **kwargs):
        # 第一步: 调用Student下面的__new__创建一个空对象, 无则使用类(type)的__new__
        obj = cls.__new__(cls,*args, **kwargs)
        print("111")
        # 第二步：调用Student下面的__init__初始化对象
        cls.__init__(obj, *args, **kwargs)  # 等价于： obj.__init__(*args, **kwargs)
        # 第三步：返回对象
        return obj


class Student(object, metaclass=Mymeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age


jack = Student('jack', 18)  # People.__call__('jack', 18)
