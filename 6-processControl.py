# 流程控制
# 1. 布尔类型
bool = True
print("my Boolean type variable bool=", bool)

print("2==3:", 2 == 3)
print("\"gao==gao\":", "gao" == "gao")
print("(1+3)>4:", (1 + 3) > 4)
print("(1+3)==4:", (1 + 3) == 4)
print("2!=4:", 2 != 4)
print("2!=2:", 2 != 2)
print("2>=1:", 2 >= 1)
print("2>=2.0:", 2 >= 2.0)
print("2.3>=2.30:", 2.3 >= 2.30)
print("1==1.0", 1 == 1.0)  # 1 == 1.0 是True
print("'a<b':", 'a' < 'b')  # 字母也有顺序
print("\"CHINA!=USA:\"", "CHINA" != "USA")

# 2 if 、else、 elif 判断
# 空白区或制表符在行开头表示缩进
if 1 < 2:  # if表达式用冒号结束
    print("1<2")

# 下面是嵌套if判断
num = 5
if (num > 3):
    print(">3")
    if (num < 10):
        print("<10")
# 加上else
if (1 + 1 == 2):
    if (2 * 2 == 5):
        print("if")
    else:
        print("else")

a = 7
if (a == 3):
    print("a is 3")
else:
    if a == 5:
        print("a is 5")
    else:
        if a == 7:
            print('a is 7')
        else:
            print('a is unknown')
# 加elif (elif是else if的缩写，用于多重判断)
b = 'b'
if (b == 1):
    print('b is 1')
elif b == 2:
    print('b is 2')
elif b == 'b':
    print('b is b')
else:
    print('b is unknown')

# 3.逻辑运算符
# python的布尔逻辑运算符是 and or 和not,对应其他语言的 && || 和 !
print(1 == 1 and 1 == 3)
print(1 == 1 or 1 == 3)
print((1 != 3) == (not 1 == 3))

if (not True):
    print(1)
elif not (2 * 3 == 5):
    print("2")
else:
    print(3)

# 运算符优先级：
# ==运算符高于or运算符
# python运算顺序和数学顺序一致:首先是括号,然后是指数,然后乘除,最后加减
print(1 == 1 or False)
print(True == (False or True))
print(1 + 2 * (2 - 4) ** 2)
print(2 << 3)

j = 4
k = 2
if not 1 + 1 == k or j == 4 and k - 1 < j:
    print("Yes")
else:
    print('No')

# 4.while循环
i = 0
while i < 7:
    i += 1
    if (i == 2):
        print("skip 2")
        continue  # continue
    if i > 5:
        print("break")
        break  # break
    print("i=", i)

# 5.for循环
cityStr = ''
citys = ['London', 'Paris', 'Hefei']
for name in citys:
    cityStr += name + ','
print('cityStr=', cityStr[0:len(cityStr) - 1])

# 从1加到100
sum = 0
for x in range(101):
    sum += x
print('sum=', sum)

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# birth = input('birth: ')
birth = 1988
birth = int(birth)  # input()得到的是str类型，要类型转换的，才能和2000比较

if birth < 2000:
    print('00前')
else:
    print('00后')

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 5
while n > 0:
    sum = sum + n
    n = n - 2
print('n=' + str(n), 'sum=' + str(sum))
