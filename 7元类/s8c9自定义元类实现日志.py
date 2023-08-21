# -*- coding: utf-8 -*-
class DebugMeta(type):
    def __new__(cls, name, bases, cls_dict):
        for attr_name, attr_value in cls_dict.items():
            if callable(attr_value):  # 检查属性是否是可调用的（方法）
                cls_dict[attr_name] = cls.debug_decorator(attr_value)  # 使用装饰器替换方法
        return super().__new__(cls, name, bases, cls_dict)

    @staticmethod
    def debug_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs},modu:{func.__module__}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result

        return wrapper


class DebugClass(metaclass=DebugMeta):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def create(self, a, b):
        return a * b


# 使用
debug_instance = DebugClass()
result = debug_instance.add(5, 3)
# print(result)
result2 = debug_instance.create(a=8,b=3)
print(result2)