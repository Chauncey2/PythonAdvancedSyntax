# -*- encoding:utf-8 -*-




def main():
    """
    chr()
    返回 Unicode 码位为整数 i 的字符的字符串格式
    """
    a,b,c,d = 97,101,'c',8364

    print("a:{}".format(chr(a))) # a
    print("b:{}".format(chr(b))) # e
    # print("c:{}".format(chr(c))) # 只能接收整数实参，返回一个Unicode码字符号格式
    print("d:{}".format(chr(d))) #  €

"""
底层实现
"""

if __name__ == '__main__':
    main()