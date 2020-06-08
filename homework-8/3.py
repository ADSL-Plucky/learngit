# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/05/20 21:25:18
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数 判断一个数字是否为素数，
   然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
import math
import time
from multiprocessing import Pool

#判断一个数字是否为素数
def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        else:
            return True

def timekeeping(func):
    def Time(*args):
        t_start = time.time()
        result = func(*args)
        t_end = time.time()
        print(t_end - t_start)
        return result
    return Time

@timekeeping
def processePool(n):
    pool = Pool(n)
    list = pool.map_async(func=isprime,iterable=range(1,100000))
    pool.close()
    pool.join()
    count = 0
    for i in list._value:
        if i == True:
            count += 1
    return count

@timekeeping
def prime(x):
    num = 2
    Num = 0
    while num < x:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            Num += 1
        num += 1
    return Num

if __name__ == "__main__":
    print("不使用多进程所用时间：",end = "")
    print("结果："+ str(prime(100000)))
    print("使用4个进程所用时间：",end="")
    print("结果：" + str(processePool(4)))
    print("使用10个进程所用时间：",end="")
    print("结果：" + str(processePool(10)))