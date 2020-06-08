# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/05/30 19:10:27
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
'''
import socket
def recieve():
    host = socket.gethostname()
    port = 12345
    server_addr = (host,port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server_addr)
    print("本机ip为：", server_addr[0])
    print("本机端口号：", server_addr[1])
    print("开始接收")
    while True:
        recv_data = s.recvfrom(1024)  # 1024表示本次接收的最大字节数
        # 打印显示接收到的数据
        print("{1}:{0}".format(recv_data[0].decode("gbk"), recv_data[1]))
        s.close()

if __name__ == '__main__':
    recieve()