#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #######################################################################
# 集合（set）：可变无序的python序列，元素（不可变对象）不可重复，类型可不同
# #######################################################################
# myDict = {[1, 2, 3]: '123', 'name': 'cxy'}
# mySet = {'a', [1, 2, 3]}
# TypeError: unhashable type: 'list'
# 这个错误通常意味着你试图将一个list对象用作哈希参数，有以下两种典型的情况：
# 用作字典的键
# 用作集合set的元素
# list是可变的，是unhashable（不可哈希）的，不能作为dict的键和set的元素，tuple就可以
# 通常的解决方案是将list强制转换为tuple再使用

# {}创建集合
set1 = {"Python", 19, ('c', 2.0)}
print(set1)  # {19, 'Python', ('c', 2.0)}
# set()函数创建集合
'''创建一个空集合必须用set()而不是{}，{}是用来创建一个空字典'''
num = [1, 2, 3]  # list
print(set(num))  # {1, 2, 3}
fruit = ('apple', 'banana', 'cherry')  # tuple
print(set(fruit))  # {'cherry', 'banana', 'apple'}
student = {'小红': 23, '小米': 18, '小青': 19}  # dict
print(set(student))  # {'小青', '小红', '小米'}

'''set的方法'''
# ####################################
# 添加/复制类：add、update/copy
# ####################################
# add()：若添加元素在集合中已存在，则不执行操作
f = set(fruit)
f.add("orange")
print(f)
# update()：添加元素或集合到当前集合中，重复元素只保留1个
x = {"apple", "banana", "cherry"}
y = {"pear", "peach", "apple"}
x.update(y)
print(x)  # {'cherry', 'peach', 'pear', 'banana', 'apple'}
# copy()：浅拷贝
a = {1, (9, 2), 3}
b = a.copy()
# {1, 3, (9, 2)} 2134964855968 {1, 3, (9, 2)} 2134964942432
print(a, id(a), b, id(b))

# ######################################
# 删除类：remove、discard、pop、clear
# ######################################
# remove()：移除集合中的指定元素，元素不存在时，发生错误
x.remove("apple")
print(x)
# discard()：移除集合中的指定元素，元素不存在时，不发生错误
x.discard("pear")
# pop()：随机移除一个元素
x.pop()
# clear()：移除集合中的所有元素
x.clear()
print(x)  # set()

# ########################################
# 判断类：isdisjoint、issubset、issuperset
# ########################################
# isdisjoint()：不相交，判断两个集合是否包含相同元素，没有返回True，否则返回False
x = {'a', 'b', 'c'}
y = {'x', 'y', 'z'}
print(x.isdisjoint(y))  # True
# issubset()：子集，判断原始集合所有元素是否都包含在指定集合中，是则返回True
x = {'a', 'b', 'c'}
y = {'x', 'y', 'z', 'a', 'b', 'c'}
print(x.issubset(y))  # True
# issuperset()：超集，判断指定集合所有元素是否都包含在原始集合中，是则返回True
x = {'a', 'b', 'c', 'x', 'y', 'z'}
y = {'a', 'b', 'c'}
print(x.issuperset(y))  # True

# ########################################################
# 集合运算类：union
# intersection、intersection_update
# difference、difference_update
# symmetric_difference、symmetric_difference_update
# ########################################################
# union()：返回多个集合的并集，原集合不变，返回新的集合
set1 = {'b', 'c', 1}
set2 = {1, 2, 3}
set3 = {'A', 1, 'c'}
set4 = {'b', 1, 'B'}
set1.union(set2, set3)
print(set1)  # {1, 'c', 'b'}
print(set1.union(set2, set3))  # {1, 2, 3, 'A', 'c', 'b'}

# intersection()：返回多个集合的交集，原集合不变，返回新的集合
print(set1.intersection(set2, set3))  # {1}

# intersection_update()：将多个集合的交集赋给原集合，原集合改变
set1.intersection_update(set2, set3)
print(set1)  # {1}

# difference()：返回两个集合的差集，原集合不变，返回新的集合
print(set2.difference(set3))  # {2, 3} 等同于print(set2 - set3)
print(set3.difference(set2))  # {'c', 'A'}

# difference_update()：将两个集合的差集赋给原集合，原集合改变
set2.difference_update(set3)
print(set2)  # {2, 3}

# symmetric_difference()：返回两个集合的对称差集，原集合不变，返回新的集合
print(set3.symmetric_difference(set4))  # {'c', 'B', 'b', 'A'} 等同于print(set3 ^ set4)
print(set3 ^ set4)
print(set3)  # {1, 'c', 'A'}

# symmetric_difference_update()：将两个集合的对称差集赋给原集合，原集合改变
set3.symmetric_difference_update(set4)
print(set3)  # {'c', 'b', 'A', 'B'}
