# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/06/3 19:10:13
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
1 数据库查询练习：
   针对我们给大家的2张表（学生表和班级表），做以下查询；（查询脚本放在一个文件中，创建一个SQL文件夹，放到这个里面，最有提交到代码仓库）
① 查询所有男生的姓名，年龄，所在班级名称；
② 查询所有查询编号小于4或没被删除的学生；
③ 查询姓黄并且“名”是一个字的学生；
④ 查询编号是1或3或8的学生
⑤ 查询编号为3至8的学生
⑥ 查询未删除男生信息，按年龄降序
⑦  查询女生的总数
⑧  查询学生的平均年龄
⑨ 分别统计性别为男/女的人年龄平均值
⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
    | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                               |
	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                      |
	| 中性   | 金星                                                       |
	| 保密   | 凤姐                                                       |
'''

import pymysql
import os
class DataBase:
    def __init__(self,host = 'localhost',user = 'root',password = 'password',db = 'learn'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.database = pymysql.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.database.cursor()

    def interface(self):
        '''
        界面
        :return:
        '''
        os.system('cls')
        print("                            数据库查询                                       ")
        print("----------------------------------------------------------------------------")
        print("0.退出")
        print("1.查询所有男生的姓名，年龄，所在班级名称")
        print("2.查询所有查询编号小于4或没被删除的学生")
        print("3.查询姓黄并且“名”是一个字的学生")
        print("4.查询编号是1或3或8的学生")
        print("5.查询编号为3至8的学生")
        print("6.查询未删除男生信息，按年龄降序")
        print("7.查询女生的总数")
        print("8.查询学生的平均年龄")
        print("9.分别统计性别为男/女的人年龄平均值")
        print("10.按照性别来进行人员分组如下显示（group by + group_concat()）")
        print("----------------------------------------------------------------------------")
        num = 1
        while num != 0:
            try:
                num = int(input("请输入您想要进行的操作(0 - 10)："))
                if num in range(0, 11):
                    self.execute(num)
                else:
                    raise Exception
            except Exception:
                print("您输入的操作数有误，请重新输入！")
        print("退出数据库")
        self.database.close()

    def execute(self,n):
        '''
        查询操作
        :return:
        '''
        print("您要进行的是操作{}！".format(n))
        if n == 0:
            return
        elif n == 1:
            sql = 'select name,age,cls_id from students where gender = "男"'
        elif n == 2:
            sql = 'select * from students where id < 4 or is_delete = 0'
        elif n == 3:
            sql = 'select * from students where name like "黄%"'
        elif n == 4:
            sql = 'select * from students where id = 1 or id = 3 or id = 8'
        elif n == 5:
            sql = 'select * from students where id between 3 and 8'
        elif n == 6:
            sql = 'select * from students where gender = "男" and is_delete = 0 order by age DESC'
        elif n == 7:
            sql = 'select count(*) from students where gender = "女"'
        elif n == 8:
            sql = 'select avg(age) as avgage from students'
        elif n == 9:
            sql = 'select avg(age) as avgage,gender from students group by gender'
        elif n == 10:
            sql =  'select gender,group_concat(name) from students group by gender'
        self.show(sql,n)

    def show(self,sql,n):
        '''
        查询结果显示
        :param sql:
        :param n:
        :return:
        '''
        def Print(results):
            for result in results:
                print("id = {} , name = {} , age = {} , height = {} , gender = {} , cls_id = {}".format
                      (result[0], result[1], result[2], result[3], result[4], result[5]))
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        if n == 1:
            print('男生的姓名，年龄，所在班级名称为:')
            for result in results:
                print("name = {} , age = {} , cls_id = {}".format(result[0] , result[1] , result[2]))
        elif n == 2:
            print('查询所有查询编号小于4或没被删除的学生为:')
            Print(results)
        elif n == 3:
            print('查询姓黄并且“名”是一个字的学生为:')
            Print(results)
        elif n == 4:
            print('查询编号是1或3或8的学生为:')
            Print(results)
        elif n == 5:
            print('查询编号为3至8的学生为:')
            Print(results)
        elif n == 6:
            print('查询未删除男生信息，按年龄降序:')
            Print(results)
        elif n == 7:
            print('查询女生的总数:')
            print(results[0][0])
        elif n == 8:
            print('查询学生的平均年龄:')
            print(''+results)
        elif n == 9:
            print('分别统计性别为男/女的人年龄平均值:')
            n = 0
            for result in results:
                if n in (0,1):
                    print('{}生的平均年龄：{}'.format(result[1],result[0]))
                    n += 1
        elif n == 10:
            print('按照性别来进行人员分组如下显示:')
            # print(results)
            for result in results:
                print('| {:<4} | {:<40} |'.format(result[0], result[1]))

if __name__ == '__main__':
    database = DataBase()
    database.interface()