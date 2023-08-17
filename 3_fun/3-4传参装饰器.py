# -*- coding: utf-8 -*-
import time


def wrapper(flag):
    def outer(func):
        def inner(*args, **kwargs):
            start = time.time()
            rets = func(*args, **kwargs)
            end = time.time()
            if flag == "am":
                print(f'{func}运行用时(am):{end - start}s')
            elif flag == "pm":
                print(f'{func}运行用时(pm):{end - start}s')
            return rets

        return inner
    return outer


@wrapper("am")
def foo(x, y):
    time.sleep(1)
    return x + y


print(foo(3, 4))