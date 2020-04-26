# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/04/12 20:36:18
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
三、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
'''
class dictclass:
    mydict = {}
    def __init__(self, mydict):
        self.mydict = mydict

    def del_dict(self, key):
        del self.mydict[key]

    def get_dict(self, key):
        if key in self.mydict:
            return self.mydict[key]
        else:
            return "not found"

    def get_key(self):
        return [key for key in self.mydict.keys()]

    def update_dict(self, dict):
        for key,value in dict.items():
          self.mydict[key] = value
        return [value for value in self.mydict.values()]


if __name__ == "__main__":
    Data =  {'A':1,'B':2,'C':3}
    Dict = dictclass(Data)
    print('生成Dict后，里面的数据：',Dict.mydict)
    Dict.del_dict('A')
    print('删除键A后里面的数据：',Dict.mydict)
    print('键B对应的值：',Dict.get_dict('B'))
    print('键A对应的值：',Dict.get_dict('A'))
    print('Dict中键组成的列表：',Dict.get_key())
    print('所返回的合并后字典的values组成的列表',Dict.update_dict({'D': 4}))
    print('合并新字典后后里面的数据：', Dict.mydict)
