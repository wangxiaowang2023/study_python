# -*- coding: utf-8 -*-
def test_sort(list_t):
    n = len(list_t)
    for i in range(n):
        # 最后一个元素i已经排好序了，无需比较
        for j in range(0, n - i - 1):
            if list_t[j] > list_t[j + 1]:
                list_t[j], list_t[j + 1] = list_t[j + 1], list_t[j]  # 如果前面的数值比后面的数据大，那么前面的数值就和后面的交换顺序


list_r = [1, 3412, 627, 198, 23, 76, 2342, 56456]
# test_sort(list_r)
# print(list_r)


# 冒泡的核心是什么： 是把自己和下一个元素做对比，如果自己比下一个元素大，就把自己和下一个元素换位置。
# 先定义n，数组长度
# 遍历呢。第一层遍历的次数就是 数组的长度， 在第一遍遍历内每次遍历内的遍历对比大小就是。开头到总长减去本次再减1
# 最后就是对比大小了，如果大就换位置，不大就也不处理
def fun1(list1):
    n = len(list1)
    for i in range(n):
        for j in range(n - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                # setattr()
                # return


print(list_r)

fun1(list_r)
print(list_r)