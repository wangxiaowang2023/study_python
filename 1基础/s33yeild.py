# -*- coding: utf-8 -*-
def my_range(start,end,step=1):
    while start< end:
        yield start
        start+=step
g=my_range(1,5)
print(g) # 会显示g是一个迭代器对象
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3


def eater():
    print('Ready to eat')
    while True:
        food = yield
        print('get the food: %s, and start to eat' %food)


g = eater()
next(g)				# 传值前必须先调用一次生成器，让生成器先挂起来，等待接收yield赋值给food
g.send('包子')	   # 通过send方法将数据传给yield赋值给food,生成器内部有循环又会再次被挂起
g.send('牛奶')	   # send（）必须要有一个实参
g.send(None)		# 如果send的是None，则默认执行next(g)
