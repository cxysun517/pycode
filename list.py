#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 列表：可变有序的python序列
# []创建列表
# 列表的遍历操作
name = ['cxy', 'zsh']
for i in name:
    print(i)

length = len(name)
i = 0
while i < length:
    print(name[i])
    i += 1

# list()函数创建列表
list1 = list("hello")
print(list1)  # ['h', 'e', 'l', 'l', 'o']
kv = {'a': 100, 'b': 42, 'c': 9}
list2 = list(kv)
print(list2)  # ['a', 'b', 'c']
list3 = list(kv.values())
print(list3)  # [100, 42, 9]
list4 = list((55, 'a'))
print(list4)
# 创建空
list5 = list()
print(list5)  # []

# 列表的方法
# ####################################
# 添加类：append、extend、insert
# ####################################
# append：在列表末尾追加整个对象，可以是字符串，列表，字典，元组，集合
d = [25, 'a', {1: "p"}, (1, 'e')]
kv = {2: "a", 3: "hj"}
t = (['b', 'c'], 100, 'hi gg')
s = {5, 'w'}
name.append('cxy')
name.append(s)
print(name)
# ['cxy', 'zsh', 'cxy', {'w', 5}]

# extend：在列表末尾逐个追加对象的元素
name.extend(s)
print(name)
# ['cxy', 'zsh', 'cxy', {'w', 5}, 'w', 5]

# insert：在列表指定索引位置添加整个对象
name.insert(2, kv)
print(name)
# ['cxy', 'zsh', {2: 'a', 3: 'hj'}, 'cxy', {'w', 5}, 'w', 5]

# ####################################
# 删除类：del、pop、remove
# ####################################
# del：根据下标删某个元素，不能删除列表
del name[2]
print(name)

# pop：删除最后一个元素
name.pop()
print(name)

# remove：删除指定元素，有相同元素时，只删第一个
name.remove('cxy')
print(name)

# ######################################
# 查找判断类：in/not in、index、count
# ######################################
# in/not in：判断元素是否在可迭代对象中，可配合“if”和“while”使用
# index：找指定的元素第一次出现在对象中的索引位置，可指定查找区间，左闭右开
ls = [1, 2, 3, "a", 3, 5, "a", 5, [1, 7, "b"]]
print(ls.index("a"))  # 3
print(ls.index('a', 4, 7))  # 6

# count：统计元素出现的次数
print(ls.count('a'))

# ##############################
# 排序类：sort、sorted、reverse
# ##############################
# sort：直接对原列表（元素的数据类型相同）正向排序，无返回，可指定方法排序，可反向排序
ls1 = [1, 3, 7, 2, 4, 5, 6]
# ls1.sort()
ls1.sort(reverse=True)  # 反向排序
print(ls1)

# sorted：返回排序新列表，原列表不动
ls2 = [1, 3, 7, 2, 4, 5, 6]
ls3 = sorted(ls2)
print(ls2)  # [1, 3, 7, 2, 4, 5, 6]
print(ls3)

# reverse：反转排序
ls2.reverse()
print(ls2)  # [6, 5, 4, 2, 7, 3, 1]
