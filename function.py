#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 4种参数及定义顺序从先到后：位置参数-默认参数-可变参数-关键字参数
# 位置参数，按顺序依次赋值
def test(a, b):
    print("%d+%d=%d" % (a, b, a + b))


test(1, 100)


# 函数嵌套
def test1(a1, b1):
    return a1 + b1


def average(i, j):
    sum1 = test1(i, j)
    return sum1 / 2.0


res = average(33, 63)
print(res)


# 函数返回多值，组成元组
def information(name, age):
    # print("name:%s age:%d" % (name, age))
    return name, age


# information("cxy", 18)
print(information('cxy', 18))  # ('cxy', 18)


# 默认参数必须指向不变对象，必须定义在位置参数的后面
def students(name, sex, age=18):
    return name, age, sex


print(students('ym', 'male'))  # ('ym', 18, 'male')
print(students('lh', age=22, sex='female'))  # ('lh', 22, 'female')


# 可变参数，形参会自动组装成一个元组，传入实参的数量可以变化
# 用位置参数，只能传入list或tuple
def cal(numbers):
    sum1 = 0
    for i in numbers:
        sum1 += i
    return sum1


print(cal((1, 2, 3)))  # 传入tuple
print(cal([1, 2, 3]))  # 传入list


# 用可变参数，可以传入任意数量个参数，包括0个
def cal(*numbers):
    sum1 = 0
    for i in numbers:
        sum1 += i
    return sum1


print(cal())  # 甚至可以传入0个参数
print(cal(1, 2))  # numbers接收到的是一个tuple
# 已有一个list或tuple了，怎么把它传入函数中，使用*
num = [1, 3, 5, 6, 7, 8]
print(cal(*num))  # 这儿*是序列解包


# 关键字参数，形参会自动组装成一个dict，实参在传递时是键值对的方式
def persion(name, age, **kw):
    print('name:', name, 'age:', age, kw)


persion('cxy', '18', city='hz')
# 已有一个dict了，怎么把它传入函数中，使用**
d = {'city': 'sh', 'job': 'teacher'}
persion('dyl', '30', **d)
# name: dyl age: 30 {'city': 'sh', 'job': 'teacher'}

# ################################################################
# Python中一切内容都可以称为对象:
# 不可变对象（数值类型int/float、字符串、元组tuple）
# 可变对象（列表list、字典dict、集合set）
# ################################################################
# Python中函数参数传递遵循极具Python土味的 Call-by-Object（传递对象）
# Python的变量充其量就是对象的一个引用
# 函数的参数传递本质上就是：从实参到形参的赋值操作
# 变量赋值操作其实是把一个名字绑定到对象上，变量就是一个标签，一个名字
# ################################################################

# 传递不可变对象
a = 5  # 给对象5一个名字叫a，a绑定到对象5上，是对象5的一个引用


def test(p):
    p = p + 10  # 执行时，p这个名字又从对象5上给撕了下来，并贴给了p+10这个对象
    print(p)  # 15


test(a)  # 传递的是对象5，再确切点是对象5的地址指向，对象5多了一个名字p
print(a)  # 5 对象5只剩下a这个名字了

# 传递可变对象
a = [1, 2]


def f1(m):
    print('m', id(m))  # a和m是同一个对象
    m.append(3)  # 由于m是可变对象，不创建对象拷贝，直接修改这个对象


f1(a)
print('a', id(a))
print(a)  # [1, 2, 3]


# 递归函数：函数内部调用自己
def calNum(num):
    if num > 1:
        result = num * calNum(num - 1)
    else:
        result = 1
    return result


print(calNum(3))

# 匿名函数：lambda关键字定义
func1 = lambda a, b: a + b
print(func1(3, 4))  # 7
func2 = lambda x, y: x if x > y else y
print(func2(3, 100))
stus = [
    {"name": "zh", "age": 18},
    {"name": "li", "age": 19},
    {"name": "wu", "age": 17}
]
# 做内置函数的参数
stus.sort(key=lambda x: x['age'])
print(stus)
