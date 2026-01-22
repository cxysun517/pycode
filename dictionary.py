#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 字典：可变（指可改变"键"对应的"值"；可新增键值对）无序的python序列，键值对。
# "键"是任意不可变数据，比如整数、浮点数、字符串、元组。
# 列表、字典、集合这些可变对象，不能作为"键"。
# "键"不可重复。
# "值"可以是任意数据，可重复。

# {}创建字典
a = {'name': 'cxy', 'age': 18, 'job': 'player'}
print(a['age'])
# dict()函数创建字典
d1 = dict()  # 创建空字典
print(d1)  # {}

d2 = dict(及时雨='宋江', 玉麒麟='卢俊义')
# 新增键值对
d2['花和尚'] = '鲁智深'
print(d2)  # {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深'}
# 修改值
d2['花和尚'] = '鲁花花'

# 字典的遍历操作
# 遍历字典的键
for key in d2.keys():
    print(key)

# 遍历字典的值
for key in d2:
    print(d2[key])
for values in d2.values():
    print(values)

# 遍历字典的键值对
for k, v in d2.items():
    print("key=%s,values=%s" % (k, v))

# 统计字符串中每个字符出现的次数
message = 'The quick brown fox jumps over the lazy dog'
resoult = {}
for i in message:
    resoult[i]=message.count(i)
for k, v in resoult.items():
    print("字符'%s'出现了%s次" % (k, v))

# 遍历字典的元素
for item in d2.items():
    print(item)
# ('及时雨', '宋江')
# ('玉麒麟', '卢俊义')
# ('花和尚', '鲁花花')

# 元组的方法
# del 根据键删某个元素（键值对）
del d2['花和尚']
print(d2)
# clear() 删除所有元素
d2.clear()

# keys()/values() 返回键/值为元素组成的列表
print(a.keys())
print(a.values())

# items() 返回键值对元组为元素组成的列表
print(a.items())
# dict_items([('name', 'cxy'), ('age', 18), ('job', 'player')])

# get() 若字典d中有k键，则返回对应的值d[k]，否则返回v，v可自定义
# 语法：d.get(k,v=None)
print(a.get('age'))  # 18
print(a.get('f', '性别未知'))

# pop() 若字典d中有k键，则返回对应的值d[k]并且删除该键值对，否则返回v，v可自定义
# 语法：d.pop(k,v=None)
print(a.pop('age'))  # 18
print(a.pop('age', '年纪未知'))
print(a)  # {'name': 'cxy', 'job': 'player'}
