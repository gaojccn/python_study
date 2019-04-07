#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python的注释是 #打头 (单行注释)

# 1.基本类型变量
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "wonderful"  # 字符串

a, b, c = 1, 2, 3  # 多个变量一起赋值

print("整型变量counter=", counter)
print('浮点型变量 miles=', miles)
print('字符串 name=', name)
print('把miles转为整型int =', int(miles))  # int()是类型转换
print('多个变量a,b,c=', a, ',', b, ',', c)

# 打印换行
print('\n')
# 2.查看变量的类型
print('查看变量的类型如下:')
print(type(a), type(miles), type(name), type(False), type(4 + 2j))
print(name[2], name[2:4])  # 下标2到4的字符,下班是从0开始,字符串截取也是含头不含尾

# 3.数组
list = ['gaojc', 'Ronaldo', 12, 34]
wlist = ['shanghai', 'beijing']

print(list)
print(list[1:])  # 下标1到结束
print(wlist * 2)  # 打印2次

wlist[1] = 'new york'  # 设置元素的值
print(list + wlist)  # 拼接

list[1:] = []  # 对应元素设为空
print(list)

# 4.字符串
word = "I like python"
print('字符串named word is', word)
word = word + ',it\'s userful'  # 拼接，加转义字符
print('字符串拼接和转义后=', word)
word = word + ",i say:\" i am study it\""  # 双引号中加转义字符
print(word)

print('字符串123=', str(123))  # 把123变成字符串
print('换行符=', '\n', 'next line')

# 单引号或3个引号里面的字符保留原始输入状态，里面的回车白自动转义成\n
originWord = """we can do better to win the battle,
our country need us,the same to our people 
"""
print("原始字符串originWord=", originWord)

# del originWord
print(originWord)  # 删除了，报错

print("kop" * 3)  # kop连接3次 打印
print(4 * '2')  # >>>'2222'
