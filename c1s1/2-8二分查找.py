# -*- coding: utf-8 -*-
# 代码实现，假设列表元素升序排列
def binary_search(target, li):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == li[mid]:		# 刚好找到
            return mid
        elif target < li[mid]:		# 待查值在候选区的左半部分，调整候选区右边界，
            right = mid - 1
        else:						# 待差值在候选区的右半部分，调整候选区左边界
            left = mid + 1
    else:
        return -1

if __name__ == '__main__':
    ll = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search(target=3, li=ll))