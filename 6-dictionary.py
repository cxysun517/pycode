#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

# #########################################################
# 字典{}：可变（指可改变"键"对应的"值"；可新增键值对）无序。
# "键"是任意不可变数据，比如整数、浮点数、字符串、元组。
# 列表、字典、集合这些可变对象，不能作为"键"。
# "键"不可重复。
# "值"可以是任意数据，可重复。
# #########################################################
'''创建字典'''
# {}创建
a = {'name': 'cxy', 'age': 18, 'job': 'player'}
print(a['age'])
# dict()函数创建
d1 = dict()  # 创建空字典
print(d1)  # {}

d2 = dict(及时雨='宋江', 玉麒麟='卢俊义')
# 新增键值对
d2['花和尚'] = '鲁智深'
print(d2)  # {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深'}
# 修改值
d2['花和尚'] = '鲁花花'

'''字典的遍历操作'''
# 遍历字典的键
for key in d2.keys():
    print(key)

# 遍历字典的值
for key in d2:
    print(d2[key])
for values in d2.values():
    print(values)
# 宋江
# 卢俊义
# 鲁花花

# 遍历字典的键值对
for k, v in d2.items():
    print(f"key={k},values={v}")
# key=及时雨,values=宋江
# key=玉麒麟,values=卢俊义
# key=花和尚,values=鲁花花

# 遍历字典的元素
for item in d2.items():
    print(item)
# ('及时雨', '宋江')
# ('玉麒麟', '卢俊义')
# ('花和尚', '鲁花花')

'''keys()/values() 返回键/值为元素组成的列表'''
print(a.keys())  # dict_keys(['name', 'age', 'job'])
print(a.values())  # dict_values(['cxy', 18, 'player'])

'''items() 返回键值对元组为元素组成的列表'''
print(a.items())
# dict_items([('name', 'cxy'), ('age', 18), ('job', 'player')])

'''统计字符串中每个字符出现的次数'''
message = 'The quick brown fox jumps over the lazy dog'
res = {}
for i in message:
    if i != ' ':  # 若字符不是空格
        res[i] = message.count(i)
for k, v in res.items():
    print(f"字符{k}出现了{v}次")

'''del 根据键删某个元素（键值对）'''
del d2['花和尚']
print(d2)  # {'及时雨': '宋江', '玉麒麟': '卢俊义'}
# clear() 删除所有元素
d2.clear()
print(d2)  # {}

'''get() 若字典d中有k键，则返回对应的值d[k]，否则返回v，v可自定义'''
# 语法：d.get(k,v=None)
print(a.get('age'))  # 18
print(a.get('f', '性别未知'))  # 性别未知

'''pop() 若字典d中有k键，则返回对应的值d[k]并且删除该键值对，否则返回v，v可自定义'''
# 语法：d.pop(k,v=None)
print(a.pop('age'))  # 18
print(a.pop('age', '年纪未知'))  # 年纪未知
print(a)  # {'name': 'cxy', 'job': 'player'}

'''update() 更新字典中的键/值对，可以修改原字典中存在的键对应的值，也可以添加新的键/值对到原字典中'''
d3 = {'one': 1, 'two': 2}
d3.update({'three': 3, 'four': 4})  # 传一个字典
d3.update(five=5)  # 传关键字
d3.update([('six', 6), ('seven', 7)])  # 传一个包含一个或多个元祖的列表
d3.update(zip(['eight', 'nine'], [8, 9]))  # 传一个zip()函数
d3.update(one=111, two=222)  # 使用以上任意方法修改存在的键对应的值
print(d3)
# {'one': 111, 'two': 222, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

'''JSON字符串和字典互转'''
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 将字典转换为JSON字符串
json_string = json.dumps(person)
print(json_string)  # {"name": "Alice", "age": 30, "city": "New York"}

# 将JSON字符串转换为字典
person_dict = json.loads(json_string)
print(person_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
