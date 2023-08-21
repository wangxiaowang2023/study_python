# -*- coding: UTF-8 -*-
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# 创建 Singleton 类的实例
obj1 = Singleton()
print(id(obj1))
obj2 = Singleton()
print(id(obj2))

print(obj1 is obj2)  # 输出：True，因为 obj1 和 obj2 引用同一个实例
