# -*- encoding:utf-8 -*-
import random 
import os
import sys


def main():
    """
    bool() 类
    只有True 和False两个实例
    继承自int类（int类有的方法，它也有【conjugate(...)、bit_length(...)等】）
    """
    a = 1
    print("bool类的返回值：{}".format(bool(a)))
    print("bool类的bit_length：{}".format(bool(a).bit_length()))
    # print(dir(bool))
    
"""
底层实现
"""



if __name__ == '__main__':
    main()