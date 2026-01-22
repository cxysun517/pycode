#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests  # 导入requests模块
import re  # 导入正则表达式模块

# ###############################
# 字符串：不可变有序的python序列
# ###############################
'''切片操作'''
name = "abcdefghi"
# 不包含下标为6的字符，步长2  bdf
print(name[1:6:2])
# 下标为2到最后的字符  cdefghi
print(name[2:])
# 下标为1到倒数第二个字符，不包含下标-1对应的倒数第一个元素  bcdefgh
print(name[1:-1])
# 当step为负数时，切片将其解释为从start出发以步长|step|逆序索引序列  ihgfedcba
print(name[::-1])

'''转义字符，使用单引号或双引号加\反斜杠'''
print('\'')  # 单引号中打印单引号'
print("\"")  # 双引号中打印双引号"
print('\\')  # 单引号或双引号中打印反斜杠\
print("a\nb")  # 打印换行
print("The path is:\nc:\\user\python")
# The path is:
# c:\user\python


'''字符串的方法'''
mystr = 'hello world itcast AND itcastcpp'
# #####################################################
# 大小写转换类capitalize、title、lower、upper、swapcase
# #####################################################
# capitalize 字符串第一个字符变为大写，其他变小写
print(mystr.capitalize())  # Hello world itcast and itcastcpp

# title 字符串中所有单词首字母大写，其他小写
print(mystr.title())  # Hello World Itcast And Itcastcpp

# lower/upper 将字符串中所有字符变为小写/大写
print(mystr.upper())  # HELLO WORLD ITCAST AND ITCASTCPP

# swapcase 翻转大小写
print(mystr.swapcase())  # HELLO WORLD ITCAST and ITCASTCPP

# ####################################################
# 判断类startswith/endswith、isupper/islower、istitle
# isspace、isalpha、isdigit、isalnum
# ####################################################
# startswith/endswith 判断字符串是否以某字符串开头/结尾，是则返回True，否则返回False
print(mystr.startswith('hell'))  # T
print(mystr.startswith('wor', 6))  # 指定起始位置，T
print(mystr.startswith('AND', 19, 22))  # 指定起始及结束位置，T
print(mystr.startswith('AND', 19, 21))  # 指定起始及结束位置，F
print(mystr.endswith('cpp'))  # T
print(mystr.endswith('app'))  # F

# isspace 判断字符串是否只包含空白符，是则返回True，否则返回False
# 空白符是一类特殊字符，如空格、制表符、换行符等。空字符串是一个长度为零的字符串，不包含任何字符。
# 空字符串''不是空白符，所以''.isspace()结果为False
print(f"空字符串''不是空白符，所以''.isspace()结果为{''.isspace()}")
# 空格' '是空白符，所以' '.isspace()结果为True
print(f"空格' '是空白符，所以' '.isspace()结果为{' '.isspace()}")

# isalpha/isdigit 判断字符串是否只由字母或只由十进制数字（0和正数）构成，注意空格不是字母/数字
print('i love you'.isalpha())  # F
print('good'.isalpha())  # T
print('123 555'.isdigit())  # F
print('123456'.isdigit())  # T

# isalnum 判断字符串是否只由字母（a-z，A-Z，其它语言如汉字，俄文，日文的字符）或纯数字构成
print('abc123'.isalnum())  # T
print('abc 123'.isalnum())  # F，字符串中包含了空格

# #######################################
# 查找类find、index、count、rfind、rindex
# #######################################
# find 判断字符串里是否包含了某字符串，是则返回找到的第一个字符串的索引，否则返回-1
# rfind 判断字符串里是否包含了某字符串，是则返回找到的最后一个字符串的索引，否则返回-1
print(mystr.find('itc'))  # 12
print(mystr.rfind('itc'))  # 23
print(mystr.find('itc', 0, 14))  # -1，指定范围内查找
print(mystr.find('itc', 0, 15))  # 12

