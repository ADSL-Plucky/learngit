# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/04/9 15:20:52
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
1  编写一个装饰器，能计算其他函数的运行时间；
'''
import time
def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("函数运行时间：{}s".format(end - start))
    return wrapper
@deco
def func(a,b):
    print("这是一个计算{} + {}的函数:".format(a,b))
    time.sleep(0.5)
    print("结果：{}".format(a+b))

if __name__ == '__main__':
    func(3,4)
