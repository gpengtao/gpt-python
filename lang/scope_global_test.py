#!/usr/bin/python
"""
全局变量测试代码
"""
a = 0  # initialize variable a，函数外部进行初始化


def coo():
    global a  # 函数内部通过global关键字呼叫这个变量，就可以实现全局变量的功能
    a += 1
    return a


for i in range(10):
    print(coo())
