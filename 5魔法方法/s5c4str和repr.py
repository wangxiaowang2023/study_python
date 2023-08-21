# -*- coding: UTF-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


person = Person("Alice", 30)
print(person)  # Output: Person(name=Alice, age=30)

# sut = Student("name","age")
# print(sut) # 这个时候打印出来的内容，就是str方法return出来的内容
