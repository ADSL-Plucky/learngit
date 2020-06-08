# -*- encoding: utf-8 -*-
'''
@File    :   excese.py
@Time    :   2020/05/2 19:00:18
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
爬虫基本操作练习
'''
# import requests
# response = requests.get('http://ww.baidu.com')
#
# data = {'word':'hello'}  #表单参数
# response = requests.post('http://httpbin.org/post',data = data)
#
# print("状态码",response.status_code)
# print('请求地址',response.url)
# print('头部信息',response.headers)
# print('cookie信息',response.cookies)
# print('文本源码',response.text)
# print('字节流源码',response.content)



# import requests
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url = 'http://www.whatismyip.com/'
# response = requests.get(url,headers = headers)
# print(response.content.decode('utf-8'))



# import requests
# #导入3种网络请求模块中的异常类
# from requests.exceptions import ReadTimeout,HTTPError,RequestException
# #循环发送请求，另反应服务器超时
# for  a in range(0,50):
#     try:
#         response = requests.get('http://www.whatismyip.com/', timeout=1)
#         print(response.status_code)
#     except ReadTimeout :
#         print("超时")
#     except HTTPError :
#         print("HTTP错误")
#     except RequestException :
#         print("请求异常")



# import requests
# #设置代理IP
# proxy = {'HTTP':'223.82.106.253:3128',
#          'HTTPS':'119.84.112.139:80'}
# response = requests.get('http://www.baidu.com',proxies = proxy)
# print(response.content.decode('utf-8'))



# import requests
# from bs4 import BeautifulSoup
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc,features='lxml')
# print(soup)
# print('html代码的tile',soup.title)

# soup = BeautifulSoup(open('index.html'),features='lxml')
# print(soup.prettify())



# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://news.baidu.com/')
# soup = BeautifulSoup(response.text,features='lxml')
# print(soup.find('title').text)

