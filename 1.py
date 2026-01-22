#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a = 1
b = 2
y = a
a = b
b = y
print("a=%d,b=%d" % (a, b))

print(max([33, 5 + 61, 7, -15, 19, 55, 0]))
print(min([33, 5, 7, -15, 19, 55, 0]))

f = open('String.py', 'r', encoding='UTF-8')
linelist = f.readlines()
for i in linelist:
    if i.startswith('#'):
        continue
    else:
        print(i.replace('\n', ''))
f.close()
