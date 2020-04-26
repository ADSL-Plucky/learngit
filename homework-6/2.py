# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/04/12 20:05:25
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
二 定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
'''
class student:
    name = ''
    age = 0
    Chinese = 0
    Math = 0
    English = 0
    def __init__(self, name, age, Chinese, Math, English):
        self.name = name
        self.age = age
        self.Chinese = Chinese
        self.Math = Math
        self.English = English
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        return max(self.Chinese, self.Math ,self.English)
if __name__ == '__main__':
    A = student('Jack', 18, 98, 50, 60)
    print('对象A所存储的学生姓名为{}，年龄为{}，3门科目中最高的分数是{}'.format(A.get_name(),A.get_age(),A.get_score()))

    B = student('Tom', 22, 50, 80, 90)
    print('对象B所存储的学生姓名为{}，年龄为{}，3门科目中最高的分数是{}'.format(B.get_name(),B.get_age(),B.get_score()))