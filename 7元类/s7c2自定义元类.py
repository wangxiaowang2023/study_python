# -*- coding: utf-8 -*-
class Student(metaclass=type):  # class机制默认的元类是type：我们可以修改metaclass参数来选择自定义元类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('hello')


class Mymeta(type):  # 只有继承了type的类才能作为元类使用
    pass


class Student2(metaclass=Mymeta):  # 使用Mytema元类，即Mymeta(class_name, class_bases, class_dict)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('hello')


class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dict):

        if not class_name.istitle():  # 自定制需求 istitle()用于检查字符串的首字母是否大写，如果大写就是Ture，否则Flase
            raise NameError('类名首字母必须大写')

        if not self.__doc__:  # # 如果类的__doc__属性是空，就抛出异常 doc就是注释那里
            raise TypeError('类必须要有文档注释')

        super().__init__(class_name, class_bases, class_dict)


# People = Mymeta(class_name, class_bases, class_dict),
class People(object, metaclass=Mymeta):
    """
    deox这里就是__doc__属性
    """
    x = 10

    def f(self):
        pass


print(People.__dict__)