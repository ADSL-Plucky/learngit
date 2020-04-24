# 3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#    数字列表请用随机数函数生成;
from random import randint
def Find_odd(n):
    for i in range(len(n)):
        if n[i] % 2 != 0:
            print(n[i],end = ' ')
list1 = [randint(0,100) for _ in range(10)]
print(list1)
Find_odd(list1)