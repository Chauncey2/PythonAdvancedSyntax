# -*- encoding:utf-8 -*-
import random 
import os
import sys




def main():
    """
    abs数学类内置函数
    返回整数的绝对值，返回复数的模
    """
    integer = -10
    complex_num = 1 + 1J
    print("整数-10的绝对值：{}".format(abs(integer)))
    print("复数1+J的绝对值：{}".format(abs(complex_num))) # 输出根号2的值

"""
abs底层实现
"""


if __name__ == '__main__':
    main()