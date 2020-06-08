# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/05/4 19:10:12
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3  给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
注意：
获取的音频网址前面需要加上 前缀 http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
MP3文件中有空格字符，组成下载网址时，需要进行url编码，否则空格会被当成命令行分隔符。参考代码如下所示
>>> from urllib.parse import quote
>>> quote('2019-04-13 NEWSworthy Clips.mp3')
'2019-04-13%20NEWSworthy%20Clips.mp3'
'''
import requests
import re
import wget
import os
url = 'http://www.listeningexpress.com/studioclassroom/ad/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#代理IP，失效了请换一个或者删了不用
proxy = {'HTTP': '223.82.106.253:3128',
         'HTTPS': '119.84.112.139:80'}
if not os.path.exists("download"):
  os.mkdir("download")
download = os.path.join(os.path.abspath(os.getcwd()),"download")

response = requests.get(url=url,headers=headers,proxies=proxy).content.decode('GBK') #  'utf-8' codec can't decode byte 0xbf in position 89: invalid start byte
ret = re.finditer(r'sc-[a-zA-Z0-9 -.]+\.mp3', response)

for r in ret:
    BufferUrl = url + r.group() # 尝试过写quote，但反而会报错
    print(url)
    filePath = r'.\songs\%s'%r.group()
    wget.download(BufferUrl, out = download)

