'''
如在汉诺塔游戏中，我们希望将塔A上的n个盘子，通过塔B移动到塔C，则对于任意输入的n，给出移动的步骤。
输入格式:
一个正整数n
输出格式：
移动的步骤
输入样例：
2
输出样例：
Move 1 from A to B
Move 2 from A to C
Move 1 from B to C
'''
def Hanoi(n,a,b,c):
    f = 0
    if(n == 1):
        print("Move %s from %s To %s"%(n,a,c))
    else:
        Hanoi(n-1,a,c,b)
        print("Move {} from {} to {}".format(n,a,c))
        Hanoi(n-1,b,a,c)
f = 0
n = int(input())
Hanoi(n,'A','B','C')
