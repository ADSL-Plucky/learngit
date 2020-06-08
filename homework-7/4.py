# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2020/05/6 20:30:22
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
4 爬取这个网址上http://www.python3.vip/doc/prac/python/0001/，所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；
'''
from bs4 import BeautifulSoup
import requests

url = 'http://www.python3.vip/doc/prac/python/0001/'
# 伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
}

# 发送请求
r = requests.get(url, headers=headers).content.decode('utf-8')
# print(r)

# 解析html文档
soup = BeautifulSoup(r, 'html.parser')  # 这里用lxml会出错
# print(type(soup))

# 查找每个练习的a链接href属性获取对应的链接地址
re_a = soup.find(id='content').ul.find_all('a')  # 返回的是100个a标签的列表

# 创建一个列表保存url
list = []
for i in re_a:
    list.append(i.attrs['href'])
# print(list)


"""
	2、根据获取的每个练习的链接地址来请求每个练习获得页面内容
"""
# 遍历列表100次
data = []
for x in list:
    dict = {}
    # 请求详细页面
    test = requests.get('http://www.runoob.com' + x, headers=headers).content.decode('utf-8')
    # print(test)

    # 解析html文档
    soup_test = BeautifulSoup(test, 'html.parser')
    # print(type(soup_test))

    # 查找练习内容
    # 查找标题
    dict['title'] = soup_test.find(id='content').h1.text

    # 查找题目
    dict['tm'] = soup_test.find(id='content').find_all('p')[1].text
    # print(title)

    # 查找程序分析
    dict['cxfx'] = soup_test.find(id='content').find_all('p')[2].text
    # print(cxfx)

    # 程序源代码
    try:
        dict['code'] = soup_test.find(class_="hl-main").text
    except Exception as e:
        dict['code'] = soup_test.find('pre').text
    # print(code)
    # print(dict)

    # 保存文件1
    # 	data.append(dict)
    #
    # import pandas as pd
    # datas = pd.DataFrame(data)
    # datas.to_csv('py-100.csv')

    # 保存文件2
    with open('100-py.csv', 'a+', encoding='utf-8') as file:
        file.write(dict['title'] + '\n')
        file.write(dict['tm'] + '\n')
        file.write(dict['cxfx'] + '\n')
        file.write(dict['code'] + '\n')
        file.write('*' * 50 + '\n')
        file.write('\n')
