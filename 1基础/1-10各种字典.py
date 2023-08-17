from collections import defaultdict


def default_value():
    return 500


dd = defaultdict(default_value)
v1 = dd[1]
print(v1)
# -*- coding: utf-8 -*-
print(dd)