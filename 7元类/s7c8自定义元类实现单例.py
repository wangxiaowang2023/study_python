# -*- coding: utf-8 -*-
class Mymeta(type):
    def __init__(cls, name, bases, dic):
        super().__init__(name, bases, dic)
        cls._instance = None  # 将记录类的实例化对象的数据属性放在元类中自动定义了 # 这里和之前定义类的时候是一个意思

    def __call__(cls, *args, **kwargs):  # 此call会在类被调用（即实例化时出发）
        if cls._instance:  # 判断类有没有实例化对象
            return cls._instance  # 如果有就返回这个实例化对象啊
        else:  # 如果没有
            obj = cls.__new__(cls, *args, **kwargs)  # 那就控制类造一个空对象并完成初始化
            obj.__init__(*args, **kwargs)  # 那就控制类造一个空对象并完成初始化
            cls._instance = obj  # 保存这个对象，那cls的_instance是这个对象，下一次再实例化的时候就直接返回而不用再造对象
            return obj  # 返回这个对象


class Student(metaclass=Mymeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student("jone", 18)
stu2 = Student('xiaoming', 19)
print(stu1 is stu2)
print(stu1.__dict__, stu2.__dict__)
# class Mymeta(type):
#
#     def __init__(cls, name, bases, dic):
#         super().__init__(name, bases, dic)
#         cls._instance = None		                  # 将记录类的实例对象的数据属性放在元类中自动定义了
#
#     def __call__(cls, *args, **kwargs):	    # 此call会在类被调用（即实例化时触发）
#         if cls._instance:				  # 判断类有没有实例化对象
#             return cls._instance
#         else:						  # 没有实例化对象时，控制类造空对象并初始化
#             obj = cls.__new__(cls, *args, **kwargs)
#             obj.__init__(*args, **kwargs)
#             cls._instance = obj			          # 保存对象，下一次再实例化可以直接返回而不用再造对象
#             return obj
#
#
# class Student(metaclass=Mymeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# stu1 = Student('jack', 18)
# stu2 = Student('ja1ck', 128)
# print(stu1 is stu2)
# print(stu1.__dict__, stu2.__dict__)

# 原理：类定义时会调用元类下的__init__，类调用(实例化对象)时会触发元类下的__call__方法
# 类定义时，给类新增一个空的数据属性，
# 第一次实例化时，实例化之后就将这个对象赋值给类的数据属性；第二次再实例化时，直接返回类的这个数据属性
# 和方式3的不同之处1：类的这个数据属性是放在元类中自动定义的，而不是在类中显示的定义的。
# 和方式3的不同之处2：类调用时触发元类__call__方法判断是否有实例化对象，而不是在类的绑定方法中判断