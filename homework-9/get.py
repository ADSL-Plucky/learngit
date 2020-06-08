# -*- encoding: utf-8 -*-
'''
@File    :   get.py
@Time    :   2020/06/1 19:50:30
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
import socket
import datetime

def get_ip():
    # 获取IP
    return socket.gethostbyname(socket.gethostname())

def get_time():
    """
    获取时间
    格式：年/月/日 时:分:秒
    """
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
