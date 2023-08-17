# -*- coding: utf-8 -*-
def foo():
    return 'asd'
a = lambda: 'asd12'

print(foo())
print(a())
def foo2(x):
    return x ** 2
# print(foo2(4))
foo3 = lambda x: x ** 2
# print(foo3(4))
# foo()
# use def
def sq(x):
    return x*x

print(map(sq, [y for y in range(10)]))

# use lambda
c= map(lambda x: x*x,[y for y in range(10)])
print(list(c))

def is_odd(n):
    return n % 3 == 1

# filter返回的是迭代器，需要使用list转化为列表
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
print(list(filter(lambda x: x % 3 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


names = ["李四", "张三", "王二", "麻子"]
for index, name in enumerate(names, 100):		# 指定index的起始值
    print(f'{index}: {name}')


names = {"a": 122, "b": 222, "c": 333}
for index, name in enumerate(names.keys()):
    print(f'{index}: {name}')