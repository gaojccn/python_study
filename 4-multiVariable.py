# 复合数据类型---集合等

# 1.元组
tup1 = ('a', 2)
print(tup1[0])
# tup1[1]=1  #TypeError: 'tuple' object does not support item assignment

# 2.集合
country = {'china', 'USA', 'Russia', 'France'}
print(country)

if ('Germany' in country):
    print('Germany 在 country集合里')
else:
    print('Germany 不在country集合里')

setA = set('abcdbdcfc')
setB = set('docker')

print(setA - setB)  # 差集
print(setA | setB)  # 并集
print(setA & setB)  # 交集
print(setA ^ setB)  # 不同时存在的集

dict = {}
dict[1] = 'one'
dict[2] = 'two'
print('dict=', dict)

# dict 键值对 相当于map
myDict = {'name': 'gaojc', 'id': 8171, 'height': '170cm'}

print('myDict.keys()=', myDict.keys())
print('myDict.values()=', myDict.values())
print('myDict=', myDict)
print('myDict.get(\'id\')=', myDict.get('id'))
# x 这个key不存在，返回 自定义的newStr
print("myDict.get('x','newStr')=", myDict.get('x', 'newStr'))
# 删除一个key 用pop(key)
myDict.pop('height')
print('myDict=', myDict)

# set 存储key的集合，没有value,key不能重复
# class set([iterable])
mySet = set([1, 2, 3])
print('mySet=', mySet)
mySet = set(range(10))
print('mySet 2=', mySet)
mySet = set({'w', 3, 'd'})
print('mySet 3=', mySet)
# issubset(other) Test whether every element in the set is in other.
print('issubset=', set([3]).issubset(mySet))
# use add(key) method to add element to set
mySet.add('z')
print('mySet4=', mySet)
mySet.remove('d')  # remove(key) 删除一个元素
print('mySet5=', mySet)

print(type(mySet))

# 2.list 列表
nums = [1, 2, 'a', ['doc', [9, 8, ]], ]  # 4个元素,逗号可以放最后
print('a list named nums=', nums)
print('nums[3][1][1]=', nums[3][1][1])
print('nums[-0]=', nums[-0])
print('nums[-2]=', nums[-2])  # 倒数下标往前

nums[1] = nums[2]

print('nums=', nums)
nums = nums + [3]  # 追加一个元素到list后
print(nums)

print(nums[3] * 2)  # 重复打印2次
print('a' in nums)  # 判断元素是否在列表 用 in
print("ch" in 'china')
print('U' not in 'CPU')  # not in
print(not 1 in nums)
print(not 2 in nums[3][1])

# len()函数获取列表长度
print('nums\'s lenth=', len(nums))

# insert()指定插入位置
nums.insert(2, "book")
print(nums)

# index() 返回元素首次出现的下标 ，类似于java的indexOf()
print(nums.index("a"))
print(nums.count('a'))  # 返回a 在nums里的出现次数
print(nums.remove('a'))  # 移除列表中找到的第一次的此元素
print(nums)
# 数组顺序反转
nums.reverse()
print(nums)
# 移除列表的最后一个元素,返回该元素
print("nums.pop()=", nums.pop())

word = ['chin']
word.append('ese')  # 在列表尾部追加用append
print(word)

word = word[0] + word[1]
print(word)

# range(n) range函数创建从0-n的有序序列
rang = list(range(5))
print(rang)
# range(x,y) range函数创建从x到y-1的有序序列
rang = list(range(2, 6))
print(rang)
