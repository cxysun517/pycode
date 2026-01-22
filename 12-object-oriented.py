#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 面向对象：把数据及对数据的操作方法放在一起，作为一个相互依存的整体。
# 对同类对象抽象出其共性，形成类。
# 面向对象的基本特性:抽象、封装、继承、多态。
# 实例方法、类方法、静态方法
# 定义静态方法主要是规避两个模块调用同名函数的情况
class Car:
    car_num = 0  # 类属性

    def __init__(self, brand, color, price):
        self.carBrand = brand  # 实例属性
        self.carColor = color
        self.carPrice = price
        Car.car_num += 1

    # 类方法，只访问类属性，至少有一个cls参数
    @classmethod
    def car_count(cls):
        print(f"我有{cls.car_num}辆车")

    # 实例方法，调用实例属性，至少有一个self参数
    def level(self):
        if self.carPrice > 300000:
            print(f"{self.carBrand}是高级轿车")
        else:
            print(f"{self.carBrand}是非高级轿车")

    # 静态方法，什么属性都不访问
    @staticmethod
    def tips():
        print("温馨提示：开车不喝酒")


# __init__()方法在对象创建时默认被调用
# 默认有个参数self，python解释器会自动把当前对象的引用传递进去
BWM = Car('宝马', 'white', 600000)
van = Car('五菱宏光', 'red', 70000)
BWM.level()  # 调用实例方法
van.level()
print(f'The color of BWM is {BWM.carColor}.')
Car.car_count()  # 调用类方法
Car.tips()  # 调用静态方法


# 类属性：该类所有实例共享，实例对象只能访问它，不可修改
# 实例属性：每个实例本身独有
class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.dogName = name  # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')
print(f'{d.kind} {d.dogName}')  # canine Fido
print(f'{e.kind} {e.dogName}')  # canine Buddy

'''
访问限制
以双下划线__开头的，私有的类属性或方法，private
类的外部无法通过"类的实例对象.类属性或方法"的方式来直接访问
可通过给类增加get和set方法来实现外部访问
'''


class Student:
    def __init__(self, name, score):
        self.__studentName = name
        self.__studentScore = score

    def get_info(self):
        return f'name = {self.__studentName}, score = {self.__studentScore}'

    def set_score(self, score):
        if 0 < score < 100:
            self.__studentScore = score
        else:
            return ValueError('bad score')


peter = Student('Peter', 78)
# print(peter.__studentName)  # 报错，类外部不能直接访问类的私有属性
print(peter.get_info())

peter.set_score(88)  # name = Peter, score = 78
print(peter.get_info())  # name = Peter, score = 88

'''
继承和多态
一个类可以继承一个或多个父类。原始类称为基类（base）或超类（super）
'''
