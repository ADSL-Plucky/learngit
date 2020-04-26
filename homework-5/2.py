# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/04/9 15:35:20
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
'''
import time
def deco(func):
    def wrapper(a,b):
        try:
            with open('log.txt',"a+",encoding="utf-8") as f:
                f.write("函数{}开始执行，时间为：{}\n".format(func.__name__,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
                result = func(a,b)
                f.write("函数{}结束执行，时间为：{}\n".format(func.__name__,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            f.close()
        except FileNotFoundError:
            print("The file was not found!")
        except IOError:
            print("Open fail")
        return result
    return wrapper

@deco
def func(a,b):
    print("这是一个计算{} + {}的函数:".format(a,b))
    time.sleep(1)
    print("结果：{}".format(a+b))

if __name__ == '__main__
    func(3,4)