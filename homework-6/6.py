# -*- encoding: utf-8 -*-
'''
@File    :   6.py
@Time    :   2020/04/12 23:45:10
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
六  用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;
'''
class Student:
    def __init__(self, data):
        self.Class = data[0]
        self.number = data[1]
        self.name = data[2]
        self.score = data[3]
    def Print(self):
        print("班级：{} 学号：{} 姓名：{} python成绩：{}".format(self.Class, self.number, self.name, self.score))
        
class system:
    Stu = []

    def __init__(self):
        try:
            with open('student information.txt', "r", encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    data = line.split(" ")
                    self.Stu.append(Student(data))
            f.close()
        except FileNotFoundError:
            print("The file was not found!")
        except IOError:
            print("Open fail")

    def Add(self):
        try:
            print("开始添加学生信息！")
            Class = int(input("请输入班级："))
            number = int(input("请输入学号："))
            name = input("请输入姓名：")
            score = input("请输入python成绩：")
            Data = [Class, number, name, score]
            self.Stu.append(Student(Data))
            with open('student information.txt', "a+", encoding="utf-8") as f:
                f.write('{} {} {} {}\n'.format(Class,number,name,score))
            f.close()
            print("添加成功！")
        except ValueError as e:
            print(e)
        except FileNotFoundError:
            print("The file was not found!")
        except IOError:
            print("Open fail")

    def Delete(self):
        print("开始删除学生信息！")
        name = input("请输入需要删除信息的学生姓名：")
        for i in range(len(self.Stu)):
            if name == self.Stu[i].name:
                del self.Stu[i]
                try:
                    with open('student information.txt', "w", encoding="utf-8") as f:
                        for student in self.Stu:
                            f.write('{} {} {} {}\n'.format(student.Class,student.number,student.name,student.score))
                    f.close()
                except FileNotFoundError:
                    print("The file was not found!")
                except IOError:
                    print("Open fail")
                print("删除成功！")
                break
        else:
            print("没有该学生！删除失败！")

    def change(self):
        print("开始更改学生信息！")
        name = input("请输入需要更改信息的学生姓名：")
        for i in range(len(self.Stu)):
            if name == self.Stu[i].name:
                print("已找到该学生，请选择需要更改的信息：")
                print("1.班级 2.学号 3.姓名 4.python成绩")
                try:
                    choose = int(input())
                    if choose == 1:
                        Class = int(input("请输入更改后的班级："))
                        self.Stu[i].Class = Class
                    elif choose == 2:
                        number = int(input("请输入更改后的学号："))
                        self.Stu[i].number = number
                    elif choose == 3:
                        name = input("请输入更改后姓名：")
                        self.Stu[i].name = name
                    elif choose == 4:
                        score = input("请输入更改后python成绩：")
                        self.Stu[i].score = score
                    with open('student information.txt', "w", encoding="utf-8") as f:
                        for student in self.Stu:
                            f.write('{} {} {} {}\n'.format(student.Class,student.number,student.name,student.score))
                    f.close()
                    print("更改成功！")
                    print("更改后该学生的信息如下：")
                    self.Stu[i].Print()
                except ValueError as e:
                    print(e)
                except FileNotFoundError:
                    print("The file was not found!")
                except IOError:
                    print("Open fail")
                break
        else:
            print("没有该学生，无法修改信息！")

    def search(self):
        print("开始查询学生信息！")
        name = input("请输入需要查询信息的学生姓名：")
        for i in range(len(self.Stu)):
            if name == self.Stu[i].name:
                print("该学生的信息如下：")
                self.Stu[i].Print()
                break
        else:
            print("没有该学生！")

    def Panel(self):
        while True:
            print("0.退出程序")
            print("1.增加学生信息")
            print("2.删除学生信息")
            print("3.修改学生信息")
            print("4.查找学生信息")
            try:
                choose = int(input("请输入序号："))
            except ValueError as e:
                print(e)
            if choose == 0:
                break
            elif choose == 1:
                self.Add()
            elif choose == 2:
                self.Delete()
            elif choose == 3:
                self.change()
            elif choose == 4:
                self.search()
            else:
                print("输入错误，请重新输入")

if __name__ == "__main__":
    System = system()
    System.Panel()