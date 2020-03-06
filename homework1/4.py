
'''
@File    :   4.py
@Time    :   2020/03/06 21:45:15
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 判断用户输入的年份是否为闰年
try:
    year = int(input("请输入年份："))
except ValueError as e:
    print("输入错误：",e)
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("年份{}为闰年".format(year))
else:
    print("年份{}不为闰年".format(year))
