# -*- coding: utf-8 -*-

def fun(x,y):
    return x+y
add = lambda x,b:x+b

c=add(1,5)
print(c)


def sq(x):
    return x*x


# 常规：
map(sq,[y for y in range(10)])
map(lambda x:x*x,[y for y in range(10)])
