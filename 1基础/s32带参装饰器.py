# -*- coding: utf-8 -*-


# 实现带参装饰器，打印日志等级
# 知道怎么实现装饰器的话，实现带参装饰器就很简单，就在最外层加一个装饰器就行

def overfun(login):  # 再在最外层加一个函数
    def outfun(fun):  # 先普通实现装饰
        def innerout(*args, **kwargs):
            if login == "debug":
                print(f"------函数的方法名称为：{fun.__name__},日志等级为：debug")
            result = fun(*args, **kwargs)
            if login == "info":
                print(f"-------函数的方法名称为：{fun.__name__},日志等级为：info222222222")
            else:
                print(f"-------函数的方法名称为：{fun.__name__},日志等级为：{login}")
            return result

        return innerout

    return outfun


@overfun(login='debu2g')
def testadd(a, b):
    return a + b


r = testadd(1, 2)
print(r)
