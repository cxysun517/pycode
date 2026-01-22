#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

'''#!/usr/bin/env python3'''
# #!是特殊指令，在python中称为Shebang或Hashbang，通常出现在类Unix系统的脚本中第一行，
# 作为前两个字符，后接解释器的绝对路径，用于指明执行这个脚本文件的解释器。
# 这行代码中的env命令会在$PATH环境变量指定的路径中查找python3这个程序，并用其执行该文件。
# 即使系统修改了Python所在的路径也不需要修改脚本中的路径。

'''# -*- coding:utf-8 -*-'''
# 添加此行是为了告诉Python解释器该文件的编码方式。
# Python2.x默认源文件是ASCII编码，若使用中文、日文等非ASCII字符，则必须添加此行。
# Python3.x默认源文件编码方式就是UTF-8，此行不是必需的，但是加上是一个好习惯。

'''Python的由来及特性'''
# 为了增进效率，语言也迫使程序员像计算机一样思考，以便能写出符合机器口味的程序，如c语言。
# unix的管理员们常常用shell去写一些简单的脚本，以进行一些系统维护的工作，如定期备份、文件系统管理等。
# Shell没有数据类型的概念，加法运算都很复杂。无论输入的是字符串、数字，在Shell中都按照字符串类型来存储。
# 总之，shell不能全面调动计算机的功能。
# Python将许多机器层面上的细节隐藏，交给编译器处理，并凸显出逻辑层面的编程思考。
# 以对象为核心组织代码，支持函数式、面向对象等多种编程范式，采用动态类型，自动进行内存回收。

'''函数式编程'''
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda a: a ** 2, nums))
print(squares)  # [1, 4, 9, 16, 25]
# map()会将传入的函数依次应用到可迭代对象的每个元素上，并返回一个迭代器或生成器对象。
# lambda函数是一种匿名函数，其定义由一个简单的表达式完成，其返回值就是该表达式的值。
# 上述代码没有使用循环或者变量来迭代列表中的元素，而是直接将平方函数应用到整个列表上。
# 这就是函数式编程的风格，具有很强的表达能力和简洁性，能够提高代码的复用性和可维护性。
# Python既支持面向过程也支持面向对象编程。
# 面向过程---程序是由过程或仅仅是可重用代码的函数构建起来的。
# 面向对象---程序是由数据和功能组合而成的对象构建起来的。

'''采用动态类型'''
# 解释性---Python语言写的程序不需要编译成二进制代码。
# 静态类型语言：C、C++、Java、Object-C
# 数据类型在编译期间确定，编码时，必须明确指定变量的数据类型，然后再赋值。
# 动态类型语言：Python
# 数据类型不在编译期间确定，变量的类型绑定延后到了运行阶段，使用前不需要类型声明。

'''Python的一些基础语法'''
# 强制缩进---表示代码块
# 多行注释---三个单引号(''' ''')或三个双引号(""" """)
# 标识符---由字母、数字、下划线组成，但不能以数字开头，区分大小写。
# 特殊标识符：
# 以单下划线开头的 _foo ：代表不能直接访问的类属性，需通过类提供的接口进行访问
# 以双下划线开头的 __foo ：代表类的私有成员
# 以双下划线开头和结尾的 __foo__ ：代表特殊方法，如 __init__()代表类的构造函数
# 关键字---如'False', 'None', 'True' 不能用作标识符
# 转义---\n换行符、\r回车符、\\反斜杠、\"双引号、\'单引号
print(r'a\n2')  # a\n2
print('a\n2')

# 一行代码太长如何换行---加反斜杠、加三引号，两者有区别
long_str = 'Hello! Nice to meet you!\
I am happy.'
print(long_str)  # Hello! Nice to meet you!I am happy.
# 当一个长字符串需要断行，则在三引号范围内直接断行即可（原来代码是啥样，输出就是啥样）
demo = """
Hello! Nice to meet you!
    I am happy.
"""
print(demo)
# Hello! Nice to meet you!
#     I am happy.

# 布尔值---None、任何数值类型中的0、空字符串""、空元组、空列表、空字典、空集合等都可以被当作False

'''Python3的六个标准数据类型'''
# 不可变数据（3个）：Number（数值）、String（字符串）、Tuple（元组）
# 可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）
# 数值类型是不允许改变的，如果改变数字数据类型的值，将重新分配内存空间。
# Python不支持单字符类型，单字符在Python中也作为一个字符串使用。

