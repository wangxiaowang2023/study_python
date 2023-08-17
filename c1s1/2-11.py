# -*- coding: utf-8 -*-
list1 = [{"id":3},{"id":5},{"id":1}]
def sort(x):
    return x['id']
list1.sort(key=sort)
print(list1)