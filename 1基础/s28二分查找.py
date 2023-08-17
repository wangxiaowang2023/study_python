# -*- coding: utf-8 -*-
# 二分查找的重点是从中间截取数据


def c_get(target, list_a):
    # 先定义最左和最右边的下表
    left = 0
    right = len(list_a) - 1
    while left <= right:  # 开始无限循环
        mid = (left + right) // 2
        if target == list_a[mid]:
            return mid
        elif list_a[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  # 查找成功了，结束了，返回-1


# 测试
# sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target_element = 18
#
# result = binary_search(sorted_list, target_element)
#
# if result != -1:
#     print(f"目标元素 {target_element} 在索引 {result} 处找到。")
# else:
#     print("未找到目标元素。")

if __name__ == '__main__':

    test = [1, 2, 3,  5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19]
    m = 4
    result2 = c_get(target=m, list_a=test)
    if result2 != -1:
        print('z找到了')
    else:
        print('没找到')

# 现找到这个列表的中间元素
# 如果没找到，就继续找这左右一半的列表中的中间的，
#
