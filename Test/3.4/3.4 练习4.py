# -*- encoding: utf-8 -*-
'''
@File    :   3.4 练习4.py
@Time    :   2020/03/04 09:15:46
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
#  创建一个有10个数字的列表,先输出此列表,然后再输出其中为偶数元素;
list = [10,12,515,13,52,13,220,52,30,16]
print(list)
print("该列表中偶数有：")
for i in range(len(list)):
    if(list[i] % 2 == 0):
        print(list[i])