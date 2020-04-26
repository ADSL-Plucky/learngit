'''
@File    :   6.py
@Time    :   2020/03/06 22:01:18
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 前面2个元素为0，1，输出100以内的斐波那契数列；
print("斐波那契数列：",end=' ')
a, b = 0, 1
print(a,end = ' ')
while(b < 100):
    a, b = b, a + b
    print(a,end = ' ')
