# -*- encoding:utf-8 -*-
import random 
import os
import sys


def main():
    """
    enumerate((iterable, start=0) 缺省参数start
    返回迭代元素和一个技术值
    """
    l = [random.uniform(-1,1) for _ in range(10)]

    for key,value in enumerate(l):
        print(key," ",value)

"""
等价实现
"""
def enumerate(sequence, start=10):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

"""
底层实现
"""


if __name__ == '__main__':
    main()