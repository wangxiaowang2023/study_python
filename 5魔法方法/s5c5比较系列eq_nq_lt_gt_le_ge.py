# -*- coding: UTF-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            print("eq被执行了")  # 只有当你在判断两个对象是否相等时，这个方法才会被触发
            return self.name == other.name and self.age == other.age
        return False


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Alice", 25)
# print(person1.name)
print(person1 == person2)  # False，根据 __eq__ 方法的定义，person1 和 person2 不相等
print(person1 == person3)  # True，根据 __eq__ 方法的定义，person1 和 person3 相等
