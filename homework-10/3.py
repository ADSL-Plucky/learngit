# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/06/7 21:45:30
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3  对2中的表结构，用SQLAchemy模块来实现同样的操作；
'''
from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:password@localhost:3306/learn')
# 创建对象的基类:
Base = declarative_base()

class GuestBook(Base):
    # 表的名字:
    __tablename__ = 'guestbook'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    message = Column(String(60))
    name = Column(String(20))
    time = Column(String(30))
    is_delete = Column(Integer)

try:
    GuestBook.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新GuestBook对象:
    new1 = GuestBook(id='10', message='time is fast', name='Alice', time='2020/6/1 03:13:12', is_delete=0)
    new2 = GuestBook(id='11', message='word is big', name='Bob', time='2020/6/1 03:19:12', is_delete=0)
    new3 = GuestBook(id='12', message='i am happy', name='Cindy', time='2020/6/1 03:20:12', is_delete=0)

    # 添加到session:
    session.add(new1)
    session.add(new2)
    session.add(new3)

    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
except Exception as e:
    print(e)