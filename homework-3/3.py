# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/03/20 21:25:53
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
'''
transcript = []
try:
    with open('E:\Python\homework\homework-3\Transcript.txt','r')as f:
        for line in  f.readlines():
            line = line.strip('\n')
            s = line.split(" ")
            transcript.append(s)
except FileNotFoundError:
    print("The file was not found!")
except IOError:
    print("Open fail")
finally:
    f.close()

transcript.sort(key = lambda a:int(a[2]),reverse=True)
print('学号         姓名  Python课程分数')
for line in transcript:
    print(" ".join(line))
