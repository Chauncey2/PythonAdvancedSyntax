# -*- encoding:utf-8 -*-
import random 
import os
import sys



def main():
    """
    eval(expression, globals=None, locals=None) 函数用来执行一个字符串表达式，并返回表达式的值
        
    """
    expression1 ='[1,2,3]'
    expression2 ='1+1'
    expression3 ='pow(1,2)'

    print(eval(expression1))
    print(eval(expression2))
    print(eval(expression3))

if __name__ == '__main__':
    main()