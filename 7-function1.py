#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import locale
import math

from functools import reduce
from collections import Iterable

import os
import operator

# 函数学习1 调用函数

compare = operator  # operator是python3自带的比较函数，可以把函数赋值给一个变量

print(compare.le(1, 3))  # 比较1小于3?

print(abs(1 - int('3')))

print(bool(1 - 3 > 0))
print("--------------------------------")

# 函数学习2 自定义函数
# 2.1
tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print(tour)
print(height)

print("--------------------------------")
# 2.2range()函数，下面是生成9到0的序列，步长是-1#################
# 函数原型：range（start， end， scan):
# 参数含义：start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
# end:技术到end结束，但不包括end.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
for r in range(9, 0, -2):
    print(r)

print("--------------------------------")
sequence = [12, 34, 34, 23, 45, 76, 89]

# 遍历数组，通过下标索引
for key in range(len(sequence)):
    print(key, sequence[key])
# 遍历数组，通过迭代器enumerate
for i, j in enumerate(sequence):
    print("index:" + str(i) + ",value:" + str(j))

print("--------------------------------")


# 2.2 函数传参
# 关键字参数 顺序不重要,
# -----------注意：必选参数在前，默认参数在后------------
def printinfo(name, age=20):
    "打印任何传入的字符串"
    print("name: ", name)
    print("age:", age)
    return;


# printinfo(age=36,name='Ibracimovic')
# 调用的时候，既可以按顺序提供默认参数,也可以不按顺序提供部分默认参数,当不按顺序提供部分默认参数时，需要把参数名写上
printinfo('Ibracimovic', 36)
printinfo('Ibracimovic', age=35)
printinfo('Ibracimovic')  # 第二个参数不传，就使用默认参数

print("--------------------------------")

# 2.3全局变量和局部变量
total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total;


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)

print("--------------------------------")

st = "你好"
print(st)

# 将utf-8的str转换为unicode，注意，python3的默认的文本字符串为unicode格式，因此文本字符串没有decode方法
# st=st.decode("utf-8")
st = st.encode('gbk')  # 将unicode转换为str，编码为GBK
print('st in encode gbk=', st)
print('st=', st.decode('gbk'), ',type(st)=', type(st), ",len(st)=", len(st))

print("--------------------------------")


def reverse(ListInput):
    RevList = []
    for i in range(len(ListInput)):
        RevList.append(ListInput.pop())
    return RevList


arr = [0, 1, 2, 3, 4]
print("arr=", reverse(arr))

print("--------------------------------")


def p(f):
    print('%s.%s(): %s' % (f.__module__, f.__name__, f()))


# 返回当前系统所使用的默认字符编码
p(sys.getdefaultencoding)
# 返回用于转换Unicode文件名至系统文件名所使用的编码
p(sys.getfilesystemencoding)
# 获取默认的区域设置并返回元祖(语言, 编码)
p(locale.getdefaultlocale)

print("--------------------------------")


def retTwoVal(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


a, b = retTwoVal(10, 20, 2, 30)
print(a, b)

print("--------------------------------")


# 定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())

print("--------------------------------")


# 可变参数，从0到n个都可以 [格式是 在行参前面加*]
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


print(calc(1, 2, 3, 4, 5))
print(calc(1, 2))
print(calc(0))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))

print("--------------------------------")


# 关键字参数 [**paramName],可以传入任意个数的关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('gaojc', 29, phone=18110012200)
person('Xiaomi', 18)
person('wangnima', 14, sex='male', weight='100kg')
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
kw = {'sex': 'female', 'weight': '45kg'}
person('mengnv1', 20, **kw)


# 定义一个函数，包含上述4种参数：必选参数、默认参数、可变参数和关键字参数
def func(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


func(1, 2, 3, 'x', 'y', city='hefei')

print("--------------------------------")


# 递归函数
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print('递归函数fact(4)=', fact(4))


def digui(n):
    if (n == 1):
        return 1
    return n * digui(n - 1)


print('digui(5)=', digui(5))

# tuple切片
tup1 = (0, 1, 2, 3, 4, 5)[:3]
print(tup1)

print("--------------------分割线-------------------")

numSeq100 = range(100)

print("numSeq100 first 10 nums=", numSeq100[:10])
print("get once every 5 num=", numSeq100[::5])

tljr = 'allinChina'
print("string 'tljr'.split [3:5]=", tljr[3:5])

# 迭代字符串
for x in tljr:
    print(x, )  # python2不换行的写法 print something,

# tljr 这个字符串是否可以迭代
print("tljr isIterable ?", isinstance(tljr, Iterable))
# 给字符串加下标打印，把一个list变成索引-元素对
for i, value in enumerate(tljr):
    if (i == len(tljr) - 1):
        print(i, value, '\n', )
    else:
        print(i, value, '\t', )
print("--------------------分割线--------------------")
# 对循环的每个元素作运算,在一行代码实现
numSeq2 = [x * x for x in range(1, 11)]
print(numSeq2)

# 双重循环生成排列组合
doubleSeq = [m + n for m in 'ABC' for n in 'XYZ']
print(doubleSeq)

filesDirList = [d for d in os.listdir('E:\maven')]
print('filesDirList=', filesDirList)

print("-------------------分割线-----------------------")

# generator生成器
generator1 = (x * x for x in range(10))

print('generator1=', generator1)
print(generator1.__next__)
print(generator1.__next__())
print("------上面是打印generator1.next(),下面是打印所有的generator1------------")
for x in generator1:
    print(x)

print("----------------------分割线-------下面看map和reduce的用法--------------")
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
# 把这个list所有数字转为字符串
strMap = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print('map use on a number list:', strMap)
for e in strMap:
    print(e)


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算 :
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn1(x, y):
    return x * 10 + y


toInteger = reduce(fn1, [1, 2, 3])
print('reduce use on a number list:', toInteger)


# map和reduce结合使用
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


print(str2int('12345'))
print("----------------------分割线--------------------------")


# 利用filter()函数删除1~100的素数
def delPrimeNum(n):
    if n > 1:
        for x in range(2, n):
            if (n % x) == 0:
                return False
                break
        else:
            return True
    else:
        return False


primeNumsIn100 = filter(delPrimeNum, range(1, 101))
print('prime Nums In100=', primeNumsIn100)
for num in primeNumsIn100:
    print(num)
print("----------------------分割线--------------------------")


# 用内置的sorted()函数来排序
# 对单词排序，忽略字母的大小写，先转成大写来
def cmp_ignore_case(s1):
    u1 = s1.lower()
    print('u1=', u1)
    return u1


slist = ['bob', 'about', 'Zoo', 'Credit']
# 转化小写
slist = map(cmp_ignore_case, slist)
sortedStr = sorted(slist, reverse=True)
# 反转  Python 3.x的sorted(iterable, key=None, reverse=False)
print(sortedStr)

print("----------------------分割线--------------------------")


# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f1Val = f1()
print("f1Val=", f1Val)

# 匿名函数lambda
lanb1 = lambda x=0: x * x
anonyV = map(lanb1, [1, 2, 3])
for x in anonyV:
    print("anonyV element =", x)
# 函数的"__name__"属性
print(lanb1.__name__, lanb1.__module__)
