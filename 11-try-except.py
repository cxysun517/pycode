#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 使用 assert 检查除数是否为非零值
def divide(a, b):
    assert b != 0, "除数不能为零"
    return a / b


# 使用 try/except 处理可能出现的异常
try:
    result = divide(10, 0)
    print(result)
except AssertionError as error:
    print(f"错误: {error}")

print('继续执行下面的代码')
# 运行结果：
# 错误: 除数不能为零
# 继续执行下面的代码
