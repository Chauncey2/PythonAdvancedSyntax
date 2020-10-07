# -*- encoding:utf-8 -*-
import random 
import os
import sys



def main():
    """
    ascii(object)
    返回一个对象可打印的字符串(转义非 ASCII 字符：)
    如果打印的字符串中包含非ASCII字符，则进行转义（会使用 \\x、\\u 和 \\U 来转义）
    """
    a=1
    print("ascii(object)返回的是什么东西：{}".format(ascii('My name is Ståle'))) #  My name is St\xe5le

"""
底层实现
"""

if __name__ == '__main__':
    main()