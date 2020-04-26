# -*- encoding: utf-8 -*-
'''
@File    :   6.py
@Time    :   2020/03/28 22:35:12
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小
'''
import os
import datetime

FilePath = input("请给定一个文件夹：(绝对路径):")
def show(file):
    if os.path.isfile(file):
        print("{0:30} {1:29} {2:10} {3:10d}kb".format(os.path.basename(file),
              datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y/%b/%d %H:%M:%S'), "文件", os.path.getsize(file)))
    elif os.path.isdir(file):
        print("{0:30} {1:29} {2:10}".format(os.path.basename(file),
              datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y/%b/%d %H:%M:%S'), "文件夹"))

print("{0:28} {1:28} {2:12} {3:10}".format("名称", "日期", "类型", "大小"))

list1 = os.listdir(FilePath)
for file in list1:
    show(os.path.join(FilePath, file))

#没搞懂用os.walk提取第一个目录为啥文件,只能找到文件夹找不到= =,绝对路径显示一样
# Tuples = tuple(os.walk(FilePath))
# for root,dirs,files in Tuples:
#     for name in dirs:
#         print(os.path.join(root,name),'文件夹')
#     for name in files:
#         print(os.path.join(root,name),'文件')