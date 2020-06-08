# -*- encoding: utf-8 -*-
'''
@File    :   4-server.py
@Time    :   2020/06/1 19:50:06
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
多人聊天室服务器
'''
import socket
import get  # 网上的稍微修改
import threading
import os

class Sever:
    def __init__(self,port=8080):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.users = {}

    def start(self):
        '''
        启动服务器
        :return:
        '''
        try:
            self.sock.bind((get.get_ip(),self.port))
        except Exception as e:
            print(e)
        self.sock.listen(5)
        print("服务器已开启，当前ip为：{}，所占用端口为：{}".format(get.get_ip(), self.port))
        print("可以随时在空白处输入stop sever并回车，来关闭服务器")

        # 此处不用线程启动方法的话会卡在该方法的死循环中，无法关闭服务器
        threading.Thread(target=self.accept_member, args=()).start()

    def accept_member(self):
        '''
        接收新成员
        :return:
        '''
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            print("欢迎用户{}加入聊天室！现在聊天室有{}位用户".format(addr, len(self.users)))
            threading.Thread(target=self.recv_send, args=(s, addr)).start()

    def recv_send(self, sock, addr):
        '''
        接收用户信息
        :param sock:用户的socket
        :param addr:用户的ip以及端口
        :return:
        '''
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("utf-8")
                msg = "{}  来自用户{}的消息：{}".format(get.get_time(), addr, response)

                for client in self.users.values():
                    client.send(msg.encode("utf-8"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

    def close_sever(self):
        '''
        当服务器关闭时执行，关闭套接字并结束线程
        :return:
        '''
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    sever = Sever()
    sever.start()
    while True:
        cmd = input()
        if cmd == "stop sever":
            # print(cmd)
            sever.close_sever()
            break
        else:
            print("输入命令无效，请重新输入！")
