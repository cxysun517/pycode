#!/usr/bin/env python3
# -*- coding:utf-8 -*-
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"1+2+3+...+99+100={sum}")

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(f"2+4+...+98+100={sum}")

i = 1
sum = 0
while i <= 100:
    if i % 2 != 0:
        sum += i
    else:
        sum -= i
    i += 1
print(f"1-2+3-4+...+99-100={sum}")

'''多层循环可以使用while循环嵌套，也可以使用for循环嵌套'''
# 例子1：打印100到200范围内的素数（质数），即大于1的整数中，只能被1和这个数本身整除的数
# 代码一，while循环嵌套
num = 100
while num <= 200:
    i = 1
    j = 0
    while i <= num:
        if num % i == 0:
            j += 1
        i += 1
    if j == 2:
        print(num)
    num += 1

# 代码二，for循环嵌套
for num in range(100, 201):
    j = 0
    for i in range(1, num + 1):
        if num % i == 0:
            j += 1
    if j == 2:
        print(num)


# 求任意区间内的素数
def is_prime(min_num, max_num):
    prime_list = []
    for n in range(min_num, max_num + 1):
        j = 0
        for i in range(1, num + 1):
            if n % i == 0:
                j += 1
        if j == 2:
            prime_list.append(n)
    return prime_list


# a = int(input("请输入区间左端点："))
# b = int(input("请输入区间右端点："))
a, b = map(int, input("请输入区间左右端点：").split())  # 请输入区间左右端点：100 200
# map()会将传入的函数依次应用到可迭代对象的每个元素上，并返回一个迭代器或生成器对象。
# split()指定分隔符分割字符串，可指定分割几次，默认分割到底，返回一个列表。若不指定参数即默认分隔符为空格、换行符\n、制表符\t
# a, b = ... 多重赋值语句，允许同时为多个变量赋值

print(is_prime(a, b))
# [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]


# 例子2：打印九九乘法表
# 代码一，while循环嵌套
row = 1  # 九九乘法表第row行
while row <= 9:  # 循环打印乘法表第row行
    k = 1
    while k <= row:
        # print("%d×%d=%d" % (k, row, k * row), end='\t')
        print(f"{k}x{row}={k * row}", end='\t')
        if k == row:
            print('\n', end='')  # 换行
        k += 1
    row += 1

'''格式化字符串 f'''
# 代码二，for循环嵌套
for row in range(1, 10):
    for k in range(1, row + 1):
        print(f"{k}x{row}={k * row}", end='\t')
        if k == row:
            print('\n', end='')  # 换行

'''
打印如下图形
* 
* * 
* * * 
* * * * 
* * * * * 
'''
i = 1
while i <= 5:
    print(i * '* ')
    i += 1

'''
打印如下图形
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *  
*  *  *  *  
*  *  *  
*  *  
*  
'''
i = 1
while i <= 5:
    print(i * '*  ')
    i += 1
j = 4
while j >= 1:
    print(j * '*  ')
    j -= 1
