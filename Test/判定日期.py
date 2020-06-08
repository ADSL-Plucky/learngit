# -*- encoding: utf-8 -*-
'''
@File    :   判定日期.py
@Time    :   2020/03/03 08:42:52
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''

L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
count = 0
for year in range(1901, 2001):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        L[1] = 29
        print("闰年 = ",year)
    else:
        L[1] = 28
        print("year = ",year)
    for month in range(1, 13):
        day += L[month - 1]
        if(day % 7 == 0):
            count += 1
print (count)
