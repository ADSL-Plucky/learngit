# -*- encoding: utf-8 -*-
'''
@File    :   man.py
@Time    :   2020/04/12 21:39:10
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
五  请写一个小游戏，人狗大站;  规则:
    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
        人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
    2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
    3   对战规则: 
     A  随机决定,谁先开始攻击; 
     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
'''
import random
import time
from dog import Dog
from man import Man
class Fight:
    def __init__(self):
        self.ManList = [Man('Tom'), Man('Jack')]
        self.DogList = [Dog('Alice'), Dog('Black'), Dog('Jerry')]
        self.Flag = 0
        self.ROUND = 1
    def start(self):
        self.flag = random.randint(0, 1)
        while True:
            print("-"*40)
            print("第{}回合开始！".format(self.ROUND))
            if self.flag == 0:
                print("人类进攻！")
                Attack = random.randint(0, len(self.ManList)-1)
                Target = random.randint(0, len(self.DogList) - 1)
                self.DogList[Target].Attacked(self.ManList[Attack].ATK)
                print("人类{}攻击了狗{}，{}收到{}点伤害,剩余{}点血".format(self.ManList[Attack].name,self.DogList[Target].name,
                      self.DogList[Target].name,self.ManList[Attack].ATK,self.DogList[Target].Blood))
                if self.DogList[Target].status == 'dead':
                    print("狗{}已死亡".format(self.DogList[Target].name))
                    del self.DogList[Target]
                time.sleep(0.5)
                self.flag = 1
            else:
                print("狗进攻！")
                Attack = random.randint(0, len(self.DogList) - 1)
                Target = random.randint(0, len(self.ManList) - 1)
                self.ManList[Target].Attacked(self.DogList[Attack].ATK)
                print("狗{}攻击了人类{}，{}收到{}点伤害,剩余{}点血".format(self.DogList[Attack].name, self.ManList[Target].name,
                      self.ManList[Target].name, self.DogList[Attack].ATK,self.ManList[Target].Blood))
                if self.ManList[Target].status == 'dead':
                    print("人{}已死亡".format(self.ManList[Target].name))
                    del self.ManList[Target]

                time.sleep(0.1)
                self.flag = 0
            if len(self.ManList) == 0:
                return 1
            elif len(self.DogList) == 0:
                return 0
            else:
                self.ROUND += 1
F1 = Fight()
if F1.start() == 1:
    print("狗获得胜利！")
else:
    print("人获得了胜利！")