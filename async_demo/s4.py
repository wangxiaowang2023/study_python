# -*- coding: utf-8 -*-
from greenlet import greenlet
import gevent
#
# def f1():
#     print(1)
#     gr2.switch()
#     print(2)
#     gr2.switch()
#
#
# def f2():
#     print(3)
#     gr1.switch()
#     print(4)
#
#
# gr1 = greenlet(f1)
# gr2 = greenlet(f2)
#
# gr1.switch()	# 依次打印：1 3 2 4




def f1():
    print(1)
    gevent.sleep(2)		# 注意不使用time.sleep(2)
    print(2)


def f2():
    print(3)
    gevent.sleep(2)
    print(4)


g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)


gevent.joinall([g1, g2])	# 等待所有函数运行结束，依次打印1 3 -睡2s- 2 4