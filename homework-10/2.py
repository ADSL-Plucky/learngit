# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/06/3 21:30:35
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
'''
import pymysql
import os
import datetime
class DataBase:
    def __init__(self,host = 'localhost',user = 'root',password = 'password',db = 'learn'):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.database = pymysql.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.database.cursor()

    def Send_Sql(self,sql):
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return self.cursor
        except Exception as e:
            print(e)
            print("SQL语句执行失败！")
            self.database.rollback()

    def interface(self):
        '''
        界面
        :return:
        '''
        os.system('cls')
        print("                  留言板                                   ")
        print("----------------------------------------------------------")
        print("0.退出")
        print("1.增加留言信息")
        print("2.删除留言信息")
        print("3.修改留言信息")
        print("4.查询留言信息")
        print("5.输出全部留言")
        print("----------------------------------------------------------")
        num = 1
        while num != 0:
            try:
                num = int(input("请输入您想要进行的操作(0 - 5)："))
                if num in range(0, 6):
                    self.execute(num)
                else:
                    raise Exception
            except Exception:
                print("您输入的操作数有误，请重新输入！")
        print("退出数据库")
        self.database.close()

    def execute(self, n):
        '''
        查询操作
        :return:
        '''
        print("您要进行的是操作{}！".format(n))
        if n == 0:
            return
        elif n == 1:
            message = input("请输入留言：")
            name = input("请输入留言人：")
            time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            sql = 'insert into guestbook(message,name,time) values (\"%s\",\"%s\",\"%s\")'%(str(message),str(name),str(time))
            self.Send_Sql(sql)
        elif n == 2:
            delete_id = input("请输入您要删除的留言id：")
            sql = 'update guestbook set is_delete = 1 where id = \"%d\"'%(int(delete_id))
            self.Send_Sql(sql)
        elif n == 3:
            id = input("请输入您要修改的留言id：")
            fields = input("请输入您要修改的字段：")
            value = input("请输入您要修改的值：")
            sql = 'update guestbook set {} = \"{}\" WHERE id={}'.format(fields, value, id)
            self.Send_Sql(sql)
        elif n == 4:
            id = input("请输入您要查询的id：")
            sql = 'select * from guestbook where id = \"%d\" and is_delete = 0'%(int(id))
            # sql = """SELECT * FROM guestbook WHERE id = \"{}\" AND is_delete = 0""".format(id)
            res = self.Send_Sql(sql)
            if res is not None:
                if res.rowcount == 0:
                    print("查询结果为空！")
                else:
                    print("{:<5}{:60}{:^10}{:>30}".format("id", "message", "name", "time"))
                    for r in res:
                        print("{:<5}{:60}{:^10}{:>30}".format(r[0], r[1], r[2], r[3]))
        elif n == 5:
            sql = 'select * from guestbook'
            res = self.Send_Sql(sql)
            if res is not None:
                if res.rowcount == 0:
                    print("留言板没有留言")
                else:
                    print("{:<5}{:60}{:^10}{:>30}{:>10}".format("id", "message", "name", "time", "is_delete"))
                    for r in res:
                        print("{:<5}{:60}{:^10}{:>30}{:>10}".format(r[0], r[1], r[2], r[3], r[4]))
        results = self.cursor.fetchall()

if __name__ == '__main__':
    database = DataBase()
    database.interface()