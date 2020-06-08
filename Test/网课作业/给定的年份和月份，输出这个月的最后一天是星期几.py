'''
题目内容：
若已知1800年1月1日为星期3，则对于一个给定的年份和月份，输出这个月的最后一天是星期几。
输入格式:
两行整数，分别代表年份和月份
输出格式：
星期数，0代表星期日
输入样例：
2033
12
输出样例：
6
'''
L = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
sum = 0
Year = int(input(""))
Month = int(input(""))
L_year = 0   #闰年数
C_year = 0   #平年数
d = 0
for year in range(1800, Year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        L_year += 1
    else:
        C_year += 1
if(Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    L[1] = 29
for month in range(Month):
    sum = sum + L[month]
Day = 366 * L_year + 365 * C_year + sum - 1
day = (3 + Day) % 7
print(day)
