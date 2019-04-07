#!/usr/bin/python
# -*- coding: utf-8 -*-

# 面向对象编程

# 1.创建Student类，集成于object类，所有类都集成顶级的object类
class Student(object):
    # 特殊方法“__init__“，第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
    def __init__(self, name, score):
        self.__name = name  # 加'__'就是变成私有变量，等于是private的了，(java角度理解就是 __name=private String name)
        self.score = score

    def getName(self):
        return self.__name

    def print_score(self):
        print('%s:%s' % (self.__name, self.score))

    def set_score(self, score):
        # 对输入参数校验
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('invalid score')

    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
    def setSpeVirable(self, v1):
        self.__name__ = self.name  # 注意
        if v1 == None:
            self.__v1__ = self.__name__
        else:
            self.__v1__ = v1


gaojc = Student('gaojc', '99')


# class SuperStudent 继承于Student
class SuperStudent(Student):
    # 重写父类的初始化方法
    def __init__(self, name, score):
        self.__name = 'super' + name
        self.name = self.__name  # 注意
        self.score = 'super' + str(score)


liudehua = SuperStudent('liudehua', 90)

print(gaojc)
# print(gaojc.__name)  #报错AttributeError: 'Student' object has no attribute 'name'(无法从外部直接访问内部私有属性)
print(gaojc.score)
# 改变属性值
gaojc.score = 95
print(gaojc.score)
gaojc.print_score()

print(liudehua.score)
# 子类集成了父类的方法
liudehua.set_score(88)
# liudehua.set_score(101) # >100不合法的参数
# liudehua.print_score()

liudehua.setSpeVirable(None)
print('1. liudehua.__v1__:', liudehua.__v1__)
liudehua.setSpeVirable('laohu')
print('2. liudehua.__v1__:', liudehua.__v1__)
liudehua.__name = 'newliudehua'
print(liudehua.__name)
print(gaojc.getName())

print("--------------------------华丽的分割线----------------------------")


# 2.继承和多态
class Animal(object):
    # python新模式的class，即从object继承下来的类有一个变量是__slots__，slots的作用是阻止在实例化类时为实例分配dict，
    # 默认情况下每个类都会有一个dict,通过__dict__访问，这个dict维护了这个实例的所有属性
    __slots__ = ('animal',)  # 阻止在实例化类时为实例分配dict
    animal = "pig"  # 被阻止了

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


class Timer(object):
    def run(self):
        print('Start Timer...')


a = Animal()
d = Dog()
c = Cat()
timer = Timer()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))  # 父类不是一种子类

print('d is Animal?', isinstance(d, Animal))  # 子类是一种父类 (多态)
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

print('timer is Animal?', isinstance(timer, Animal))
# 传入Timer类型的变量也行，只要timer里面有run()方法就行
run_twice(timer)

run_twice(c)
run_twice(a)
# type判断变量/对象的类型 type函数返回对应的Class类型
print(type(timer))
print(isinstance(d, Dog) and isinstance(1, int))
# 获得一个对象的所有属性和方法，可以使用dir()函数
print("dir(a)=", dir(a))

print(a.__slots__)
print(c.__eq__(c))
print(d.__hash__())

c.__setattr__('color', 'red')
print(c.color)  # 知道c有color属性，就不用下面那写法了
print(getattr(c, 'color'))
cc = getattr(d, 'z', 404)  # 找不到返回默认值404
print(cc)
crun = getattr(c, 'run')  # 获取c的run()方法，赋值给crun
print(crun)
crun()

print('----------------------------------------------------------')


# 在继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例
# self 相当于java的this
class Parent:
    def __init__(self, name):
        self.name = name

    def pprt(self):
        print(self.name)


class Child(Parent):
    def cprt(self):
        print(self.name)


c = Child('Child')
c.cprt()
c.pprt()  # Child  打印的是传入的实例的名字
print(c.name)  # Child

p = Parent('Parent')
p.pprt()
print(p.name)
print(getattr(p, 'name'))


class Desc:
    # object.__get__(self, instance, owner) 只用在descriptor中。可以通过owner class或者instance来访问属性
    # instance是调用者实例 ，
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self)
        print(self, ins, cls)


class Test:
    desc = Desc()

    def prt(self):
        print('self in Test: %s' % self)


t = Test()
t.prt()
t.desc
Test.desc
# '''    3个单或双引号是多行注释
'''总结 
    self在定义时需要定义，但是在调用时会自动传入。
    self的名字并不是规定死的，但是最好还是按照约定是用self
    self总是指调用时的类的实例。
'''
print('----------------------------------------------------------')


# 3.实例属性和类属性
# 为了统计球的数量，可以给Ball类增加一个类属性，每创建一个实例，该属性自动增加：
# 当实例和类有相同属性时，优先访问实例属性，如果实例没有某个属性，那么就会访问类属性，如果都没有，就报错
class Ball(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Ball.count += 1  # 每个Ball实例化,把Ball的类属性count+1

    # 类方法。用@classmethod定义
    @classmethod
    def doAddBal(self, ballName):
        Ball(ballName)  # 创建新的实例
        print('add a new ball：', ballName)


if Ball.count != 0:
    print('测试失败')
else:
    ftb = Ball('footBall')
    if Ball.count != 1:
        print('测试失败')
    else:
        bskb = Ball('basketBall')
        if Ball.count != 2:
            print('balls:', Ball.count)
            print('测试失败')
        else:
            print('balls:', Ball.count)
            print('测试通过')

# doAddBal()
print(Ball.count)
footb = Ball('footBall')
footb.count = 'footb.count'
print('footb.count:', footb.count)
print('footb.name:', footb.name)
print('Ball.count:', Ball.count)

# 调用函数，第一个参数默认传入了对象本身，t.func()等同于t.fun(t)
footb.doAddBal('bal1')
Ball.doAddBal('ball2')
print('Ball.count:', Ball.count)
print(Ball.__reduce__(footb))
