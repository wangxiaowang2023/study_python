# -*- coding: utf-8 -*-
import time


class MyRange:
    def __init__(self, total: int, step: int = 1):
        self.count = 0
        self.total = total
        self.step = step

    def __iter__(self):
        print(1111)
        return self  # for循环第一个进入时执行一次，需要返回一个实现了__next__的迭代器对象

    def __next__(self):  # 每次循环取值时执行，最后没有元素可取时需要抛出异常：StopIteration
        time.sleep(0.5)
        self.count += self.step
        if self.count == self.total:
            raise StopIteration
        return self.count


for i in MyRange(16, 2):
    print(i)