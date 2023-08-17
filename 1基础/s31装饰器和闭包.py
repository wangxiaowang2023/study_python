# -*- coding: utf-8 -*-

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)


def outfun(fun):
    def innerfun(*args,**kwargs):
        print(f"当前方法的名称是：{fun.__name__}")
        re = fun(*args,**kwargs)
        print(f"当前方法的名称是：{fun.__name__}")
        return re
    return innerfun

@outfun
def testfun(a,b):
    return a+b

r=testfun(1,2)
print(r)