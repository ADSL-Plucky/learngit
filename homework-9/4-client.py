# -*- encoding: utf-8 -*-
'''
@File    :   4-client.py
@Time    :   2020/06/1 19:50:48
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
多人聊天器客户端
'''
import socket
import threading
import os
import get # 网上的稍微修改
class Client:
    def __init__(self, port=8080):  #ip = 1234
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        # self.ip = ip

    def connect(self):
        try:
            # addr = (self.ip,self.port)
            addr = (get.get_ip(), self.port)  # 只有自己一台电脑做测试时，可以直接用左边的
            self.sock.connect(addr)
            threads = [threading.Thread(target=self.Receive), threading.Thread(target=self.Send)]
            for t in threads:
                t.start()
        except Exception as e:
            print(e)

    def Receive(self):  #
        print("成功聊天室！现在可以接收消息并发送消息！\n")
        while True:
            try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
                response = self.sock.recv(1024)
                print(response.decode("utf-8"))
            except ConnectionResetError:
                print("服务器关闭，聊天已结束！")
                self.sock.close()
                break
        os._exit(0)

    def Send(self):
        print("输入消息按回车来发送")
        print("输入byebye来退出聊天")
        while True:
            msg = input()
            if msg == "byebye":
                print("聊天已经结束")
                self.sock.close()
                break
            self.sock.send(msg.encode("utf-8"))
        os._exit(0)

client = Client()
client.connect()
