'''
@File    :   8.py
@Time    :   2020/03/06 22:19:07
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
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
for i in range(10):
    for j in range(i+1,10):
        if employees[j][3] > employees[i][3] :
            a = employees[i]
            employees[i] = employees[j]
            employees[j] = a
print("按照工资从高到低排序后：")
print("工号  姓名 工龄  工资")
for i in range(10):
    for j in range(4):
        print("{:^4}".format(employees[i][j]),end=' ')
    print()
