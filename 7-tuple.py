#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #######################################################################
# 元组（tuple）：不可变有序的python序列，元素可重复，类型可不同，"只读列表"
# #######################################################################
# ()创建元组
abc = ("Python", 19, [1, 2], ('c', 2.0), {"a": 555, "b": 666})
# 当创建的元组中只有一个字符串类型的元素时，该元素后面必须要加一个逗号,
# 否则 Python 解释器会将它视为字符串
a = ("http",)
print(type(a))
print(a)
b = 'x', 'y', 'z'  # 不要括号也可以
print(b)  # ('x', 'y', 'z')

# tuple()函数创建元组
tup1 = tuple("hello")
print(tup1)  # ('h', 'e', 'l', 'l', 'o')
tup2 = tuple(['Python', 'Java', 'C++', 'JavaScript'])
print(tup2)  # ('Python', 'Java', 'C++', 'JavaScript')
dict1 = {'a': 100, 'b': 42, 'c': 9}
tup3 = tuple(dict1)
print(tup3)  # ('a', 'b', 'c')
tup4 = tuple(dict1.values())
print(tup4)  # (100, 42, 9)
# 创建空元组
tup5 = tuple()
print(tup5)  # ()

'''索引访问'''
print(tup2[-1])  # JavaScript
'''切片访问'''
print(tup2[1::2])  # 步长为2，('Java', 'JavaScript')
print(tup2[-3:-1])  # ('Java', 'C++')

'''元组的方法'''
# index、count用法同列表
# del删除整个元组（元组是不可变的，不能删除它的元素）
# Python自带垃圾回收功能，会自动销毁不用元组，一般不需要del手动删除。

# 使用+可以拼接元组，并返回新元组
tup1 = (100, 0.5)
tup2 = (3 + 12j, 99)
print(tup1 + tup2)  # (100, 0.5, (3+12j), 99)
# 使用*整数n可以扩展元组，并返回新元组
print(tup1 * 2)  # (100, 0.5, 100, 0.5)

# 元组是不可变序列，元组中的元素不能被修改
# 但当元组中元素是列表，字典时，元组中的列表的元素及字典的值是可修改的
abc[2][1] = 222
abc[4]['b'] = 888
print(abc)  # ('Python', 19, [1, 222], ('c', 2.0), {'a': 555, 'b': 888})
