# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/03/20 21:00:13
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
'''
# import  math
# def Change(n):  #数字转中文
#     f = '0123456789'
#     num = '零一二三四五六七八九十'
#     unit = ['','十','百','千','万','十万','百万','千万','亿','十亿']
#     changed = ''
#     a = int(math.log10(n))
#     for i in f:
#         if a == i:
#             pass
#     else:
#         print('数字过大无法转换')
#     return changed

List = []
try:
    with open('E:\Python\homework\homework-3\input.txt','r',encoding='utf-8')as f:
        for Line in  f.readlines():
            Line = Line.strip('\n')
            List.append(Line)
except FileNotFoundError:
        print("The file was not found!")
except IOError:
    print("Open fail")
finally:
    f.close()
a = len(List)
for i in range(a):
    print('#第 {} 行：{}'.format(i+1,List[i]))