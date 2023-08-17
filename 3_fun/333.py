# -*- coding: utf-8 -*-
class Test():
    def __new__(cls, *args, **kwargs):
        print('123123')
    def __init__(self,a):
        print(a)
        print('111')
    def test(self):
        print('222222')

    def __del__(self):
        print('12312')


if __name__ == '__main__':
    c=Test('你好')
    print(c)