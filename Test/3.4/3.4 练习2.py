# -*- encoding: utf-8 -*-
'''
@File    :   3.4 练习2.py
@Time    :   2020/03/04 08:26:34
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
#  提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,请计算应支付的总价,并打印提示输出;
weight = int(input("请输入苹果的斤数："))
price = int(input("请输入苹果每斤的价格："))
print("总价：",weight * price,"元")
print("总价：%d元"%(weight * price))
print("总价：{0:d}元".format(weight * price))