# -*- coding: UTF-8 -*-
class Person(object):

    def __init__(self, name):
        self.name = name

    def __setitem__(self, key, value):
        print("[]设置值时触发")
        setattr(self, key, value)

    def __getitem__(self, item):
        print("[]取值时触发")
        return getattr(self, item)

    def __delitem__(self, key):
        print("del p[key]时触发", key)


p = Person('jack')
p['name'] = 'mack'  # 需要__setitem__才可以
print(p['name'])  # 需要__getitem__才可以
print(p.__dict__)

del p["name"]  # 需要__delitem__才可以
