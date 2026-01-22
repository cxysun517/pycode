#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv

# ########################################################
# r 从文件读取
# w 写入文件，若文件存在，会清空其原有内容；反之，则创建新文件。
# a 表示追加写入
# b 以二进制方式操作文件
# + 可读可写文件
# ########################################################
# 总结：
# 只用于读取用r，只用于清空写用w，只用于追加写用a
# 既读又写要用+：清空读写用w+，追加读写用a+，从头覆盖写用r+
# ########################################################

# 读函数：read()、readline()、readlines()
# 总结：read、readline函数均返回字符串对象，readlines返回list

f = open('a.txt')  # 默认只读方式打开已创建好的文件
# print(f.read(3))  # size指定一次最多可读取的字符数
# print(f.read())  # 全部读取

# print(f.readline(7))  # 指定读取文件中一行前size个字符
# print(f.readline())  # 读取文件中完整一行内容，包含最后的换行符“\n”

# print(f.readlines(20))
# 如果已读入的字符数大于size，则停止读入下一行
linelist = f.readlines()
# 指定读取文件中所有行内容，返回一个字符串列表，每个元素为文件中的一行内容
for i in linelist:
    print(i)
f.close()  # 使用open()函数打开的文件对象，操作完必须手动进行关闭

# 写函数：write()、writelines()
f2 = open('b.txt', 'w+')  # 打开文件用于读写，若文件已存在，先清空
f2.write('cxy\ngood luck')
f2.close()

# 应用：复制文件内容到另一个文件中
f3 = open('b.txt')
f4 = open('c.txt', 'w+')
f4.writelines(f3.readlines())
f3.close()
f4.close()
# writelines()函数向文件中写入多行数据时，不会自动给各行添加换行符

# csv文件的读写操作
# csv文件以纯文本形式存储表格数据（数字和文本）,以标准英文逗号分隔

# 读csv文件：csv.reader()，以行为单位
# 接收一个可迭代的对象（比如csv文件），返回一个生成器，再结合遍历

with open("test.csv", "r", encoding="utf-8") as f:
    fcsv = csv.reader(f)
    for row in fcsv:
        # print(row)  # 打印所有
        print(row[1])  # 只打印某一列，如名字一列
# ['No.', 'Name', 'Age', 'Score']
# ['1', 'cxy', '18', '99']
# ['2', 'dyl', '22', '100']
# ['3', 'chn', '26', '95']

# Name
# cxy
# dyl
# chn

# 上述方法不能根据标题打印需要的列，使用DictReader实现
# 返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题
with open("test.csv", "r", encoding="utf-8") as f:
    fcsv = csv.DictReader(f)
    for row in fcsv:
        # print(row)  # 打印所有
        print(row['Name'])  # 只打印某一列，如名字一列

# {'No.': '1', 'Name': 'cxy', 'Age': '18', 'Score': '99'}
# {'No.': '2', 'Name': 'dyl', 'Age': '22', 'Score': '100'}
# {'No.': '3', 'Name': 'chn', 'Age': '26', 'Score': '95'}

# cxy
# dyl
# chn

# 写csv文件：csv.writer()，返回一个对象
# 借助其方法writerow()一次写入一行或writerows()一次性写入多行

ro = ['4', 'hjf', '23', '81']
f5 = open("test.csv", "a")
fro = csv.writer(f5)
fro.writerow(ro)

# 文件指针:用于标明文件读写的起始位置
# 方法：tell()、seek()
# file.tell()——该方法返回文件内部指针当前位置，无参数。

# 文件对象读写数据时，文件指针会自动向后移动
# 读写多少个字符，就从当前位置向后移动多少个位置
#
# file.seek(offset, from)——该方法用于移动文件指针到指定位置
# from：0、1、2
# seek(3,0)---文件指针向后移动至距文件开头3个字符处
# seek(5,1)---文件指针向后移动至距当前位置5个字符处
# seek(-3,2)---文件指针向前移动至距文件结尾3个字符处
# 当未使用二进制格式打开文件时，若从当前位置或文件尾移动指针会报错
f6 = open('a.txt', 'rb')
# first line: hello world
#
# second line: i love china
print(f6.read(1))  # b'f'
print(f6.tell())  # 1：读1个字符，指针从文件开头向后移动1个位置，指向i
print(f6.read(2))  # b'ir'
print(f6.tell())  # 3： 读2个字符，指针从指向i向后移动2个位置，指向s
f6.seek(8, 0)  # 文件指针向后移动至距文件开头8个字符处，指向n
print(f6.tell())  # 8
print(f6.read(1))  # b'n'
f6.seek(-3, 2)  # 文件指针向前移动至距文件结尾3个字符处，指向i(结尾是换行符)
print(f6.tell())  # 47
print(f6.read(1))  # b'i'

# ########################################
# 文件重命名及删除
# python os模块
# import os
# os.rename("旧文件名", "新文件名")
# os.remove("待删除文件名")
# ########################################
# 文件夹创建、获取当前目录、获取目录列表、删除
# os.mkdir("文件夹名称")
# os.getcwd()
# os.listdir("./")
# os.rmdir("待删除文件夹")
# ########################################
