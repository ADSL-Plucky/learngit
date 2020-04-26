
'''
@File    :   3.py
@Time    :   2020/03/06 21:04:19
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
#  定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
from random import randint
def Remove_same_elements(list):
    i = 9
    list.sort()
    while(i>0):
        if(list[i] == list[i-1]):
            del list[i-1]
        i -= 1   
    return list
list1 = [randint(0,30) for _ in range(10)]
list2 = [randint(0,30) for _ in range(10)]
print("列表1：",list1)
print("列表2：",list2)
list1 = Remove_same_elements(list1)
list2 = Remove_same_elements(list2)
list = list1 + list2
print("相同的元素：")
for i in range(31):
    if list.count(i) > 1:
        print(i)