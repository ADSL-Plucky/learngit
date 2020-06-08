# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/05/20 20:35:31
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块
   def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"
'''
import requests
from multiprocessing import Pool
import time
import os

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
def CheckURL(url):
    try:
        r = requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        print("子进程(%s)访问%s成功" %(os.getpid(), url))
        time.sleep(1)
        return True
    except:
        print("子进程(%s)访问%s超时" %(os.getpid(), url))


if __name__ == '__main__':
    with open(r'.\url_data.txt', 'r') as f:
        urls = f.read().splitlines()
    pool = Pool(30)
    for url in urls:
        pool.apply_async(CheckURL, args=(url,))
    print("----start-----")
    pool.close()
    pool.join()
    print("----close-----")