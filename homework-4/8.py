# -*- encoding: utf-8 -*-
'''
@File    :   8.py
@Time    :   2020/03/29 15:52:32
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
8 京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，每行随机为
172.25.254.1---172.25.254.254之间的ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
'''
from random import randint
import os
def spanned_file(filename):
    #生成文件
    try:
        with open(filename, 'w', encoding = 'utf-8') as f:
            for i in range(1200):
                end = randint(1,255)
                ip = '172.25.254.' + str(end)
                f.writelines(ip + '\n')
        f.close()
    except OSError as e:
        print(e)

def read_file(filename):
    #读取文件，统计频率
    try:
        with open(filename, 'r', encoding = 'utf-8') as f:
            List = f.readlines()
            for i in range(len(List)):
                List[i] = List[i].strip('\n')
        f.close()
        ip = ['172.25.254.' + str(end) for end in range(1,255)]
        countlist = [(num,List.count(num)) for num in ip]
        countlist.sort(key=lambda i:(i[1],i[0]), reverse=True)
        return countlist[:10]
        #
        # Dic = {}
        # for i in range(len(List)):
        #     if (List[i] in Dic):
        #         Dic[List[i]] = Dic[List[i]] + 1
        #     else:
        #         Dic[List[i]] = 1
        # sortedDic = sorted(zip(Dic.values(), Dic.keys()), reverse=True)
        # return sortedDic[:10]
    except FileNotFoundError as e:
        print(e)

spanned_file('ip.txt')
countList = read_file('ip.txt')
for i in range(len(countList)):
    print(countList[i])
