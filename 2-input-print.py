#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# input()函数用于从标准输入（通常是键盘）读取一个字符串
pwd = input("请输入密码：")
print("你刚刚输入的密码是:", pwd)
# print("你刚刚输入的密码是：%s" % pwd)

# input()输入的是str类型，要想实现逻辑运算必须转化为int类型
# age = input("请输入年龄：")
age = int(input("请输入年龄："))
if age >= 18:
    print("哥已成年，网吧可以去了")
else:
    print("未成年人禁止入内")

name = input("请输入姓名：")
QQ = input("请输入QQ：")
iphone_number = input("请输入电话号码：")
company_address = input("请输入公司地址：")
print(20 * '-')

"""%s方法"""
# print("姓名：%s\nQQ：%s\n手机号：%s\n公司地址：%s" % (name, QQ, iphone_number, company_address))

"""format是python2.6新增的格式化字符串方法"""
# 不需理会数据类型，而%方法只能替代指定类型，如%s只能替代字符串类型
# 通过{}占位，顺序填充
# print("姓名：{}\nQQ：{}\n手机号：{}\n公司地址: {}".format(name, QQ, iphone_number, company_address))

'''f-string是Python3.6新增的'''
print(f"姓名：{name}\nQQ：{QQ}\n手机号：{iphone_number}\n公司地址：{company_address}")
print(20 * '-')
if name == 'cxy' and iphone_number == '555':
    print("2024年运气爆棚")

# print不换行
for i in range(3):
    print(i, end=' ')  # 0 1 2
print("\n")
for i in range(3):
    print(i, end='')  # 012
print("\n")
# print默认换行，默认参数end = '\n'
for i in range(3):
    print(i)

seat = int(input("请输入剩余座位数："))
balance = int(input("请输入余额："))
if seat > 0:
    print("请上车刷卡")
    if balance >= 2:
        print("请找个空座坐下")
    else:
        print("余额不足，请下车")
else:
    print("没有空余座位了，请等待下一辆车")

name = "cxy"
pwd = "123"
Username = input("请输入用户名:")
Password = input("请输入密码:")
if Username == name and Password == pwd:
    print("欢迎进入xxx的世界")
else:
    print("用户名或密码错误")

"""强大的format函数"""
# 通过位置
name = 'cxy'
age = 18
print('I am {1}, {0} years old'.format(age, name))  # I am cxy, 18 years old
print('I\'m {1}, I\'m {0} {1}'.format('lucky', name))  # I'm cxy, I'm lucky cxy

# 通过关键字参数
print('{name} is {age} years old!'.format(age=30, name='lxb'))  # lxb is 30 years old!


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def information(self):
        # format()必须传入实参
        return 'This guy is {self.name}, {self.age} years old'.format(self=self)


p = Person('cxy', 18)
print(p.information())  # This guy is cxy, 18 years old

# 通过映射list
a_list = ['cxy', 20, 'china']
print('my name is {0[0]}, from {0[2]}, age is {0[1]}'.format(a_list))

# 通过映射dict
b_dict = {'name': 'cxy', 'age': 20, 'province': 'shanxi'}
print('my name is {name}, age is {age}, from {province}'.format(**b_dict))

# 填充与对齐
# :> 右对齐
# :<左对齐
# :^居中对齐
# My name is   cxy, from China  , i am  18  years old.
print("My name is {:>5}, from {:<7}, i am{:^6}years old.".format("cxy", "China", 18))
# :号后面可带唯一一个填充字符，不指定默认空格填充
# My name is &&cxy, from China**, i am￥￥18￥￥years old.
print("My name is {:&>5}, from {:*<7}, i am{:￥^6}years old.".format("cxy", "China", 18))

# 精度与类型f
# .2表示长度为2的精度，f表示float类型
print("{:.2f}".format(3.1415926))  # 3.14

"""解决中英文混输格式对齐的问题"""
# 中国大学排名定向爬虫
