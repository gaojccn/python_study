#!/usr/bin/python
# -*- coding: utf-8 -*-
from types import MethodType


# 面向对象高级编程
# 1.使用__slots__
class Person(object):
    pass


p1 = Person()
p1.name = 'Mike'

print(p1.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# 给一个实例绑定方法
p1.set_age = MethodType(set_age, p1)
p1.set_age(20)
print(p1.age)

p2 = Person()
# p2.set_age(11)  #AttributeError: p2 has no attribute 'set_age'
Person.set_age = set_age  # 为了给所有实例都绑定方法，可以给class绑定方法
p2.set_age(11)
print(p2.age)


# p1.color='red'

class Car(object):
    # 用tuple定义允许绑定的属性名称,特殊的__slots__,只对当前类有效，对子类无效
    __slots__ = ('brand', 'price')

    def __init__(self, brand):
        self.brand = brand


car1 = Car('BMW')
print(car1.brand)


# car1.length='4.5m'  #不能定义length属性
# print(car1.length)

class RunCar(Car):
    pass


car2 = RunCar('Farali')
print('car2.brand:', car2.brand)
car2.oilPer = '10L/100KM'
print('car2.oilPer:', car2.oilPer)

print('----------------------------------------------------------')


# 2.内置的@property装饰器
# 用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        # return self.width*self.height
        return ('%d*%d' % (self.width, self.height))  # 格式化输出


pm = Screen()
pm.width = 1280
pm.height = 720
pm.height = 1080
print('pm.resolution:', pm.resolution)
print(pm.width)
print('----------------------------------------------------------')


# 3.多重继承
class A(object):
    def __init__(self, a):
        print(a)


class B(object):
    def __init__(self, a, b):
        print(a + b)


class C(A, B):
    def __init__(self):
        super(C, self).__init__(B)


c = C()
print('----------------------------------------------------------')


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
# class sample(people,speaker):
class sample(student, speaker):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排最前一个的父类的方法

print('----------------------------------------------------------')


# 4.定制类
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    def __repr__(self):
        return 'Student object (name=%s)' % self.name
        # __repr__ = __str__


s = Student('feizi')
s  # 在python控制台直接敲变量停用 __str__()定义输入不行，要加__repr__()才行
print(s)
print('----------------------------------------------------------')


class PrimeNumbers(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNumber(self, k):
        for i in range(2, k):
            if k % i == 0:
                return False
        return True;

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNumber(k):
                yield k


for x in PrimeNumbers(1, 10):
    print(x)
print('----------------------------------------------------------')


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print('b=', b)
        a, b = b, a + b
        print('b=', b)
        n = n + 1


for data in fab(6):
    print('data is ', data)
print('----------------------------------------------------------')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值

    # 要像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


for n in Fib():
    print(n)
f1 = Fib()
print('F1[4]=', f1[4])
print('f1[4]=Fib()[4] ?', f1[4] == Fib()[4])

print('----------------------------------------------------------')


# 链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        # %s%s将字符串相互联系在一起
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def users(self, value):
        # 递归
        return Chain("%s%s" % (self._path, value))

    __repr__ = __str__

    def __call__(self):
        print('My name is %s.' % self)


repos = Chain().users('michael').repos.com.cn
print(repos)
print('repos is callable:', callable(repos))
print('repos is callable:', callable(123))

dd = Chain('adver')
dd()
print('----------------------------------------------------------')

# 5.枚举
from enum import Enum, unique


# unique 表示不能重复
@unique
class Color(Enum):
    # 格式 name=value
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
    # red_alias = 1  #ValueError: duplicate values found in <enum 'Color'>: red_alias -> red


for name, member in Color.__members__.items():
    print(name, '=>', member, ',', member.value)
# for color in Color.__members__.items():
#	print(color)
# 枚举成员不能进行大小比较
# print(Color.red > Color.blue) #TypeError: '>' not supported between instances of 'Color' and 'Color'

red = Color.red
print(Color['red'])
print(Color.red)
print(Color.blue.name)
print(Color.orange.value)
print(red == Color.red)
print(Color(2))

print('----------------------------------------------------------')


# 6.使用元类
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


'''
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名sayHello上。
'''
Hello = type('Hello', (object,), dict(sayHello=fn))  # 创建Hello class

h = Hello()
print(h)
h.sayHello()
print(type(Hello))
print(type(h))
print('----------------------------------------------------------')

# 元类metaclass，用于创建类，先定义metaclass，然后创建类，最后创建实例
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”
# 参考博客 ：http://blog.jobbole.com/21351/
'''
li=list()
i.add(1)
print(li)
'''


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


myList = MyList()
myList.add('a')
myList.add('b')

for x in range(len(myList)):
    print('myList [%s]=%s' % (x, myList[x]))
print(myList)
