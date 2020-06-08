# -*- encoding: utf-8 -*-
'''
@File    :   b.py
@Time    :   2020/02/26 08:33:25
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
题目内容：
10以内的素数2,3,5,7的和为17。要求计算得出任意正整数n以内的所有素数的和。
输入格式:
一个正整数n。
输出格式：
n以内的所有素数的和。
输入样例：
10
输出样例：
17
'''
import  math
def is_primer(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
count = 0
for x in range(2, n):
    s = str(x)
    for i in s:
        if i in ['0', '2', '4', '5','6', '8']:
            break
    else:
        l = 0
        tx = x
        flag = 0

        if is_primer(x):
            t = str(x)
            l = len(t)
            if l == 1:
                count += 1
            else:
                flag = 1
                temp = 0
                init = x
                while temp != init:
                    i = int(x / 10)
                    j = int(x % 10)
                    temp = j * (10 ** (l - 1)) + i
                    if is_primer(temp):
                        flag = 1
                        x = temp
                    else :
                        flag = 0
                        break
            if flag == 1:
                count += 1
print (count+2)