# index与find()用法一样，只不过找不到时会抛出异常
print(mystr.index('itc', 12))  # 12，从指定索引处开始查找
print(mystr.index('itc', 13))  # 23，从指定索引处开始查找
# print(mystr.index('itc', 24))  # 找不到，抛出异常

# count 返回字符串里包含某字符串的次数
print(mystr.count('itc'))  # 2
print(mystr.count('itc', 13))  # 1，从指定索引处开始统计
print(mystr.count('itc', 24))  # 0

# ##############
# 替换类replace
# ##############
# replace 把字符串里的某字符串替换掉，可指定替换几次，默认全替换掉
print(mystr.replace('itc', 'kkk', 1))  # hello world kkkast AND itcastcpp
print(mystr.replace('itc', 'kkk'))  # hello world kkkast AND kkkastcpp

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
mystr3 = '#%A-happy new year-!%#--'
mystr4 = '今天天气不错'
print(mystr1.lstrip())  # 删除开头空白符，happy new year!
print(mystr2.lstrip('s'))  # 指定删除开头所有的s字符，happy new year!
print(mystr3.strip('-#%'))  # 指定删除头尾所有的-或#或%字符，A-happy new year-!
print(mystr4.removeprefix('今天'))  # 天气不错
print(mystr4.lstrip('今天'))  # 指定删除开头所有的今或天字符，气不错

# ###########################################
# 拆分类split、rsplit、partition、splitlines
# ###########################################
# split 指定分隔符分割字符串，可指定分割几次，默认分割到底，返回一个列表。
# 若不指定参数即默认分隔符为空格、换行符\n、制表符\t，分割次数不限。
# 若使用空字符串作为分隔符，会引发ValueError，因为空字符串不是空白符，不能作为有效的分隔符。

# partition 指定分隔符分割字符串，返回一个3元的元组，第一个为分隔符左边的子串，
# 第二个为分隔符本身，第三个为分隔符右边的子串。

# splitlines 按照行(回车'\r', 回车换行'\r\n', 换行'\n')分隔，返回一个包含各行作为元素的列表。
# 回车'\r'：将当前位置移到本行开头
# 换行'\n'：将当前位置移到下一行
print(mystr.split(' ', 3))  # ['hello', 'world', 'itcast', 'AND itcastcpp']
print(mystr.rsplit(' ', 3))  # ['hello world', 'itcast', 'AND', 'itcastcpp']
print(mystr.split(' '))  # ['hello', 'world', 'itcast', 'AND', 'itcastcpp']
print(mystr.partition(' '))  # ('hello', ' ', 'world itcast AND itcastcpp')
print('hello\nworld'.splitlines())  # ['hello', 'world']

print("Line1\nLine2\n\nLine4".splitlines())  # ['Line1', 'Line2', '', 'Line4']
# 原始字符串中包含了多个换行符，把文本分成了四行
# 空行也作为一个元素存在，并且在列表中表示为空字符串

# #######################
# 拼接类join、str1+str2
# #######################
# join将python序列中的元素以指定的字符连接生成一个新的字符串并返回
s1 = ''  # 空
s2 = '-'
s3 = ' '  # 空格
str1 = ['i', 'love', 'you']
str2 = ('i', 'love', 'you')
print(s1.join(str1))  # iloveyou
print(s2.join(str2))  # i-love-you
print(s3.join(str1))  # i love you

# ##########################################
# 字符串编码解码encode（编码）、decode（解码）
# ##########################################
# 计算机最开始在美国被发明使用，需要编码的字符集并不是很大，人们将所需字符集中的字符
# 一一映射到128个二进制数上（0X00~0X7F）也即基础ASCII编码。

# 中国为了将汉字及非汉字图形字符纳入字符集，采用两个字节对字符集进行编码，
# 并向下兼容ASCII编码也即GB2312编码。

# 再后来生僻字、繁体字及日韩汉字也被纳入字符集就有了GBK编码，并向下兼容GB2312编码。

