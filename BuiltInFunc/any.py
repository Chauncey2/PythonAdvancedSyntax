# -*- encoding:utf-8 -*-
import random 
import os
import sys

def main():
    """
    iterable中含有真值返回True
    可迭代对象如果为空或者不含有真值，则返回False
    """
    crop = [random.randint(-2,2) for _ in range(10)]
    print("原始列表：{}".format(crop))
    print("列表中元素是否含有真值(不含0)：{}".format(any(crop)))

    # 等价函数
    def func():
        for i in crop:
            if  i:
                return True 
        return False
"""
底层实现
"""

if __name__ == '__main__':
    main()