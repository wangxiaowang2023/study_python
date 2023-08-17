# -*- coding: utf-8 -*-
#     def __init__(self, iterable, start=0): # known special case of enumerate.__init__
# enumerate对象产生一对包含一个计数(从start开始，默认为0)和一个由iterable参数产生的值。Enumerate用于获取索引列表:(0,seq[0])， (1, seq[1])， (2, seq[2])，
# 还可以通过传递 start 参数来指定起始的索引值：aa
lis1 = ["asd","asdasda","wqeerw","213"]
a=enumerate(lis1)
for i in a:
    print(i)
print("sadas")


print(dir(lis1))