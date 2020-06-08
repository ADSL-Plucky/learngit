# -*- encoding: utf-8 -*-
'''
@File    :   3-client.py
@Time    :   2020/05/30 20:41:08
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
server_addr = (host, port)
data = ''
while data != 'byebye':
    data = input("请发送消息：")
    s.sendto(data.encode(), server_addr)
    print(s.recv(1024).decode())
    if data == 'byebye':
        break
s.close()