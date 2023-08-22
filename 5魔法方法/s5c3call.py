# -*- coding: UTF-8 -*-
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function is called")
        result = self.func(*args, **kwargs)
        print("After function is called")
        return result


@MyDecorator
def my_function(x, y):
    return x + y


result = my_function(3, 5)
print("Result:", result)
