#!/usr/bin/env python3
# -*- coding:utf-8 -*-
i = 1
aggregate = 0
while i <= 100:
    aggregate += i
    i += 1
print("1+2+3+...+99+100=%d" % aggregate)

i = 1
aggregate = 1
while i <= 100:
    if i % 2 == 0:
        aggregate += i
    i += 1
print("1+2+4+...+98+100=%d" % aggregate)

# 打印5行*
i = 1
while i <= 5:
    print(i * '* ')
    i += 1

i = 1
while i <= 5:
    print(i * '*  ')
    i += 1
j = 4
while j >= 1:
    print(j * '*  ')
    j -= 1

i = 1  # 九九乘法表第i行
while i <= 9:  # 循环打印乘法表第i行
    k = 1
    while k <= i:
        product = k * i
        print("%d*%d=%d" % (k, i, product), end=' ')
        if k == i:
            print('\n', end='')  # 换行
        k += 1
    i += 1

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}x{i}={i * j}", end='\t') if i >= j else None
    print()

# 打印100到200之间素数
for num in range(100, 201):
    j = 0
    for i in range(1, num + 1):
        if num % i == 0:
            j += 1
    if j == 2:
        print(num)
