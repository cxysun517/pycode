#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 字符串：不可变有序的python序列
name = "abcdefghi"
# 不包含下标为6的字符，步长2  bdf
print(name[1:6:2])
# 下标为2到最后的字符  cdefghi
print(name[2:])
# 下标为1到倒数第二个字符,不包含下标-1对应的倒数第一个元素  bcdefgh
print(name[1:-1])
# 当step为负数时，切片将其解释为从start出发以步长|step|逆序索引序列  ihgfedcba
print(name[::-1])

# 字符串操作
mystr = 'hello world itcast AND itcastcpp'
# #####################################################
# 大小写转换类capitalize、title、lower、upper、swapcase
# #####################################################
# capitalize 字符串第一个字符变为大写，其他变小写
print(mystr.capitalize())

# title 字符串中所有单词首字母大写，其他小写
print(mystr.title())

# lower/upper 将字符串中所有大写/小写字符变为小写/大写
print(mystr.upper())

# swapcase 翻转大小写
print(mystr.swapcase())

# ####################################################
# 判断类startswith/endswith、isupper/islower、istitle
# isspace、isalpha、isdigit、isalnum
# ####################################################
# startswith/endswith 判断字符串是否以某字符串开头/结尾，是则返回True，否则返回False
print(mystr.startswith('hell'))
print(mystr.startswith('wor', 6))  # 指定起始位置，True
print(mystr.startswith('AND', 19, 22))  # 指定起始及结束位置，True
print(mystr.startswith('AND', 19, 21))  # 指定起始及结束位置，False
print(mystr.endswith('cpp'))  # True
print(mystr.endswith('app'))

# isspace 判断字符串是否为空白字符串，是则返回True，否则返回False,Tab和空格也是空白字符串
print(''.isspace())  # False
print(' '.isspace())  # True

# isalpha/isdigit 判断字符串是否只有字母/十进制数字构成，注意空格不是字母/数字，只对0和正数有效
print('i love you'.isalpha())
print('good'.isalpha())
print('123 555'.isdigit())
print('123456'.isdigit())

# isalnum 判断字符串是否只有字母和十进制数字
print('abc123'.isalnum())
print('abc 123'.isalnum())

# #######################################
# 查找类find、index、count、rfind、rindex
# #######################################
# find 判断字符串里是否包含了某字符串，是则返回找到的第一个字符串的索引，否则返回-1
# rfind 判断字符串里是否包含了某字符串，是则返回找到的最后一个字符串的索引，否则返回-1
print(mystr.find('itc'))  # 12
print(mystr.rfind('itc'))  # 23
print(mystr.find('itc', 0, 13))  # -1

# index 与find()用法一样，只不过找不到时抛出异常
print(mystr.index('itc', 13))  # 23
# print(mystr.index('itc', 24))

# count 返回字符串里包含某字符串的次数
print(mystr.count('itc'))  # 2
print(mystr.count('itc', 13))  # 1
print(mystr.count('itc', 24))  # 0

# #############
# 替换类replace
# #############
# replace 把字符串里的某字符串替换掉，可指定替换几次，默认全替换掉
print(mystr.replace('itc', 'kkk', 1))
print(mystr.replace('itc', 'kkk'))

# ##############################################################################
# 截取类，Python中有三个去除头尾字符、头尾空白符的函数，中间的不删。它们依次为:
# strip：去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# lstrip：去除开头字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# rstrip：去除结尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# removeprefix：去除前缀
# removesuffix：后缀
# ##############################################################################
mystr1 = '  happy new year!'
mystr2 = 'ssssshappy new year!'
mystr3 = '#%-happy new year!%#'
mystr4 = '今天天气不错'
print(mystr1.lstrip())  # 默认删除空白符
print(mystr2.lstrip('s'))  # 指定删除开头所有字符s
print(mystr3.strip('-#%'))  # 指定删除头尾所有的-#%字符
print(mystr4.removeprefix('今天'))  # 天气不错
print(mystr4.lstrip('今天'))  # 气不错

# ###########################################
# 拆分类split、rsplit、partition、splitlines
# ###########################################
# split 指定分隔符分割字符串，可指定分割几次，默认分割到底，返回一个列表。
# partition 指定分隔符将字符串进行分割，返回一个3元的元组，第一个为分隔符左边的子串，
# 第二个为分隔符本身，第三个为分隔符右边的子串。
# splitlines 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表。
print(mystr.split(' ', 3))
print(mystr.rsplit(' ', 3))
print(mystr.split(' '))
print(mystr.partition(' '))
print('hello\nworld'.splitlines())
# ['hello', 'world', 'itcast', 'and itcastcpp']
# ['hello world', 'itcast', 'and', 'itcastcpp']
# ['hello', 'world', 'itcast', 'and', 'itcastcpp']
# ('hello', ' ', 'world itcast and itcastcpp')
# ['hello', 'world']

# #########
# 拼接类join
# #########
# join 将python序列(列表、元组、字典)中的元素以指定的字符连接生成一个新的字符串并返回
s1 = ''
s2 = '-'
str1 = ['i', 'love', 'you']
str2 = ('i', 'love', 'you')
print(s1.join(str1))  # iloveyou
print(s2.join(str2))  # i-love-you
