# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/05/20 19:45:31
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''


'''
1  有100个同学的分数：数据请用随机函数生成；
     A 利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；
'''
import random
import time
from multiprocessing import Pool
from multiprocessing import Process
import os

class SubProcess(Process):
    def __init__(self,interval,name=''):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name
    def run(self):
        for i in range(0,20):
            print("子进程(%s)开始运行，学生成绩%d" % (os.getpid(), random.randint(0, 100)))
            time.sleep(self.interval)
def score(name):
    print("子进程(%s)开始运行，学生成绩%d" % (os.getpid(), random.randint(0, 100)))
    time.sleep(1)
if __name__ == '__main__':
    # 多线程
    # p1 = SubProcess(interval=1)
    # p2 = SubProcess(interval=2,name='b')
    # p3 = SubProcess(interval=3,name='c')
    # p4 = SubProcess(interval=2,name='d')
    # p5 = SubProcess(interval=1,name='e')
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # 线程池
    pool = Pool(9)
    for i in range(100):
        pool.apply_async(score,args=(i,))
    print("----start-----")
    pool.close()
    pool.join()
    print("----close-----")