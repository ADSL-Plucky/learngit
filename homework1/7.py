'''
@File    :   7.py
@Time    :   2020/03/06 22:10:04
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
#  打印输出9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{:2}*{:2}={:2}".format(j,i,i*j),end=' ')
    print()