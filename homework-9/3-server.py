# -*- encoding: utf-8 -*-
'''
@File    :   3-server.py
@Time    :   2020/05/30 20:40:36
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
s.bind(server_addr)
data,addr = s.recvfrom(1024)
while data != 'byebye':
    print("收到消息：%s" % data)
    send_data = input("发送消息:")
    s.sendto(send_data.encode(), addr)
    if send_data == 'byebye':
        break
    data, addr = s.recvfrom(1024)
s.close()
