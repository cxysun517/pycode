#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# input()接受的输入必须是表达式
# python表达式是值，变量和操作符(或叫运算符)的组合。
# 单独的一个值是一个表达式，单独的变量也是一个表达式。
pwd = input("请输入密码：")
print("你刚刚输入的密码是：%s" % pwd)
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
print("姓名：%s\nQQ：%s\n手机号：%s\n公司地址：%s" % (name, QQ, iphone_number, company_address))
print(20 * '-')
if name == 'cxy' and iphone_number == '110':
    print("2022年运气爆棚")

# print默认换行
for i in range(3):
    print(i)
# print不换行
for i in range(3):
    print(i, end=' ')

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
Password = input("请输入密码")
if Username == name and Password == pwd:
    print("欢迎进入xxx的世界")
else:
    print("用户名或密码错误")


