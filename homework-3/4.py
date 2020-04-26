# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2020/03/20 21:45:53
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
4 题目要求：
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg.
'''
import os
import shutil
def add(path):  #添加文件
    name = ['a.png', 'b.png', 'c.png', 'd.png', 'e.png', 'f.png', 'g.png', 'h.png', 'i.png', 'j.png']
    try:
        for i in range(10):
            with open(os.path.join(path, name[i]), 'w')as f:
                continue
    except Exception:
        print("Open fail")
    finally:
        f.close()

def change(path,before,after):  #重命名
    try:
        if os.path.exists(path):
            Files = []
            for root,dirs,files in os.walk(path):
                for name in files:
                    Files.append(name)
            Filename = [os.path.splitext(filename)[0] for filename in Files]
            for i in Filename:
                oldname = os.path.join(path,i + before)
                newname = os.path.join(path,i + after)
                os.rename(oldname,newname)
    except Exception:
        print("重命名失败")
    else:
        print("重命名成功")

path = os.getcwd()
if not os.path.exists('img'):
    os.mkdir("img")
    print('初次创建目录img成功！')
else:              #重新创建
    shutil.rmtree('img')
    os.mkdir('img')
    print('重新创建目录img成功！')
path = os.path.join(path, 'img')
add(path)
change(path,'.png','.jpg')