# 随着计算机在全世界各个国家不断普及，不同的国家地区都会开发出自己的一套编码系统，冲突及乱码问题开始凸显。
# 为了实现跨语言、跨平台的文本转换和处理需求，ISO国际标准化组织提出了Unicode的新标准，
# 标准中包含了Unicode字符集和一套编码规范。

# Python的字符串类型就是采用Unicode标准来表示字符。

# Unicode规范旨在罗列人类语言所用到的所有字符，并赋予每个字符唯一的二进制编码，
# 彻底解决之前不同编码系统的冲突和乱码问题。

# Unicode标准描述了字符是如何用码位表示的，码位的取值范围是0到0x10FFFF的整数。
# 一个Unicode字符串是一系列码位组成的序列。
# 例如：我是崔晓阳cxy
# chr()函数接受一个整数（Unicode码位）作为参数，并返回对应的字符。
print("我是" + chr(23828) + chr(26195) + chr(0x00009633) + chr(0x63) + chr(120) + chr(0x79))

# Unicode有多种编码方式，UTF-8编码使用最广泛

# 将Unicode字符串翻译成计算机所能理解的字节码称为编码
str0 = "我爱我家"
byte0 = str0.encode('gb2312')  # 以gb2312编码对str0进行编码，获取bytes类型对象
print(byte0)  # b'\xce\xd2\xb0\xae\xce\xd2\xbc\xd2'
# 字节码转换成可被人类读懂的字符串即为解码
print(byte0.decode('gb2312'))  # 我爱我家

# #################################
# 编码解码在网络爬虫中处理乱码的应用
# #################################
# python3的.py文件默认编码方式为UTF-8
# 一些网页的源代码可能是GB2312等编码方式，直接打印爬虫获取的网页源代码的文本格式数据时，中文就会显示乱码。

url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpManager/stockid/000001.phtml"
text = requests.get(url).text  # 通过requests模块的get方式将源代码赋给text
# print(text)

# #################
# 正则表达式应用
# #################
'''
元字符           描述
^               匹配字符串开头
$               匹配字符串结尾
.               匹配除\n和\r之外的任何单个字符

*               匹配前面的子表达式任意次。zo*能匹配z，也能匹配zo以及zoo，但不能匹配o，等价于{0,}
                例：源字符串是kzkopzokzoot有3处匹配，z、zo、zoo
+               匹配前面的子表达式一次或多次。zo+能匹配zo以及zoo，但不能匹配z或o，等价于{1,}
                例：源字符串是kzkopzokzoot有2处匹配，zo、zoo
？              匹配前面的子表达式零次或一次。ab(cd)?能匹配ab或abcd，等价于{0,1}，
                例：源字符串是kakbmabbcdkaabnabccd有3处匹配，ab、ab、ab
                当?紧跟*，+，{n}，{n,}，{m,n}后时，匹配模式是非贪婪的
                例：源字符串是aabab
                a.*b将匹配最长的以a开始，以b结束的字符串，匹配整个aabab
                a.*?b将匹配最短的以a开始，以b结束的字符串，匹配结果是aab和ab
{n}             匹配n次。o{2}能匹配food中的oo，不能匹配dog中的o。^\d{3}$只能匹配3位的数字，如000
                例：源字符串是tokgooodogfoooood有3处匹配，oo、oo、oo
{n,}            至少匹配n次。o{2,}能匹配food中的oo，不能匹配dog中的o。^\d{3,}$能匹配3位及以上的数字，如0000
                例：源字符串是tokgooodogfoooood有2处匹配，ooo、ooooo
{m,n}           至少匹配m次且至多匹配n次。o{2,4}匹配dooog中的ooo。^\d{2,4}$能匹配2到4位的数字，如00，1111
                例：源字符串是tokgooodogfoooood有2处匹配，ooo、oooo

x|y             匹配x或y。z|food能匹配z或food。[z|f]ood则匹配zood或food
                例：正则为z|food，源字符串kzfotfoodzood有3处匹配，z、food、z
                    正则为[z|f]ood，源字符串kzfotfoodzood有2处匹配，food、zood
[xyz]           匹配所包含的任意一个字符
[a-z]           匹配指定范围内的任意字符

\d              匹配一个数字
\n              匹配一个换行符
\r              匹配一个回车符
\t              匹配一个制表符
\s              匹配任何不可见字符即空白符，包括空格、换行符、回车符、制表符等
\b              匹配一个边界，边界一边是单词字符，另一边是非单词字符
                单词字符：字母、数字或下划线，等价于[a-zA-Z0-9_]
\w              匹配字母或数字或下划线或汉字等，类似但不等价于[A-Za-z0-9_]

字符转义
\.              匹配.
\*              匹配*
\\              匹配\

反义
\W              匹配任意不是字母，数字，下划线，汉字的字符
\S              匹配任意不是空白符的字符
\S+             匹配不包含空白符的字符串
\D              匹配任意非数字的字符
\B              匹配一个边界，边界的两边都是单词字符，或都是非单词字符
[^x]            匹配除了x以外的任意字符
[^aeiou]        匹配除了aeiou这几个字母以外的任意字符
[^a-z]          匹配不在指定范围内的任意字符
'''
# \b使用场景1：匹配完整单词
test = "The quick brown fox jumps over the lazy dog."
patter = r"\bfox\b"
# 对于正则表达式\bfox\b，第一个\b其右边是单词字符，那么其左边必须是非单词字符；
# 第二个\b其左边是单词字符，那么其右边必须是非单词字符；
match = re.search(patter, test)
if match:
    print(f"Match found:{match.group()} 起始位置：{match.start()} 结束位置：{match.end()}")
    # Match found:fox 起始位置：16 结束位置：19

