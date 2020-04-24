'''
随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
    A---成绩>=90;
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
'''
from random import randint
def Judge(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'
name = [x for x in range(1,21)]
score = [randint(0,100) for _ in range(20)]
student = [[name[i],score[i],Judge(score[i])] for i in range(20)]
for i in range(20):
    print(student[i])
