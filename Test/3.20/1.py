'''
@File    :   1.py
@Time    :   2020/03/25 08:40:33
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
 将一个文件夹下的某个文件,拷贝到另外一个文件夹下去;
 提示:
写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个#参数是目标位置，将源文件copy到目标位置。
# 还需要判断一下这个文件之前是否存在
提示2:  读源文件的内容;
        创建目标文件;
        读到的内容,再写入到目标文件
路径例如：
path1 = r'D:\a\test.txt'
path2 = r'D:\b\'
'''
import os
def copy():
    f1 = open(r'E:\untitled\网课作业\names.txt', "r")
    f2 = open(r'E:\untitled\3.20\names.txt',"w")
    for line in f1.readlines():
        f2.write(line)
    f1.close()
    f2.close()
copy()