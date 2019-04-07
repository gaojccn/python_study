#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools
import sys


# decorator被称为装饰模式，下面的log(func)在函数调用前后自动打印日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s()' % func.__name__)
        ret = func(*args, **kw)
        print('end call %s()' % func.__name__)
        return ret

    return wrapper


# 作用到函数上
@log
def getName(name):
    print('name=', name)


# 调用函数
getName('gaojc')
print("--------------------------------------")

print(int('010', 2))
# 偏函数functools.partial,把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int, base=2)
print(int2('10101'))

print("--------------------------------------")


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


print(greeting('gao'))
print(greeting('we chinese'))

# 导入sys模块
# sys.path.append('D:\Program Files\Git\bin')
print("sys.path=", sys.path)