'''re.search()'''
# 正则表达式库re中的一个方法，用于在字符串中搜索与正则表达式模式匹配的第一个位置，并返回一个匹配对象，对象的方法有：
# group()：返回匹配的文本
# start(): 返回匹配的起始位置
# end(): 返回匹配的结束位置（不包含该位置的字符）
# 如果没有找到匹配项，则返回None；

# \b使用场景2：避免匹配子字符串
sentence = "The batter hit the ball with the bat."
print(re.findall(r"\bbat\b", sentence))  # ['bat']
# 对于正则表达式\bbat\b，第一个\b其右边是单词字符，那么其左边必须是非单词字符；
# 第二个\b其左边是单词字符，那么其右边必须是非单词字符；
# "batter"中的"bat"不满足，因为bat的右边是个单词字符；

'''re.findall()'''
# 用于查找字符串中所有与正则表达式匹配的子串，并返回一个包含所有匹配结果的列表；
# 如果没有找到匹配项，则返回空列表；

# 简单例子
# \ba\w*\b 匹配以字母a开头的单词（单词可包含字母、数字和下划线）
# 例：源字符串是apple alpha a123 _ab123 a有4处匹配apple、alpha、a123、a
# \d+ 匹配1个或更多连续的数字
# 例：源字符串是apple alpha a123 _ab123 a有2处匹配123、123
# \b\w{6}\b 匹配刚好6个字符的单词
# 例：源字符串是apple alpha a123 _ab123 a有1处匹配_ab123
# ^\d{5,12}$ 只匹配5到12位连续数字
# 例：源字符串是a12345有0处匹配，12345a有0处匹配，1234有0处匹配，1234567890123有0处匹配
# \d{5,12} 匹配包含5到12位连续数字的字符串
# 例：源字符串是a123AG33521k1234567890123有2处匹配，33521、123456789012
# ^\w+ 匹配以字母、数字或下划线开头的字符串，直到非单词字符才停止
examples = ["Hello World", "1_1", "_abc", " Space", "1_1-3"]
for example in examples:
    match = re.match(r'^\w+', example)
    if match:
        print(f"'{example}': Match found -> {match.group()}")
    else:
        print(f"'{example}': No match found")
