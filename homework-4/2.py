# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/03/28 20:20:15
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
'''
import datetime
def Judge_Date(Year,Month,Day):
    L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    sum = 0
    L_year = 0  # 闰年数
    C_year = 0  # 平年数
    #如果当年是闰年
    if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
        L[1] = 29
    if Year < 1800:
        print('抱歉，本程序不支持1800年之前的日期查询!')
        return
    if Month not in range(1,13):
        print('一年只有1~12月，请输入正确的月份!')
        return
    if Day not in range(1,L[Month-1]+1):
        print('当月没有该日期，请输入正确的日期!')
        return
    #判定从1800年到该年之间有多少年是润年，多少年是平年
    for year in range(1800, Year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            L_year += 1
        else:
            C_year += 1
    #当年1月1日周几
    Date_differ1 = 366 * L_year + 365 * C_year
    day1 = (3 + Date_differ1) % 7
    if day1 == 0:
        day1 = 7
    #从1月1日到该日期有多少天
    for month in range(Month-1):
        sum = sum + L[month]
    sum = sum + Day - 1
    day2 = (day1 + sum) % 7
    if day2 == 0:
        day2 = 7
    week = int((sum - (7 - day1) - day2) / 7 + 2)
    print('这是{}年第{}周周{}'.format(Year,week,day2))

    # date = list(datetime.date(Year, Month, Day).isocalendar())
    # print('{}年第{}周周{}'.format(date[0],date[1],date[2]))

def Judge_Date_school_calenda(Year,Month,Day):
    L = [29, 31, 30, 31, 30, 31, 31]
    day = 0
    sum = 0
    if Year != 2020:
        print("不在2020年上半学期的区间")
        return
    if Month not in range(2,9):
        print("不在2020年上半学期的区间")
        return
    if Day not in range(1,L[Month-2] + 1):
        print('当月没有该日期，请输入正确的日期!')
        return
    for month in range(Month-2):
        sum = sum + L[month]
    sum = sum + Day - 1
    day2 = (6 + sum) % 7
    if day2 == 0:
        day2 = 7
    week = int((sum - (7 - 6) - day2) / 7 + 2 - 3)
    if week in range(1,28):
        print("这是2020年开学后的第{}周".format(week))
    else:
        print("不在2020年上半学期的区间")

    # date = datetime.date(Year,Month,Day)
    # start = datetime.date(2020,2,17)
    # week = int((date-start).days/7)+1
    # if week in range(1,28):
    #     print("这是开学的第{}周".format(week))
    # else:
    #     print("不在2020年上半学期的区间")
try:
    Year = int(input("请输入年份："))
    Month = int(input("请输入月份："))
    Day = int(input("请输入日期："))
except ValueError:
    print("请输入整数！")
else:
    Judge_Date(Year, Month, Day)
    Judge_Date_school_calenda(Year, Month, Day)

