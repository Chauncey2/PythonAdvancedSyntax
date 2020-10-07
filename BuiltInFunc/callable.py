# -*- encoding:utf-8 -*-
import random 
import os
import sys


class A:
    def __init__(self):
        self.name = 'name'

class B:
    def __init__(self):
        self.name = 'name'

    def __call__(self):
        pass

def main():
    """
    callable() 函数用于检查一个对象是否是可调用的。
    返回True或者False
    python 3.2新增
    
    一个类中如果自定义了一个__call__函数，那么调用callable函数返回的也是True，但是这个类的实例对象也可能调用失败

    """
    a = 1
    def func(): return True
    obja = A()
    objb = B()

    print("变量a调用callable函数：{}".format(callable(a)))         # False
    print("函数func调用callable函数：{}".format(callable(func)))   # True
    print("类实例obja调用callable函数：{}".format(callable(obja))) # False
    print("类实例objb调用callable函数：{}".format(callable(objb))) # True


"""
底层实现
"""



if __name__ == '__main__':
    main()