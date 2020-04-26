# -*- encoding: utf-8 -*-
'''
@File    :   dog.py
@Time    :   2020/04/12 21:28:10
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
 人狗大战之狗类：
 狗的攻击力为 15; 初始化血为80;
 狗被打一次,攻击力降低3
'''
class Dog:
    ATK = 15
    Blood = 80
    status = 'live'
    def __init__(self, name):
        self.name = name
    def Attacked(self,damage):
        if damage != 0:  #只有收到大于0的伤害才会降低攻击力
            if self.ATK >= 3:
                self.ATK -= 3
            else:
                self.ATK = 0
        self.Blood -= damage
        if self.Blood <= 0:
            self.status = 'dead'
