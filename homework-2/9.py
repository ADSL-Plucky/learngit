'''
定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
from random import randint
from collections import Iterable
def Sort(arr):
    if isinstance(a, Iterable):
        return sorted(arr)
    else:
        pass
a = [randint(0,100) for _ in range(20)]
b = (randint(0,100) for _ in range(20))
c = {randint(0,100) for _ in range(20)}
d = 'qwerrttyigjhf'
print(a)
print(Sort(a))
print(isinstance(a, Iterable))
print(tuple(b))
print(Sort(b))
print(c)
print(Sort(c))
print(d)
print(Sort(d))