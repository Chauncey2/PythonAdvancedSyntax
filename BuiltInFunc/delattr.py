# -*- encoding:utf-8 -*-
import random 
import os
import sys

"""
delattr 
删除对象的属性
1.类属性
2.property装饰器装饰的属性

"""

class A:

    name = "test"
    age=19
    classname=1

    def __init__(self):
        pass

    @property
    def foo(self):
        return self._foo
    
    
"""
底层实现
"""





if __name__ == '__main__':
    a = A()
    print("删除之前的属性：{}".format(dir(a))) # 用到了另一个内置韩式dir 查看类A的属性
    delattr(A,'classname')
    print("删除之后的属性：{}".format(dir(a))) # 用到了另一个内置韩式dir 查看类A的属性
    delattr(A,'foo') # 删除由装饰器装饰的属性foo
    print("删除之后的属性：{}".format(dir(a)))