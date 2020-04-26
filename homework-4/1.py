# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/03/28 20:10:15
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
  用deque来实现，同样记录程序所耗费的时间；
  输出这2个时间的差值；
  提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''
import time
from random import randint
from collections import deque

List1 = [randint(0,100) for _ in range(10)]
start1 = time.time()
List1.insert(0,0)
List1.append(0)
end1 = time.time()
print(List1)

List1 = [randint(0,100) for _ in range(10)]
List2 = deque(List1)
start2 = time.time()
List2.append(0)
List2.appendleft(0)
end2 = time.time()
print(List2)

print("List 的insert和append操作耗时：",end1 - start1)
print("deque的append和appendleft操作耗时：",end2 - start2)
print("两种操作的时间差：",(end1 - start1) - (end2 - start2))