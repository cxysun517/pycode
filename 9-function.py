#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools
import time

# ###################################################################
# Python中一切内容都可以称为对象:
# 不可变对象（数值类型int/float、字符串、元组tuple）
# 可变对象（列表list、字典dict、集合set）
# ###################################################################
# Python中的函数参数传递遵循Call-by-Object(传递对象的引用)
# Python的变量充其量就是对象的一个引用
# 函数的参数传递本质上就是：从实参到形参的赋值操作
# 变量赋值操作其实是把一个名字绑定到对象上，变量就是一个标签，一个名字
# ###################################################################
import app as app

'''传递不可变对象'''
def test(p):
    # 第三步：执行p = 555，p这个名字又从对象5上给撕了下来
    # 并贴在了555这个对象上，但a还是指向的对象5
    p = 555
    print(p)

# 第一步：给对象5一个名字叫a，a绑定到对象5上，是对象5的一个引用
a = 5
# 第二步：传参，传递的是对象5的引用，即对象5的地址
# 实参a赋值给形参p，p = a，则p也指向了对象5，对象5多了一个名字p
test(a)  # 555
print(a)  # 5

'''传递可变对象'''
def f1(m):
    print('m', id(m))  # a和m指向同一个列表对象
    m.append(3)  # 直接修改这个对象

a = [1, 2]
f1(a)
print('a', id(a))  # id(a)等于id(m)
print(a)  # [1, 2, 3]


# ##############################################################
# 4种参数及定义顺序从先到后：位置参数-默认参数-可变参数-关键字参数
# ##############################################################
'''位置参数，按顺序依次赋值，形参实参一一对应'''
def test(x, y):
    print(f"{x}+{y}={x + y}")

test(1, 100)

'''默认参数必须指向不变对象，必须定义在位置参数的后面'''
def students(name, sex, age=18):
    # 函数返回多值，组成元组
    return name, age, sex

print(students('ym', 'male'))  # ('ym', 18, 'male')
print(students('ph', age=22, sex='female'))  # ('ph', 22, 'female')

'''可变参数，形参会自动组装成一个元组，传入实参的数量可以变化'''
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

'''关键字参数，形参会自动组装成一个dict，实参在传递时是键值对的方式'''
def per_info(name, age, **kw):
    print('name:', name, 'age:', age, kw)

per_info('cxy', '18', city='hz')  # name: cxy age: 18 {'city': 'hz'}
# 已有一个dict了，怎么把它传入函数中，使用**
d = {'city': 'sh', 'job': 'teacher'}
per_info('dyl', '30', **d)
# name: dyl age: 30 {'city': 'sh', 'job': 'teacher'}

'''递归函数：函数内部调用自己'''
# 阶乘
def calNum(num):
    if num > 1:
        result = num * calNum(num - 1)
    else:
        result = 1
    return result

print(calNum(5))  # 120

'''高阶函数：把函数作为参数传入，这样的函数称为高阶函数'''
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))  # 11

# ##########################################
# Python内建了map()、reduce()、filter()函数
# ##########################################
'''
map()：接收两个参数，一个函数和一个Iterable如列表、元组、集合、字符串等
map将传入的函数依次作用到可迭代对象的每个元素，并把结果作为新的Iterator返回
'''
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
string = 'i love you 555!'
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]
print(list(map(str, numbers)))  # ['1', '2', '3', '4', '5']
print(list(map(lambda x: x.upper(), string)))
# ['I', ' ', 'L', 'O', 'V', 'E', ' ', 'Y', 'O', 'U', ' ', '5', '5', '5', '!']

'''
filter用于从可迭代对象（如列表、元组、字符串等）中过滤出
满足指定条件的元素，并将它们以迭代器的形式返回
'''
print(list(map(lambda x: x.upper(), filter(lambda x: x.strip() != "", string))))
# ['I', 'L', 'O', 'V', 'E', 'Y', 'O', 'U', '5', '5', '5', '!']
print(list(map(lambda x: x.upper(), filter(lambda x: x.strip() != "" and x.strip().isalpha(), string))))
# ['I', 'L', 'O', 'V', 'E', 'Y', 'O', 'U']

'''
reduce()：接收两个参数，一个函数和一个可迭代对象
reduce从可迭代对象中逐个取出元素，将当前元素与累积值传递给函数，并返回累积的结果
'''
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = functools.reduce(add, numbers)
print(result)  # 15

# 把序列变为整数
def fn(x, y):
    return x * 10 + y

print(functools.reduce(fn, [1, 3, 5, 7, 9]))  # 13579 = (((1*10+3)*10+5)*10+7)*10+9
# 首次调用：x=1 y=3 返回13
# x=13 y=5 返回135
# x=135 y=7 返回1357
# x=1357 y=9 返回13579

# 自己定义一个将字符串表示的数字转化为整数的函数
def str_to_int(num_str):
    # 数字字符映射到相应的整数值
    digit_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # map函数返回一个Iterator作为reduce函数的参数
    num_int = functools.reduce(lambda x, y: x * 10 + y, map(lambda x: digit_map[x], num_str))
    return num_int

num_str = "13579"
num_int = str_to_int(num_str)
print(num_int)  # 13579

'''匿名函数：lambda关键字定义'''
# 在传入函数时，有时不需要显式地定义函数，直接传入匿名函数更方便
func1 = lambda a, b: a + b
print(func1(3, 4))  # 7
func2 = lambda x, y: x if x > y else y
print(func2(3, 100))  # 100
stus = [
    {"name": "zh", "age": 18},
    {"name": "li", "age": 19},
    {"name": "wu", "age": 17}
]
# 做内置函数的参数
stus.sort(key=lambda x: x['age'])
print(stus)  # [{'name': 'wu', 'age': 17}, {'name': 'zh', 'age': 18}, {'name': 'li', 'age': 19}]

