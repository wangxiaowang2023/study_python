# -*- coding: utf-8 -*-
# 通过Process库
import multiprocessing
from multiprocessing import Process


# 定义一个方法

def work_fun(name):
    print(f"这个是一个函数方法={name}")


if __name__ == '__main__':
    process = multiprocessing.Process(target=work_fun, args=[
        "args必须以可迭代对象的形式传参，几个对象就传几个进去", ])  # target=并发执行的进程，函数方法
    # process.join()
    process.start()
    process.join()
