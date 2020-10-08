# -*- encoding:utf-8 -*-
import random 
import os
import sys



def main():
    """
    exec(object[, globals[, locals]]) 函数用来执行一个字符串表达式，并返回表达式的值
    执行作为字符换定义的python命令    
    """

    python_str = "print('字符串转换命令')"
    
    exec(python_str)
    
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    



if __name__ == '__main__':
    # main()
    func()
