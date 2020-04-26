# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/03/20 20:45:12
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
1 写一个程序，
读取键盘输入的任意行文字信息，
当输入空行时结束输入，将读入的字符串存于列表;
然后将列表里面的内容写入到文件input.txt中；
'''
Lines = []
Line = input("请输入任意行文字信息,当输入空行时结束输入：").strip()
while Line != '':
    Line = list(Line.split())
    Lines.append(Line)
    Line = input().strip()
try:
    with open('E:\Python\homework\homework-3\input.txt',"a",encoding="utf-8")as f:
        for Line in Lines:
            a = " ".join(Line)
            f.writelines(a + '\n')
except FileNotFoundError:
        print("The file was not found!")
finally:
    f.close()
