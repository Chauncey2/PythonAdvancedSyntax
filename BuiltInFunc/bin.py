# -*- encoding:utf-8 -*-
import random 
import os
import sys



def main():
    """
    bin(x)
    将一个整数转变为一个前缀为“0b”的二进制字符串
    """
    x = 3
    y = '3'
    z = 2.1
    print("x:{}".format(bin(x)))
    # print("y:{}".format(bin(y))) # 報錯 bin只能接收int型
    # print("z:{}".format(bin(z))) # 報錯 bin只能接收int型

"""
底层实现

"""

if __name__ == '__main__':
    main()