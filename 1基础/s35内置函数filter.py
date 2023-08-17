# -*- coding: utf-8 -*-
# 看源码是返回其为真的值，意思就是定义一个规则，然后返回符合这个规则的数据
# 如果方法为空，则返回为真的项
# 看源码 def __init__(self, function_or_None, iterable): 第一个是方法orNone 第二个入参是可迭代对象
def fun(x):
    return x%2==0 # 除以2的余数是0，也就是说能被2整除


list1 = [1,2,3,4,5,6,7,8,9,10,12,142,352,4235,56,57,86,12,11]
a=filter(fun,list1)
print(a)  # 是一个filter对象 需要转化一下接收他
print(list(a))  # 是一个filter对象 需要转化一下接收他
# 用lambda实现

b=filter(lambda x:x%2==0,list1)
print(list(b))