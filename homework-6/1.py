# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/04/12 19:38:35
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  
       打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''
class Dog():
    Dogslist = [
        {'color':'black','price':100,'number':5},
        {'color':'white','price':200,'number':5},
        {'color':'yellow','price':300,'number':5}
    ]
    def purchase(self,color):
        try:
            for dog in self.Dogslist:
                if dog['color'] == color:
                    print('颜色为{}的狗的价格为{}元'.format(dog['color'],dog['price']))
                    num = int(input('请输入需要购买的数量：'))
                    print('购买成功,总共花费{}元'.format(dog['price'] * num))
                    dog['number'] = dog['number'] + num
        except ValueError as e:
            print(e)
    def sell(self,color):
        try:
            for dog in self.Dogslist:
                if dog['color'] == color:
                    print('颜色为{}的狗的价格为{},剩余数量为{}只'.format(dog['color'], dog['price'],dog['number']))
                    num = int(input('客户，请您输入需要购买的数量：'))
                    if num > dog['number']:
                        print('抱歉，本店存货量不足，购买失败！')
                    else:
                        print('购买成功！已收到{}元'.format(dog['price'] * num))
                        dog['number'] = dog['number'] - num
        except ValueError as e:
            print(e)
    def Print(self):
        for dog in self.Dogslist:
            print("颜色为{}的狗的剩余数量为{}".format(dog['color'],dog['number']))

if __name__ == '__main__':
    dog = Dog()
    dog.purchase('black')
    dog.purchase('white')
    dog.purchase('yellow')
    dog.sell('black')
    dog.sell('white')
    dog.sell('yellow')
    dog.Print()