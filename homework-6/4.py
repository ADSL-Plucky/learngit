# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2020/04/12 20:53:20
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''
class Student:
    def __init__(self,name = "",age = 0,sex = "男",Chinese = 0,Math = 0, English = 0):
        self.name = name
        self.age = age
        self.sex = sex
        self.Chinese = Chinese
        self.Math = Math
        self.English = English
    def Sum(self):
        return self.Chinese + self.Math + self.English

    def Average(self):
        return self.Sum() / 3

    def Print(self):
        print("学生姓名：{}".format(self.name))
        print("年龄:{}".format(self.age))
        print("性别：{}".format(self.sex))
        print("语文成绩：{}".format(self.Chinese))
        print("数学成绩：{}".format(self.Math))
        print("英语成绩：{}".format(self.English))
if __name__ == "__main__":
    student = Student('Jack',18,'male ',70,80,90)
    student.Print()
    print("总分：{}".format(student.Sum()))
    print("平均分：{}".format(student.Average()))
