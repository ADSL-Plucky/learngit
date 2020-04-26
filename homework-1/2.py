'''
@File    :   2.py
@Time    :   2020/03/06 20:35:29
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
#  一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）
from random import randint
key = [i for i in range(1,11)]
value = [randint(0,100) for _ in range(10)]
student = dict(zip(key,value))
print("10位同学的信息：",student)
print("大于80分的同学：")
for key,value in student.items():
    if(value > 80):
        print("学号：{},分数：{}".format(key,value))