'''运算符'''
# 算数运算符
m = 25
n = 6
print(m % n)  # 取余1
print(m ** n)  # m的n次方
print(m // n)  # 取商的整数，向下取整，4
# 比较运算符 ==  !=
# 赋值运算符 +=  %=
# 位运算符
t = 0b00111100
e = 0b00001101
print(t & e)  # 与运算 12
print(t | e)  # 或运算 61
print(t ^ e)  # 异或运算 49，对应的二进位相异时，结果为1
print(~t)  # 取反运算 -61，补码1100 0011，符号位不变，其它位取反，然后+1得原码10111101
print(t << 2)  # 左移运算 240，高位丢弃，低位补0，1111 0000
# 逻辑运算符 and / or / not
# 成员运算符 in / not in
# 身份运算符 is / is not，判断引用的是否为同一个对象

'''变量的赋值及变量引用'''
# 在Python中，变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在Python中，变量没有类型，"类型"是变量所指的内存中对象的类型。变量只是对对象的一个引用。
# 在Python中，等号"="是赋值语句，可以把任意数据类型赋值给变量。
# 在Python中，赋值(=)操作时，从变量到对象自动建立的连接关系，称为引用。

# 变量引用不可变数据类型如数值、字符串、元组时：值不可改变，如果变了，连接关系就要跟着变掉。
x = 1  # 把变量x绑定到整数对象1上
print(id(x))  # 1603609651504
x = 555  # 解释器并不会修改变量x指向的原内存空间中存放的值1
print(id(x))  # 而是重新开辟内存空间，存放555，x改为指向这新开辟的内存空间 1603615099120

y = 'hi'  # 把变量y绑定到字符串对象上
print(id(y))  # 2741431651824
y = y + 'cxy'
print(id(y))  # 2741431680112

k = (1, 2)  # 把变量k绑定到元组（其元素均为不可变数据类型）对象上，不可改变不可变数据类型的值，否则连接关系改变
print(id(k))  # 2022228760832
k = (1, 2, 3)
print(id(k))  # 2022233402048

j = (1, [2, 3])  # 把变量j绑定到元组（其元素存在可变数据类型）对象上，可改变可变数据类型的值，连接关系不变
print(id(j))  # 2212054715712
j[1][0] = 222
print(id(j))  # 2212054715712

# 变量引用可变数据类型如列表、字典、集合时：值可变，连接关系不变。
list1 = [1, 2]  # 把变量list1绑定到列表对象上
print(id(list1))  # 2072070736000
# append方法会修改列表对象而不会创建一个新的对象
list1.append(3)
print(id(list1))  # 2072070736000

list2 = [1, [2, 3]]  # 把变量list2绑定到列表对象上
print(id(list2))  # 2874178600256
# 修改值
list2[1][1] = 333
print(id(list2))  # 2874178600256
list2.append(555)
print(id(list2))  # 2874178600256

# extend方法会修改列表对象而不会创建一个新的对象
list2.extend([666, 888])
print(id(list2))  # 2874178600256
# 赋值运算符+=会修改列表对象而不会创建一个新的对象
list2 += [999, 111]
print(id(list2))  # 2874178600256
print(list2)  # [1, [2, 333], 555, 666, 888, 999, 111]

# 当执行列表加法操作+时，会创建一个新的列表对象，而不是修改原始列表
# 新列表对象的引用赋给了变量名list2，即把变量list2绑定到了新列表对象上
list2 = list2 + [777]
print(id(list2))  # 1852772973440，连接关系发生了改变

dict1 = {'a': 1, 'b': 2}
print(id(dict1))  # 1259867832640
dict1['b'] = 222
print(id(dict1))  # 1259867832640

set1 = {1, 2}
print(id(set1))  # 2325743163648
set1.add(3)
print(id(set1))  # 2325743163648

'''内存回收机制'''
# Python具有自动内存回收机制，也称为垃圾回收，会检测和清理不再使用的对象，以便回收占用的内存空间。
# Python使用引用计数来追踪每个对象的引用次数。当对象的引用计数归零时，即没有任何变量或数据结构引用该对象，
# Python就会立即回收该对象占用的内存。

'''什么是序列（Sequence）？'''
# 序列（Sequence）是Python中的一种数据结构，它支持索引和切片操作
# 可迭代，有序
# 支持下标访问，实现了getitem()和len()方法
# 内置的序列类型：list、str、tuple、bytes字节数组
# 序列一定是一个可迭代对象，但可迭代对象不一定是序列
# 非序列可迭代对象：set、dict（可直接迭代字典的键）、文件对象（可以迭代文件对象以逐行读取文件）、generator生成器

'''什么是命名空间（namespace）？'''
# A namespace is a mapping from names to objects.
# Most namespaces are currently implemented as Python dictionaries.
# 在Python中，命名空间是从名称（标识符）到他们所引用的对象的映射，大多数命名空间是以字典的形式实现
def test_function():
    local_variable = 10
    print("局部命名空间:", locals())


test_function()  # 局部命名空间: {'local_variable': 10}
# 避免命名冲突，使得同名标识符可以在不同的命名空间中使用而不产生冲突
# 局部命名空间（local namespace）：
# 函数中定义的名称，记录了函数的参数和局部定义的变量
# 全局命名空间（global namespace）：
# 模块中定义的名称，记录了模块级的变量和常量、函数、类、其它导入的模块
# 内置命名空间（build-in）：
# 存放函数名如abs、sum、print和标准异常名称如NameError、Exception等
# 查找顺序：
# 局部命名空间 -> 全局命名空间 -> 内置命名空间

'''什么是作用域？'''
# 变量的可访问范围
# 局部作用域：最内层，包含局部变量，比如一个函数/方法的内部
# 嵌套作用域/闭包函数外的函数中：函数A内部有函数B，查找函数B的变量时，按函数B内部->函数A内部->全局作用域->内建作用域顺序
# 全局作用域：当前脚本的最外层，比如当前模块的全局变量
# 内建作用域：内置函数和异常

# 当在函数内部使用一个变量时，Python解释器会按照以下顺序搜索各个作用域
# 首先在当前函数的局部命名空间（如果存在）中查找
# 找不到，它会查找任何封闭作用域（适用于嵌套函数）
# 还找不到，它会在全局命名空间中查找
# 最后，如果其他地方都没找到，它会在内置命名空间中查找
# 这个查找过程被称为LEGB规则，即Local, Enclosing, Global, Built-in

x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


'''什么是全局变量与局部变量？'''
# 定义在函数外的变量为全局变量
total = 0  # 全局变量


def sum(arg1, arg2):
    # 定义在函数内的变量为局部变量
    total = arg1 + arg2
    print('函数内部是局部变量，值为：', total)
    return total


sum(50, 80)  # 函数内部是局部变量，值为： 130
# 调用sum函数后
print('在函数内部即局部作用域无法修改全局作用域中的全局变量', total)  # 输出0

'''global和nonlocal关键字'''
# global：在局部作用域内修改全局作用域中的变量
# nonlocal：在闭包函数内修改闭包函数外的变量
num = 1  # 全局变量


def fun1():
    global num  # 声明global，修改全局变量
    print('函数内全局变量：', num)  # 输出结果1
    num = 123  # 重新为全局变量num赋值
    print('在函数内修改全局变量：', num)  # 输出结果123


print('未调用函数前num的值：', num)  # 输出结果1
fun1()
print('调用函数后num的值：', num)  # 输出结果123，可见global在函数内部修改了全局变量


def outer2():
    num2 = 10  # 嵌套作用域变量

    def inner2():
        nonlocal num2  # 声明nonlocal，修改闭包外的变量，即嵌套作用域变量
        print('闭包函数内嵌套作用域变量：', num2)  # 10
        num2 = 100  # 改变num的值
        print('在闭包函数内修改嵌套作用域变量：', num2)  # 100

    # 调用嵌套函数
    inner2()
    return num2


w = outer2()
print("嵌套作用域变量被修改了：", w)  # 100

'''作用域和命名空间的关系'''
# 作用域是建立在命名空间之上的一个虚拟的概念，所有的变量都是存储在某个命名空间里的
# 作用域决定了这些变量的可访问范围(可见性)

'''何时会引入新的作用域？'''
# 只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它代码块（如 if/elif/else/、try/except、for/while等）不会引入新作用域，
# 这些语句内定义的变量，外部也可以访问。

while True:
    var = 555
    break
print(var)  # 在外部可访问


def test():
    test_value = '函数中变量'


# 在全局作用域中，无法访问嵌套作用域、局部作用域中所定义的变量
# print(test_vale)# 在外部不可访问，NameError: name 'test_vale' is not defined

'''将Python安装路径添加到Windows的系统变量Path中'''
# 目的：在PC任意目录可运行python及pip
# cmd中执行python，先在cmd当前目录查找python.exe，找不到就在Path中指定的路径查找
# python.exe所在路径：C:\Users\cxy\AppData\Local\Programs\Python\Python39
# pip.exe所在路径：C:\Users\cxy\AppData\Local\Programs\Python\Python39\Scripts

'''模块（module）'''
# 本质上是一个Python程序，以.py作为文件后缀
# 作用：有效避免命名空间的冲突，将一个较大的程序分为多个文件，提升代码的可维护性和可重用性
# 导入方法：
# 1、import 模块名1 [as 别名1], 模块名2 [as 别名2]，…
# 模块名1本身被导入，但保存它原有的命名空间，需要用"模块名1.成员名1"方式访问变量
# 2、from 模块名 import 成员名1 [as 别名1]，成员名2 [as 别名2]，…
# 将该模块的函数/变量导入到当前模块的命名空间中，可直接使用函数/变量

'''if __name__ == '__main__':的作用？'''
# 在完成模块的编写之前，会对其中的功能函数进行调试，对于这些调试代码，希望只在直接运行此py文件时执行，
# 其它模块import此模块时不执行，借助Python内置__name__变量，将调试代码放在if __name__=='__main__'下即可实现。
# 取值有两种：
# py文件直接运行，值为__main__
# py文件被import到其它模块，值为该文件的名字

'''模块的说明文档'''
# 模块的说明文档放在py文件的开头，三个双引号(""" """)
"""
说明文档的内容
"""
# 可以用模块的__doc__来访问模块的说明文档

'''模块的路径'''
# 用import语句导入的模块，Python按下面的顺序查找对应的py文件:
# 1、当前的工作目录：A.py在/opt/test目录下，A.py需要加载B.py，则运行A.py时首先会查找/opt/test目录
# 2、PYTHONPATH（环境变量）中的目录：windows系统环境变量里新建环境变量名PYTHONPATH，值为要导入模块所在的路径
# 3、Python默认的安装目录，即标准连接库目录
# 以上路径都保存在标准模块sys的sys.path变量中
print(sys.path)

# 在导入自己写的模块时，Python解释器提示找不到模块，说明模块没有放在上述三类路径里
# 解决方法：
# 1、向sys.path中临时添加模块文件所在的完整路径，非永久
# import sys
# sys.path.append(r'D:\xxx\yyy')
# 2、windows系统环境变量里新建环境变量名PYTHONPATH，值为要导入模块所在的路径，永久

'''包（package）'''
# 大型项目使用包可以将相关的大量模块组织成一个层次结构，使代码更加模块化、易于管理和复用。
# Python包就是里面装了一个或多个.py文件的文件夹，包含了一组相关的模块和子包。
# 示例
# package/
#     __init__.py
#     module1.py
#     module2.py
#     ...

# import package.module1
# package.module1.some_function()
#
# from package import module2
# module2.some_function()

'''Python包的__init__.py文件'''
# 特殊的文件，告诉Python解释器该目录是一个包，并可以被导入和使用。
# 作用如下：
# 1、初始化包：包含一些初始化代码，用于设置包的环境或变量。
# 2、批量导入其他模块，避免用到时再一一导入。
# 3、控制导入行为：通过定义__all__变量来控制导入。
# __all__是一个包含字符串的列表，用于控制使用from pacakge import *语句时，允许导入哪些模块。
# 示例
# package/__init__.py
# 只导入module1和module2模块
# __all__ = ['module1', 'module2']

'''导入包'''
# 1、import 包名[.模块名[as 别名]
# 2、from 包名 import 模块名 [as 别名]
# 3、from 包名.模块名 import 成员名 [as 别名]

'''库（library）'''
# 标准库：Python官方提供的库，包含大量用于文件操作、字符串处理、网络通信、日期和时间处理、数学运算等各种功能的模块。
# 第三方库：其他开发者或组织编写的库，可通过包管理工具如pip进行安装。

'''pip安装、更新、卸载、查看第三方模块'''
# 在PC任意位置打开cmd，执行命令
# pip install numpy
# pip install -U numpy 更新numpy，注意U必须大写
# pip install xlrd==1.2.0 安装指定版本的包
# pip uninstall xlrd 卸载
# pip list 列出已安装的包
# pip list -o 查看可升级的包
# python -m pip install --upgrade pip 升级pip
# 不指定下载源将直接从https://pypi.org网站下载并安装扩展包
# 下载速度可能会慢，更换国内下载源
# 清华：https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云：http://mirrors.aliyun.com/pypi/simple/
# 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
