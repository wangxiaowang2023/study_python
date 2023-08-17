# -*- coding: utf-8 -*-
from itertools import chain

# b = [[1, 2], [3, 4], [5, 6]]
# for c in b:
#     print(c)
# print(b)
# for i in chain(*b):
#     print(i)  # 1,2,3,4,5,6
#
# e =list(chain(*b))
# print(e)
# d = {'one':{'a': 1, 'b': 2}, 'two':{'c': 3, 'd': 4}, 'three':{'e': 5, 'f': 6, 'g': "asdas"}}
# print(d)
# old_list = [[1, 2, 3], [6, 3, 5, 8], [2, 3, 5, 8, 9, 0]]

# for i in old_list:
#     # print(i)
#     for m in i:
#         print(m)
# new_list = [ m for i in old_list for m in i]
# print(new_list)
# new_list_2 = list(chain(*old_list))
# print(new_list_2)

# new_list_3 = []
# for i in old_list:
#     # print(i)
#     for m in i:
#         # print(m)
#         new_list_3.append(m)
# print(list(set(new_list_3)))
#
# new_list_4 = list(set(m for i in old_list for m in i ))# 但是这么做会破坏原有的顺序
# print(new_list_4)
#
# new_list_5 = []
# for i in old_list:
#     # print(i)
#     for m in i:
#         if m not in new_list_5:
#         # print(m)
#             new_list_5.append(m)
# print(list(set(new_list_5)))


# old_list = [[1, 2, 3], [6, 3, 5, 8], [2, 3, 5, 8, 9, 0]]
# # 需要输出，去嵌套，去重，且不破坏顺序的新列表
# # 先定义新列表和新集合 因为去重用集合最好
# new_list = []
# new_set = set()
# # 开始循环
# for i in old_list:
#     m_list = [] # 中转列表
#     for m in i :
#         if m not in new_set:
#             m_list.append(m)
#             new_set.add(m)
#     new_list.append(m_list) # 此时new_list = [[1, 2, 3], [6, 5, 8], [9, 0]] 变成这样了就好祛除嵌套了
#
# over_list = [m for i in new_list for m in i ]
# print(over_list)

import itertools

old_list = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]
print(old_list)


def fun1():
    result1 = [m for i in old_list for m in i]
    print(result1)


def fun2():
    result2 = itertools.chain(*old_list)  # 是一个chain对象，不可以直接打印。需要转换成list
    print(list(result2))


def fun3():
    result3 = sum(old_list, start=[])
    print(result3)


# fun1()
# fun2()
# fun3()

a = [[1, 2, 3], [8, 2, 5], [1, 5, 9]]
# test1 = list(set(itertools.chain(*a)))
# test2 = list(set(m for i in a for m in i))
# test3 = list(set(sum(a, start=[])))
# print(test1)
# print(test2)
# print(test3)
# for i n
new_list = []
test_set = set()
for i in a:
    m_list = []
    for m in i:
        if m not in test_set:
            m_list.append(m)
            test_set.add(m)
    new_list.append(m_list)
# print(new_list)
over_list = [m for i in new_list for m in i]
print(over_list)
test2 =list(dict.fromkeys(itertools.chain(*a)))
print(test2)

# new_list2 = list(dict.fromkeys(chain.from_iterable(old_list)))