'''生成器(generator)'''
# 生成器表达式
g = (x * x for x in range(10) if x % 2 == 0)
for item in g:
    print(item, end=' ')  # 0 4 16 36 64

# 生成器函数：函数定义中包含yield关键字，使用yield语句来产生结果，而不是使用return语句
# 执行到yield语句并返回后不会立即终止，而是暂停在此处，等待下一次调用
# 例如：打印斐波那契数列的前十个数
# 斐波那契数列：从第三项开始，每一项都等于前两项之和
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()  # 调用generator函数将返回一个generator对象
for _ in range(10):  # _作为临时变量名是一种惯例，表示在循环中不需要使用该变量的值
    print(next(fib), end=' ')   # 通过对generator对象调用next()方法来按需产生值
# 0 1 1 2 3 5 8 13 21 34

# 第1次循环，yield a语句返回a=0，暂停在此处，a=0，b=1
# 第2次循环，从上一次暂停位置继续执行a, b = b, a + b，yield a语句返回a=1，暂停在此处，a=1，b=1
# 第3次循环，从上一次暂停位置继续执行a, b = b, a + b，yield a语句返回a=1，暂停在此处，a=1，b=2
# 第4次循环，从上一次暂停位置继续执行a, b = b, a + b，yield a语句返回a=2，暂停在此处，a=2，b=3

'''处理大文件，一次只读取一行，从而节省内存'''
# def read_file(file_name):
#     file = open(file_name, encoding='utf-8')
#     txt = file.read().strip()
#     return txt
#
# txt = read_file(r'C:\pycode\large_file.txt')
# print(txt)

# 上述代码file.read()一次性将所有内容加载到内存中，在读取大文件时，
# 容易导致溢出，解决此问题，可以用生成器，加载一行，处理一行
def read_large_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        for every_line in file:  # 迭代读取每一行
            yield every_line.strip()  # 每读取到一行后，使用yield语句将此行返回

# 读取大型文件
for line in read_large_file('large_file.txt'):
    # 处理每一行数据
    print(line)

'''迭代器(Iterator)'''
# 可直接作用于for循环的数据类型有以下几种：
# 一类是list、tuple、dict、set、string
# 一类是generator，包括带yield的generator function
# 这些可直接作用于for循环的对象统称为可迭代对象：Iterable

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 生成器都是Iterator，但list、tuple、dict、set、string虽然是Iterable，却不是Iterator
# 把Iterable变成Iterator可以使用iter()函数

'''函数闭包/返回函数：函数可以作为返回值'''
# 应用1：延迟执行，如延迟获取日志
def create_logger():
    logs = []

    def logger(message):
        logs.append(message)
        print("Log:", message)

    def get_logs():
        return logs

    return logger, get_logs

# 将返回的函数分别赋给变量
log, get_all_logs = create_logger()

# 调用log("a")等同于调用logger("a")
log("a")  # Log: a
log("b")  # Log: b
log("c")  # Log: c

# 调用get_all_logs()等同于调用get_logs()
print(get_all_logs())  # ['a', 'b', 'c']

# 应用2：保持状态，如计数器、缓存等
def counter():
    count = 0  # 嵌套作用域变量

    def increment():
        nonlocal count  # 声明nonlocal，修改闭包外的变量，即嵌套作用域变量
        count += 1  # 改变count的值
        return count

    return increment

# 将返回的函数赋给变量
my_counter = counter()

# 调用my_counter()等同于调用increment()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3

'''装饰器：被装饰函数增加新功能，但不修改源代码'''
# 将原函数作为参数传递给装饰器函数。
# 装饰器函数内部定义一个新函数来包装原函数，并在新函数中添加装饰器的功能。
# 当调用原函数时，实际上调用的是装饰器函数返回的新函数。
# 新函数会首先执行装饰器的功能，然后再执行原函数的功能。
# 常用于日志打印、性能监测、权限校验等场景。

# 应用1：日志打印
# 定义一个装饰器函数logger，接收一个函数作为参数
def logger(func):
    def wrapper(*args, **kw):
        print(f'我准备开始计算{func.__name__}函数了:')

        # 执行原函数的功能
        func(*args, **kw)

        print('啊哈，我计算完啦。给自己加个鸡腿！！')
    return wrapper

@logger
def add(x, y):
    print(f'{x} + {y} = {x+y}')

add(200, 50)
# 我准备开始计算add函数了:
# 200 + 50 = 250
# 啊哈，我计算完啦。给自己加个鸡腿！！

'''可变参数*args和关键字参数**kwargs'''
def my_func(*args, **kwargs):
    print(args)  # (1, 2)
    print(kwargs)  # {'a': 3, 'b': 4}
# 在函数内部，args参数将被打包为一个元组，而kwargs参数将被打包为一个字典
my_func(1, 2, a=3, b=4)

# 应用2：性能监测（函数执行时间）
def time_took(func):
    def wrapper(*args, **kwargs):
        stat_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}函数执行花费了{end_time - stat_time}秒。')
        return res
    return wrapper

# 装饰器语法@time_took装饰calculate_sum
# 相当于执行了calculate_sum = time_took(calculate_sum)
# 这将calculate_sum重新赋值为装饰器函数返回的函数wrapper
@time_took
def calculate_sum(n):
    return sum(range(1, n+1))

# 调用calculate_sum()时，实际调用的是装饰器函数返回的函数wrapper()
print(calculate_sum(100000))
# calculate_sum函数执行花费了0.0021343231201171875秒。
# 5000050000

# 应用3：权限校验