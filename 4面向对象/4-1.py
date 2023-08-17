# -*- coding: utf-8 -*-
# a = dict(c='12',d='12')
# a = dict()

# print(type(a))
from functools import cached_property

class Count:
    # @cached_property
    def add(self):
        f1= []
        a , b = 1,1
        f1.append(a)
        for i in range(10 - 1):
            a , b = b , a+b
            f1.append(a)
        return f1



if __name__ == '__main__':
    c= Count()
    print(c.add())