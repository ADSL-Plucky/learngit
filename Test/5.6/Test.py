'''
@File    :   Text.py
@Time    :   2020/05/06 14:37:43
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
练习二：
   创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
   完成对这个表记录的增，删，改，查询；
   用PyMySQL驱动方式
'''
import pymysql

try:
    db = pymysql.connect(host='localhost', user='root', passwd="password", db='test')
    cursor = db.cursor()
    # 创建表
    cursor.execute('DROP TABLE IF EXISTS TMessage')
    sqlQuery = "CREATE TABLE TMessage(Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL," \
               "Theme VARCHAR(255) NOT NULL ,Name VARCHAR(255) NOT NULL ,Time VARCHAR(255) NOT NULL)"
    cursor.execute(sqlQuery)
    # 添加数据
    sql1 = "INSERT INTO TMessage (Id, Theme,Name,Time) VALUES (%s,%s,%s,%s)"
    val1 = [
        (1,'学习','张三','2020-5-6'),
        (2,'学习','李四','2020-5-6'),
        (3,'学习','王五','2020-5-6')
    ]
    # val1 = (1,'学习','张三','2020-5-6')
    # val2 = (2,'学习','李四','2020-5-6')
    cursor.executemany(sql1, val1)
    # cursor.execute(sql1, val2)
    db.commit()
    print("添加成功！")

    # 删除数据
    sql2 = "DELETE FROM TMessage where Name=%s"
    val2 = ('张三')
    cursor.execute(sql2, val2)
    db.commit()
    print("删除成功！")

    # 更改数据
    sql3 = "UPDATE TMessage SET Name=%s WHERE Name=%s"
    val3 = ('赵六', '李四')
    cursor.execute(sql3, val3)
    db.commit()
    print('更新成功！')

    # 查询数据
    cursor.execute("SELECT * FROM TMessage")
    results = cursor.fetchall()
    for row in results:
        Id = row[0]
        Theme = row[1]
        Name = row[2]
        Time = row[3]
        print('Id:%s,Theme:%s,Name:%s,Time:%s' % (Id, Theme, Name,Time))

    cursor.close()
    db.close()
except pymysql.Error as e:
    print('出错：',e)