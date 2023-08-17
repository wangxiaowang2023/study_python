# -*- coding: utf-8 -*-
from collections import namedtuple,OrderedDict
Point = namedtuple('point',["x","y"])
print(Point)
p = Point(11,22)
print(p.x,p.y)
print(p)

OrderedDict_1 =OrderedDict(name="a",age="2")


for k,v in OrderedDict_1.items():
    print(k,v)
for i in range(5):
    OrderedDict_1[i]=i*2
print(OrderedDict_1)
OrderedDict_1.move_to_end("name",last=True)
print(OrderedDict_1)