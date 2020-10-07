# -*- encoding:utf-8 -*-
import random 
import os
import sys


"""
实例方法：第一个参数self,指实例本身，调用方法为 类实例名.func()，内部可调用类方法
类方法：第一个参数为cls，指类本身，调用方法为 类名.func() ，可调用类属性
静态方法：参数无限制，@staticmethod装饰器声明，外部无法调用，由实例方法或者类方法调用
         调用方式， [类名.func()] (类方法内调用)
                   [self.func()] (实例方法内调用)

静态方法服务于实例方法或类方法

实例方法可以调用【静态方法】或者【类方法】
类方法可以调用【静态方法】
静态方法可以调用【静态方法】或【类方法】（ps：用类名.方法名）
"""
class A:

    class_name = "A"
    class_func = "Test classmethod"

    def __init__(self,name):
        self.name = name

    def instance_method(self):
        print("实例方法")
        print("the name is {}".format(self.name))
        print("instance_method调用静态方法：{}".format(self.static_method()))
        # 实例方法内调用类方法
        A.class_method()

    @classmethod
    def class_method(cls):
        print("类方法，类本身自己背调用")
        print(cls.class_name)
        print(cls.class_func)
        print("class_method调用静态方法：{}".format(A.static_method()))
        # 类方法无法调用实例方法
        # self.instance_method()

    @staticmethod
    def static_method():
        A.static_method2()

        return "我是静态方法，可以被实例方法或者类方法调用"

    @staticmethod
    def static_method2():
        # 写在这里是为了说明可以静态方法内调用类方法，不能这么用（循环调用了）
        # A.class_method()
        print("静态方法2")




if __name__ == '__main__':
    a = A("Tom")
    a.instance_method()
    print("="*20)
    A.class_method()



