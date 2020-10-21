# -*- encoding:utf-8 -*-
import random 
import os
import sys

"""
filter(function, iterable)
1. 根据定义的function 从iterable中筛选满足func条件的元素，组成新的 iterable 对象
iterable 中的元素挨个传入func进行判断
2. 如果function = None ,则 filter 对iterable进行过滤，筛选出为真的元素组成新的iterable 
3. 如果function ！= None,此时的filter相当于一个列表生成式
    (item for item in iterable if function(item))
4. function 可以是其他返回bool型数据的内置函数比如bool(),也可以是lambda表达式，也可以是自己定义的函数
    但是都必须是接收iterable中的元素进行判断，并返回bool型数据的表达式，否则这个函数就没有意义。
"""

def main():

    l = [1,1,1,1,0] # 5个元素
    iter_obj_int = filter(None,l) # 返回 <filter object at 0x0000021897545F28> 迭代器对象

    bool_list = [True,True,True,True,False]
    iter_obj_bool = filter(None,bool_list)

    print(list(iter_obj_int)) # [1, 1, 1, 1]
    print(list(iter_obj_bool)) # [True, True, True, True]

    iter_obj_int_by_lamdba = filter(lambda i : i > 0,l)
    print(list(iter_obj_int_by_lamdba)) # [1, 1, 1, 1]
    
if __name__ == '__main__':
    main()