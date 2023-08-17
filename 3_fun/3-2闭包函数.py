# -*- coding: utf-8 -*-
def outer():
    x = 10
    def inner():
        return x + 1	# 此时 inner是闭包函数（引用了外层函数作用域的变量）
    return inner


# x = 10
# def outer():
#     def inner():
#         return x + 1	# 此时，inner不是闭包函数(没有引用外层函数作用域的变量)
#     return inner

f=outer()
print(f())