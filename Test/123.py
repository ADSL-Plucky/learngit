# -*- encoding: utf-8 -*-
'''
@File    :   123.py
@Time    :   2020/02/21 10:25:42
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
employees =[
    [1,"赵妲",3,11000],
    [2,"钱耳",2,10000],
    [3,"孙三",5,16000],
    [4,"李思",5,18000],
    [5,"周武",3,11000],
    [6,"吴流",1,10000],
    [7,"郑期",2,11000],
    [8,"王巴",4,14000],
    [9,"冯酒",4,15000],
    [10,"陈时",3,13000],
]
print(employees)
a = employees[1]
employees[1] = employees[0]
employees[0] = a
print(employees)

# from collections import Counter
# word = "Given a paragraph of English text , count the number of occurrences of each word\
# Print output , output from high to low according to word frequency"
# c = Counter(word.split())        获得一个字典
# print(c)