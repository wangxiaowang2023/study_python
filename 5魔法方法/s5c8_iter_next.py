# -*- coding: UTF-8 -*-
import time


class MyRange():
    def __init__(self, total: int, step: int = 1):
        self.count = 0  # 这里都是定义属性
        self.total = total
        self.step = step

    def __iter__(self):  # 这个要返回迭代器对象
        print("1111")
        return self  # for循环第一个进入时执行一次，需要返回一个实现了__next__的迭代器对象

    def __next__(self):  # 这里实现迭代器
        time.sleep(0.5)
        self.count += self.step  # 没次运行加1或者自定义的数
        if self.count == self.total:
            raise StopIteration  # 如果count计数等于total总数就抛出异常
        return self.count


for i in MyRange(10, 2):
    print(i)
