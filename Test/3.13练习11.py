'''
@File    :   3.13练习11.py
@Time    :   2020/03/13 08:32:02
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 将我们作业当中,  10个同同学成绩排序的问题,用 sort函数来实现;  
# 这个10个同学的成绩,用列表存放, 列表里面每个元素是一个元组;
from random import randint
gradedict = [
    ('伊一',58),
    ('小二',76),
    ('张三',85),
    ('李四',69),
    ('王五',63),
    ('彩六',93),
    ('红旗',96),
    ('王八',88),
    ('酒九',35),
    ('时实',100)
]
gradedict.sort(key = lambda x : x[1])
for i in range(len(gradedict)):
    print(gradedict[i])