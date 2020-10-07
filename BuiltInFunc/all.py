# -*- encoding:utf-8 -*-
import random 
import os
import sys

def main():
    """
    all,逻辑类内置函数
    iterator为空，或者元素全为真，返回True，否则返回False
    """
    crop = [random.randint(-2,2) for _ in range(10)]
    print("原始列表：{}".format(crop))
    print("列表中元素是否全为真(不含0)：{}".format(all(crop)))

    # 等价函数
    def func():
        for i in crop:
            if not i:
                return False 
        return True

"""
底层实现
"""


if __name__ == '__main__':
    main()