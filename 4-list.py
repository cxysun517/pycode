#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #################################################
# 列表：可变有序的python序列，元素可重复，类型可不同
# #################################################
# 列表推导式：一种用简洁的语法从一个可迭代对象（如列表、字符串、字典、元组、集合）创建新的列表的方法
# 可直接作用于for循环的数据类型有以下几种：
# 一类是list、tuple、dict、set、string
# 一类是generator，包括带yield的generator function
# 这些可直接作用于for循环的对象统称为可迭代对象：Iterable
even = [i for i in range(10) if i % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

'''列表的遍历操作'''
# for循环
name = ['cxy', 'zsh']
for i in name:
    print(i)
# 索引
for i in range(len(name)):
    print(name[i])

'''list()函数创建列表'''
list1 = list("hello")  # 字符串
print(list1)  # ['h', 'e', 'l', 'l', 'o']
kv = {'a': 100, 'b': 42, 'c': 9}  # 字典
list2 = list(kv)
print(list2)  # ['a', 'b', 'c']
list3 = list(kv.values())  # values()方法通常结合list()函数以将其返回的字典值转化为列表
print(list3)  # [100, 42, 9]
list4 = list((55, 'a'))  # 元组
print(list4)  # [55, 'a']
list5 = list({1, 3.1415, "hello", 1 + 4j})  # 集合
print(list5)  # [1, 3.1415, 'hello', (1+4j)]

'''创建空列表'''
list6 = list()
print(list6)  # []
print(f"空列表没有任何元素，长度为{len(list6)}")  # 空列表没有任何元素，长度为0
# 有一个空字符串元素的列表['']
list7 = ['']  # 包含1个空字符串元素的列表，长度为1
print(f"包含1个空字符串元素的列表，长度为{len(list7)}")
# 有一个空格元素的列表
list8 = [' ']  # 包含1个空格元素的列表，长度为1
print(f"包含1个空格元素的列表，长度为{len(list8)}")
list9 = ['   ']  # 包含多个连续空格组成的1个元素的列表，长度为1
print(f"包含多个连续空格组成的1个元素的列表，长度为{len(list9)}")
list10 = [' ', ' ', ' ']  # 包含3个空格元素的列表，长度为3
print(f"包含3个空格元素的列表，长度为{len(list10)}")

'''切片赋值替换插入删除'''
# 一次为多个元素赋值
name1 = list('Pyther')
name1[4:] = 'on'
print(name1)  # ['P', 'y', 't', 'h', 'o', 'n']
# 使用与原序列不等长的序列将切片替换
name1[1:] = list('abcdef')
print(name1)  # ['P', 'a', 'b', 'c', 'd', 'e', 'f']
# 在索引位置处插入元素
name1[1:1] = [555, 888]
print(name1)  # ['P', 555, 888, 'a', 'b', 'c', 'd', 'e', 'f']
# 删除元素
name1[1:3] = []
print(name1)  # ['P', 'a', 'b', 'c', 'd', 'e', 'f']

'''列表的方法'''
# ####################################
# 添加类：append、extend、insert
# ####################################
# append：在列表末尾追加整个对象，可以是字符串，列表，字典，元组，集合，入栈
d = [25, 'a', {1: "p"}, (1, 'e')]
kv = {2: "a", 3: "hj"}
t = (['b', 'c'], 100, 'hi gg')
s = {5, 'w'}
name.append(s)
print(name)  # ['cxy', 'zsh', {'w', 5}]

# extend：在列表末尾逐个追加对象的元素
name.extend(t)
print(name)  # ['cxy', 'zsh', {'w', 5}, ['b', 'c'], 100, 'hi gg']

# insert：在列表指定索引位置处添加整个对象
name.insert(2, kv)
print(name)  # ['cxy', 'zsh', {2: 'a', 3: 'hj'}, {'w', 5}, ['b', 'c'], 100, 'hi gg']

# ####################################
# 删除类：del、pop、remove、clear
# ####################################
# del：根据下标删某个元素，不能删除列表
del name[2]
print(name)

# pop：删除最后一个元素，出栈
name.pop()
print(name)

# remove：删除指定元素，有相同元素时，只删第一个
name.remove('cxy')
print(name)

# clear：清空列表
name.clear()
print(name)  # []

# ######################################
# 查找判断类：in/not in、index、count
# ######################################
# in/not in：判断元素是否在可迭代对象中，可配合"if"和"while"使用
# index：找指定的元素第一次出现在对象中的索引位置，可指定查找区间，左闭右开
ls = [1, 2, 3, "a", 3, 5, "a", 5, [1, 7, "b"]]
if "a" in ls:
    print(ls.index("a"))  # 3
    print(ls.index('a', 4, 7))  # 6
    # count：统计元素出现的次数
    print(ls.count('a'))  # 2

# ##############################
# 排序类：sort、sorted、reverse
# ##############################
'''sort：直接对原列表排序，无返回，可指定方法排序，可反向排序'''
ls1 = [1, 3, 7, 2, 4, 5, 6]
# reverse：反转排序
ls1.reverse()
print(ls1)  # [6, 5, 4, 2, 7, 3, 1]
# ls1.sort()
ls1.sort(reverse=True)
print(ls1)  # 反向排序[7, 6, 5, 4, 3, 2, 1]

'''sorted：返回排序新列表，原列表不动'''


# 函数原型：sorted(iterable, key=None, reverse=False)
# iteralbe表示一个可迭代对象，主要包括3类：
# 1、所有的序列类型，比如list(列表)、str(字符串)、tuple(元组)，可迭代，有序，支持下标访问
# 2、非序列类型，比如映射类型dict(字典)、文件对象file(文件)、set(集合)
# 3、自定义的任何包含__iter__()或__getitem__()方法的类的对象
# 当使用像for循环这样的迭代环境时，Python会自动调用对象的__iter__()方法并返回一个迭代器，
# 然后迭代环境会不断调用迭代器的__next__()方法来获取下一个元素。

# 示例，如何创建一个类，包含__iter__()和__getitem__()方法来使其对象具有迭代功能
class MyClass:
    def __init__(self, data):
        self.My_data = data

    # __iter__()：用于返回一个迭代器对象，该迭代器对象可用于迭代访问类的元素
    def __iter__(self):
        return iter(self.My_data)

    # __getitem__()：用于根据索引来获取类中的元素
    def __getitem__(self, index):
        return self.My_data[index]


my_obj = MyClass([1, 2, 3, 4, 555])
# 使用for循环进行迭代
for item in my_obj:
    print(item, end=' ')  # 1 2 3 4 555
# 使用索引访问元素
print(my_obj[4])  # 555

'''key指定函数，用于从可迭代对象的每个元素中提取比较键，以进行排序'''
ls2 = (1, 3, 7, 2, 4, 5, 6)
ls3 = sorted(ls2)
print(ls2)  # (1, 3, 7, 2, 4, 5, 6) # 原tuple不变
print(ls3)  # [1, 2, 3, 4, 5, 6, 7] # 返回排序了的列表
ls4 = {'c': 2, 'a': 1, 'b': 3}
print(sorted(ls4))  # ['a', 'b', 'c',] 默认按照字典的键进行排序
print(sorted(ls4.values()))  # [1, 2, 3] 指定按照键值进行排序
# 指定按照键值对进行处理，但排序依据是键值
print(sorted(ls4.items(), key=lambda x: x[1]))  # [('a', 1), ('c', 2), ('b', 3)]
# 指定按照键值对进行处理，但排序依据是键
print(sorted(ls4.items(), key=lambda x: x[0]))  # [('a', 1), ('b', 3), ('c', 2)]
# ls4.items()：返回一个包含所有字典项（键值对）的视图对象dict_items([('c', 2), ('a', 1), ('b', 3)])，每个字典项是一个元组
# lambda x: x[1]：接受一个元素（在这个场景中是一个元组），并返回这个元素的第二个组成部分（即字典的值）

'''删除列表中的空字符串元素'''
# 方法一: 使用列表推导式
my_list = ['hello', '', 'world', '', '', 'cxy', ' ', ' ', '', 'done']
new_list = [x for x in my_list if x != '']
print(new_list)  # ['hello', 'world', 'cxy', ' ', ' ', 'done']

# 方法二：使用filter()函数
# filter(function, iterable)
# 过滤可迭代对象iterable中不符合条件的元素，返回由符合条件的元素组成的新的迭代器对象
# function：函数，依次作用于每个元素，返回值为True时保留该元素，否则元素被过滤掉
# iterable：可迭代对象，如列表、range对象等
# 空字符串没有任何元素，长度为0
print(f"空字符串没有任何元素，长度为{len('')}")
# 包含1个空格元素的字符串，长度为1
print(f"包含1个空格元素的字符串，长度为{len(' ')}")
# 包含3个空格元素的字符串，长度为3
print(f"包含3个空格元素的字符串，长度为{len('   ')}")

# filter过滤掉长度为0的空字符串，再通过list将返回的迭代器对象转换为列表形式
new_list = list(filter(len, my_list))
print(new_list)  # ['hello', 'world', 'cxy', ' ', ' ', 'done']
print(my_list)  # ['hello', '', 'world', '', '', 'cxy', ' ', ' ', '', 'done']

# 方法三：join()和split()
# ' '.join(iterable).split()：用于从可迭代对象中过滤空值
# ' '.join(iterable)：将可迭代对象中的元素用空格连接起来，返回字符串
# .split()：将字符串按分隔符拆分，返回由分割后的子字符串作为元素的列表

# 将所有元素（包括空格字符' '）用空连接在一起
s = ''.join(my_list)
print(s)  # 返回字符串"helloworldcxy  done"，注意cxy与done之间还有2个空格字符元素
# split()不指定参数即默认分隔符为空格、换行符\n、制表符\t，分割次数不限
print(s.split())  # 返回列表['helloworldcxy', 'done']
# split(' ', 1)指定以空格为分隔符，只分割1次
print(s.split(' ', 1))  # 返回列表['helloworldcxy', ' done']，注意只分割1次，done前面还留有1个空格

# 将所有元素（包括空格字符' '）用空格连接在一起
s2 = ' '.join(my_list)
print(s2)  # 返回字符串"hello  world   cxy      done"
# hello和world之间2个空格字符，world和cxy之间3个空格字符，cxy和done之间6个空格字符
print(s2.split())  # 返回列表['hello', 'world', 'cxy', 'done']

# 方法四：
# list.remove()仅从列表中删除第一个匹配项
# 再配合while循环和try/except
# try/except语句检测try语句块中的错误，让except语句捕获异常信息并处理

# 删除全部空字符串
try:
    while True:
        my_list.remove('')
except ValueError:
    pass
print(my_list)  # ['hello', 'world', 'cxy', ' ', ' ', 'done']

# 可进一步删除全部空格
try:
    while True:
        my_list.remove(' ')
except ValueError:
    pass
print(my_list)  # ['hello', 'world', 'cxy', 'done']
