# -*- coding: utf-8 -*-
l = ['aa','bb','cc','dd']


# for i in l:
    # print(i)

gl = iter(l)
while 1:
    try:
        print(next(gl))
    except StopIteration:
        break