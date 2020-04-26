'''
@File    :   9.py
@Time    :   2020/03/06 23:00:02
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
from random import randint
num = randint(0,100)
i = 0
n = 5
print("开始游戏，你有{}次机会".format(n-i))
while(i<5):
    try:
        Num = int(input("请输入您所猜测的数字："))
        if Num == num:
            print("恭喜你猜对了！")
            break
        elif Num > num:
            print("您所猜的数字太大！")
        else:
            print("您所猜的数字太小！")
        i += 1
        print("你还有{}次机会".format(n-i))
    except ValueError as e:
        print("请输入整数!")
if i == 5:
    print("抱歉，您失败了!\n所要猜的数字为：",num)

