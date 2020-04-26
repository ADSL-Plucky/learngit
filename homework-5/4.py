# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2020/04/9 15:55:10
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
     可以观看给的视频材料，仿照示例来做；
'''
import math

#目标函数无参数无返回值
def decoA(func):
    def A():
        func()
    return A

@decoA
def primeA():
    num = 2
    list1 = []
    print('函数A 打印输出20000之内的素数；')
    while num < 20000:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            list1.append(num)
        num += 1
    print(list1)

primeA()


# 目标函数有返回值
def decoB(func):
    def B():
        result = func()
        return result
    return B

@decoB
def primeB():
    num = 2
    number = 0
    print('函数B 计算整数2-10000之间的素数的个数；')
    while num < 10000:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            number += 1
        num += 1
    return number

result = primeB()
print("函数B的结果为{}".format(result))


# 目标函数有参数
def decoC(func):
    def C(M):
        func(M)
    return C

@decoC
def primeC(M):
    num = 2
    number = 0
    print("函数C 计算整数2-{}之间的素数的个数；".format(M))
    while num < M:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            number += 1
        num += 1
    print("函数C的结果为{}".format(number))

primeC(10000)


# 目标函数有参数有返回值
def decoD(func):
    def D(X):
        result = func(X)
        return result
    return D
@decoD
def primeD(M):
    num = 2
    number = 0
    print("函数D 计算整数2-{}之间的素数的个数；".format(M))
    while num < M:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            number += 1
        num += 1
    return number

result = primeD(20000)
print("函数D的结果为{}".format(result))



