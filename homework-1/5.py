'''
@File    :   5.py
@Time    :   2020/03/06 21:53:44
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 使用random模块，生成随机数，来初始化一个列表，元组；
from random import randint
List = [randint(0,100) for _ in range(10)]
Tuple = tuple(randint(0,100) for _ in range(10))
print("列表：",List)
print("元组：",Tuple)