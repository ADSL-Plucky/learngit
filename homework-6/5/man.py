# -*- encoding: utf-8 -*-
'''
@File    :   man.py
@Time    :   2020/04/12 21:38:55
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
 人狗大战之人类：
 人的打击力为10;  初始化血为100; 
 人被咬一次,打击力降低2; 
'''
class Man:
    ATK = 10
    Blood = 100
    status = 'live'
    def __init__(self, name):
        self.name = name
    def Attacked(self,damage):
        if damage != 0:  #只有收到大于0的伤害才会降低攻击力
            if self.ATK >= 2:
                self.ATK -= 2
            else:
                self.ATK = 0
        self.Blood -= damage
        if self.Blood <= 0:
            self.status = 'dead'