# 'Hello World': Match found -> Hello
# '1_1': Match found -> 1_1
# '_abc': Match found -> _abc
# ' Space': No match found
# '1_1-3': Match found -> 1_1

'''分枝条件，通过|实现'''
# \d{5}-\d{4}|\d{5} 匹配美国邮编（5位数字，或者用连字号间隔的9位数字如12345-5555）
# 例：源字符串是ABC12345-6789EF有1处匹配，12345-6789
# 注：使用分枝条件时，要注意各条件顺序。从左到右测试每个条件，若满足某个分枝，就不会再管其它条件。
# \d{5}|\d{5}-\d{4} 就只会匹配5位的邮编以及9位邮编的前5位
# 例：源字符串是ABC12345-6789EF有1处匹配，12345

'''分组，通过()实现'''
# ((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?) 匹配ip地址
# 3个分枝
# 分枝2[0-4]\d匹配200-249的数字
# 分枝25[0-5]匹配250-255的数字

# [01]?匹配0或1，出现0次或1次
# \d\d?匹配一个或两个数字，可匹配0到99之间的任意数字
# 分枝[01]?\d\d?匹配0-199的数字
# 例：源字符串是ABC12345-6789EF有4处匹配，123、45、67、89

# \. 匹配一个英文.
# {3} 分组会重复三次，匹配三个数字部分(每个数字后都带一个.)

# 日志中提取IPv4地址
log_data = """
User connected from 192.168.1.26 at 10:45 AM
Failed login from 204.120.0.15 at 10:49 AM
User connected from 10.0.0.5 at 10:50 AM
Error reported from gateway 172.16.23.1 at 10:52 AM
"""

# IPv4 正则表达式
ipv4_regex = r"((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)"

# 查找所有匹配的IPv4地址
ipv4_addresses = re.findall(ipv4_regex, log_data)

# 输出找到的IPv4地址
print(ipv4_addresses)

'''后向引用'''

'''
验证移动手机号码
正则表达式 "(13[4-9]\d{8})$|(15[01289]\d{8})$"
()匹配小括号内的字符串
|表示或
13或15开头
[4-9]表示数字4到9之间均可，[01289]表示数字0、1、2、8、9均可
d{8}匹配连续8个数字
$匹配字符串的结尾
'''
mobile = '13221828837'
pattern = r"(13[4-9]\d{8)$|(15[01289]\d{8})$"
# re.match从字符串的起始位置匹配，没匹配到则返回None
res = re.match(pattern, mobile)
if res is not None:
    print(f'{mobile}是有效的中国移动号码!')
else:
    print(f'{mobile}不是有效的中国移动号码!')

'''
查找多个网址
正则表达式 "https?://.*?\.(?:com|cn)"
https?://  匹配http://或者https://
.*? 非贪婪模式，将匹配最短的以http://或https://开始，以.com或.cn结尾的字符串
\. 匹配一个.
'''


def find_url(string):
    # 当使用re.findall(pattern,s)时，若pattern包含有()，则只匹配括号里内容
    url1 = re.findall("https?://.*?\.(com|cn)", string)
    # (?:)代替()，可匹配全部
    url2 = re.findall("https?://.*?\.(?:com|cn)", string)
    # 返回多个值，返回元组
    return url1, url2


string = "百度的网址为：https://www.baidu.com;杭州市人民政府的网站为：http://www.hangzhou.gov.cn。"
print(find_url(string))  # (['com', 'cn'], ['https://www.baidu.com', 'http://www.hangzhou.gov.cn'])

'''
匹配MAC地址
正则表达式 "[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}"
[0-9a-fA-F]{2} 匹配由两个大小写字母或数字组成的字符串，如00，dc，a8
(:[0-9a-fA-F]{2}){5} 匹配冒号后跟两个大小写字母或数字组成的字符串，匹配5次，如:0C:29:88:83:1A
'''
