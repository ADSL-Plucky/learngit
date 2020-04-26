# -*- encoding: utf-8 -*-
'''
@File    :   7.py
@Time    :   2020/03/29 15:30:25
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
7 使用python代码统计一个文件夹中所有文件的总大小
'''
import os
def GetSzie(Path):
    Size = 0
    Tuples = tuple(os.walk(Path))
    for root,dirs,files in Tuples:
        for name in files:
            Size = Size + os.path.getsize(os.path.join(root,name))
    return Size
Path = input("请输入统计大小的文件夹的绝对路径：")
Size = GetSzie(Path)
unit = ['B','KB','MB','GB','TB']
n = 0
AboutSize = Size
while AboutSize > 1024:
    AboutSize = AboutSize / 1024
    n += 1
print('文件总大小为{:.2f}{}({:,d}字节)'.format(AboutSize,unit[n],Size))

