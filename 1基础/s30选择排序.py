# -*- coding: utf-8 -*-


def selection_sort(list1):
    n=len(list1) # 遍历循环的次数是n
    for i in range(n-1):
        min_index = i # 假设当前是最小的
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]

list1 = [23, 45, 78, 21, 6, 567, 75, 67906, 34507, 359, 9089, 80]

selection_sort(list1)
print(list1)
