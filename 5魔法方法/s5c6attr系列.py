# -*- coding: UTF-8 -*-
class Person:

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print('调用不存在的属性会触发我')
        return self.__dict__.get(item)
        # return self.item      # 不能使用，会造成递归。

    def __setattr__(self, key, value):
        print('设置修改对象属性时触发我')
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('删除对象属性时触发我')
        self.__dict__.pop(item)


p = Person('jack')  # 触发__setattr__


# p.name = 'mack'         # 触发__setattr__
# print(p.age)            # 触发__getattr__
# p.age = 18              # 触发__setattr__
# print(p.age)
# del p.age               # __delattr__


class MyDict(dict):
    abc = "abc"

    def __getattr__(self, item):
        print("字典对象通过点访问不存在的属性时触发")
        return self.get(item)

    def __setattr__(self, key, value):
        if not isinstance(value, str):
            raise ValueError('值必须是字符串类型')
        self[key] = value


d = MyDict({'name': 'jack'})
print(d.name)  # 触发 __getattr__
print(d.abc)  # 没有触发 __getattr__
