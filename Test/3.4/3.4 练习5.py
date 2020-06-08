# -*- encoding: utf-8 -*-
'''
@File    :   3.4 练习5.py
@Time    :   2020/03/04 09:30:06
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, '是质数')