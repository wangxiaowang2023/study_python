# -*- coding: utf-8 -*-


class Foo():
    def add(self):
        f1 = []
        a,b = 1,1
        f1.append(a)
        for i in range(20-1):
            a,b = b, a+b
            f1.append(a)
        return f1

if __name__ == '__main__':
    f = Foo()
    print(f.add())