#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 串口监视工具
# 每个换行符之后加上本地时戳
# 输出到文本文件
# 输入串口-波特率
# 可使用notepad++实时查看
# timeout=999999
import serial  # python使用Serial模块读取串口数据
import time


class Helper:
    def __init__(self, file_name, port, baut):
        # 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        # 超时设置：None即永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        # 打开串口，并得到串口对象
        self.ser = serial.Serial(port, baut, timeout=0)
        print(dir(self.ser))  # dir()方法尝试返回对象的有效属性列表。
        self.f = open(file_name, 'wb')  # 文件路径，w先清空，再写入，b二进制方式，字节为单位
        pass

    def start_recv(self):
        while True:
            block = self.ser.read()  # ser.read()从端口读字节数据，一次只返回1个字节
            if block:
                if block == b"\r":
                    continue
                if block == b'\n':
                    self.f.write(b"\n[#%10.3f] " % (time.time()))
                else:
                    self.f.write(block)
                self.f.flush()
            else:
                continue

    pass


def monitor(file_name, port, baut=38400):
    h = Helper(file_name, port, baut)
    h.start_recv()
    pass


port = "COM4"
monitor(file_name=f"C:/Log/Serial-COM4/serial_{port}_{int(time.time())}.log", port=port)
