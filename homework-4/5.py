# -*- encoding: utf-8 -*-
'''
@File    :   5.py
@Time    :   2020/03/28 22:20:23
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
5  通过Python来模拟实现一个txt文件的拷贝过程;
'''
def Copy(copyfile,pastefile):
    try:
        f1 = open(copyfile, "r")
        f2 = open(pastefile, "w")
        for line in f1.readlines():
            f2.write(line)
        f1.close()
        f2.close()
    except OSError:
        print("文件路径错误")
copyfile = input("请输入要复制的txt文件位置(最好输入绝对路径):")
pastefile = input("请输入该文件粘贴到的位置？(最好输入绝对路径):")
Copy(copyfile,pastefile)