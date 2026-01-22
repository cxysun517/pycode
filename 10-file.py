#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import csv
import pandas as pd

# ###########################################################
# r 从文件读取
# w 写入文件，若文件存在，会清空其原有内容；反之，则创建新文件
# a 表示追加写入
# b 以二进制方式操作文件
# + 可读可写文件
# ###########################################################
# 总结：
# 只用于读取用r，只用于清空写用w，只用于追加写用a
# 既读又写要用+，清空读写用w+，追加读写用a+，从头覆盖写用r+
# ###########################################################
'''
读函数：read()、readline()、readlines()
总结：read、readline函数均返回字符串对象，readlines返回list
'''
'''
例：a.txt文件内容如下
first line: Hello world
second line: I love china
'''
f = open('a.txt')  # 默认只读方式打开已创建好的文件
print(f.read(3))  # fir, size参数指定一次最多可读取的字符数
f.seek(0, 0)  # 文件指针回到开头

print(f.read())  # 全部读取
# first line: hello world
# second line: i love china
f.seek(0, 0)

print(f.readline(7))  # first l, 指定读取文件中一行前size个字符
f.seek(0, 0)

print(f.readline())  # 读取文件中完整一行内容，包含最后的换行符"\n"
f.seek(0, 0)
# first line: hello world
#

# 指定读取文件中所有行内容，返回一个字符串列表，每个元素为文件中的一行内容
line_list = f.readlines()
print(line_list)  # ['first line: hello world\n', 'second line: i love china']
for i in line_list:
    print(i)
    # first line: hello world
    #
    # second line: i love china
f.seek(0, 0)

# 如果已读入的字符数大于size，则停止读入下一行['first line: hello world\n']
print(f.readlines(20))
f.seek(0, 0)

f.close()  # 使用open()函数打开的文件对象，操作完必须手动进行关闭

'''
写函数：write()、writelines()
'''
f = open('b.txt', 'w+')  # 打开文件用于读写，若文件已存在，先清空
f.write('cxy\ngood luck')
f.close()

# 应用：复制文件内容到另一个文件中
fb = open('b.txt')
fc = open('c.txt', 'w+')
# writelines()函数向文件中写入多行数据时，不会自动给各行添加换行符
fc.writelines(fb.readlines())
fb.close()
fc.close()

'''
csv文件的读写操作
csv文件以纯文本形式存储表格数据（数字和文本）,以标准英文逗号分隔
'''
'''
# 读csv文件：csv.reader()，以行为单位
# 接收一个可迭代的对象（比如csv文件），返回一个迭代器，再结合遍历
'''
with open("test.csv", "r", encoding="utf-8") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        # print(row)  # 打印所有
        # ['No.', 'Name', 'Age', 'Score']
        # ['1', 'cxy', '18', '99']
        # ['2', 'dyl', '22', '100']
        # ['3', 'chn', '26', '95']
        print(row[1])  # 只打印某一列，如名字一列
        # Name
        # cxy
        # dyl
        # chn
f.close()

# 上述方法不能根据标题打印需要的列，使用DictReader来实现
# 返回的每一个单元格都存放在一个字典的值内，而这个字典的键则是这个单元格的标题
with open("test.csv", "r", encoding="utf-8") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # print(row)  # 打印所有
        # {'No.': '1', 'Name': 'cxy', 'Age': '18', 'Score': '99'}
        # {'No.': '2', 'Name': 'dyl', 'Age': '22', 'Score': '100'}
        # {'No.': '3', 'Name': 'chn', 'Age': '26', 'Score': '95'}
        print(row['Name'])  # 指定标题打印某一列，如名字一列
        # cxy
        # dyl
        # chn
f.close()

'''
写csv文件：csv.writer()，返回一个对象，借助其方法writerow()一次写入一行
或writerows()一次性写入多行。但每写入一行，便多一个空行。
解决办法2个：
1、在open方法中加入参数值 newline=""
2、在csv.writer方法中加入参数值 lineterminator='\n'
'''
ro = [['4', 'hjf', '23', '88'], ['5', 'lyt', '21', '100'], ['6', 'syl', '19', '91']]
with open("test.csv", "a+", encoding="utf-8", newline="") as f:
    fro = csv.writer(f)
    fro.writerows(ro)
f.close()

'''
删除csv的行和列
'''
# 用pandas库中的read_csv()函数读取出csv文件中的数据
# 参数一：要读取的csv文件的路径 参数二： sep指定字段之间的分隔符
df = pd.read_csv('test.csv', sep=',')  # df将被赋值为一个DataFrame对象，包含来自csv文件的数据

# 删除csv文件(有标题)的第4到6行，注意index[3:6]是左开右闭
# df.drop默认不会就地修改原始数据，但会传回新的DataFrame
df = df.drop(df.index[3:6])

# 或者设置参数inplace=True，要求就地修改数据，如下
# df.drop(df.index[3:6], inplace=True)

print(df)
#    No. Name  Age  Score
# 0    1  cxy   18     99
# 1    2  dyl   22    100
# 2    3  chn   26     95

'''保存到新的csv文件，参数index=False，表示输出不显示index(索引)值'''
df.to_csv("new_test.csv", index=False, encoding="utf-8")

'''应用：复制csv文件内容到另一个文件中'''
f_n = open('new_test.csv')
f_o = open('test.csv', 'w+')  # 清空写
# writelines()函数向文件中写入多行数据时，不会自动给各行添加换行符
f_o.writelines(f_n.readlines())
f_n.close()
f_o.close()

file = 'new_test.csv'
if os.path.exists(file) and os.path.isfile(file):
    os.remove(file)
    print("file deleted")
else:
    print("file not found")

# #################################################################
# 文件指针:用于标明文件读写的起始位置
# 方法：tell()、seek()
# file.tell()——该方法返回文件内部指针当前位置，无参数。

# 文件对象读写数据时，文件指针会自动向后移动
# 读写多少个字符，就从当前位置向后移动多少个位置
#
# file.seek(offset, from)——该方法用于移动文件指针到指定位置
# from参数：0、1、2
# seek(3,0)---文件指针向后移动至距文件开头3个字符处
# seek(5,1)---文件指针向后移动至距当前位置5个字符处
# seek(-3,2)---文件指针向前移动至距文件结尾3个字符处
# 当未使用二进制格式打开文件时，若从当前位置或文件尾移动指针会报错
# #################################################################
f = open('a.txt', 'rb')  # 二进制读取
# first line: hello world
#
# second line: i love china
print(f.read(1))  # b'f'
print(f.tell())  # 1：读1个字符，指针从文件开头向后移动1个位置，指向i
print(f.read(2))  # b'ir'
print(f.tell())  # 3： 读2个字符，指针从指向i向后移动2个位置，指向s
f.seek(8, 0)  # 文件指针向后移动至距文件开头8个字符处，指向n
print(f.tell())  # 8
print(f.read(1))  # b'n'
f.seek(-3, 2)  # 文件指针向前移动至距文件结尾3个字符处，指向i(结尾是换行符)
print(f.tell())  # 47
print(f.read(1))  # b'i'

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

'''open()函数创建或打开指定文件'''
# 若要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可，否则，需要指定完整路径
f = open('5-String.py', 'r', encoding='UTF-8')  # f是文件对象
# readlines()返回一个字符串列表，其中每个元素为文件中的一行内容
line_lists = f.readlines()
for i in line_lists:
    if i.startswith('#'):  # 检查字符串是否是以指定的子字符串开头
        continue  # 结束本次循环，执行下一次循环
    else:
        print(i.replace('\n', ''))  # 删除换行"\n"，用空值置换
f.close()
