# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2020/05/20 22:45:15
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
4 多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
'''
import time,random,threading
from queue import Queue

class Send(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data = queue
    def run(self):
        send_data = input("请输入发送的消息：")
        self.data.put(send_data)
        time.sleep(random.random())
        print("发送者%s发送完成！"%self.getName())

class Receive (threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data = queue
    def run(self):
        if not self.data.empty():
            receive_data = self.data.get()
            print("接收到的消息是：%s" % receive_data)
            time.sleep(random.random())
            print("接收者%s接收成功！"%self.getName())
if __name__=='__main__':
    queue = Queue()
    while True:
        send = Send('Sender',queue)
        receive = Receive('receiver',queue)
        send.start()
        send.join()
        receive.start()
        receive.join()
