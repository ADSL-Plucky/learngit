# -*- encoding: utf-8 -*-
'''
@File    :   2.py
@Time    :   2020/05/2 21:02:12
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
'''
# here put the import lib

#  给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库
from bs4 import BeautifulSoup
import requests
import re
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from random import randint

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#代理IP，失效了请换一个或者删了不用
proxy = {'HTTP': '223.82.106.253:3128',
         'HTTPS': '119.84.112.139:80'}

def getURL(file):
    try:
        with open(file, 'r',encoding='utf-8') as f:
            return f.readlines()
    except (FileNotFoundError, AttributeError, OSError) as e1:
        print("错误：", e1)
    finally:
        f.close()

if __name__ == '__main__':
    urls = getURL('url.txt')
    # print(urls)
    n = 0
    num = 0
    URL_compony = []
    while num < 100:
        flag = 0
        try:
            url = urls[n].strip()
            # print(url)
            n += 1
            response = requests.get(url=url, headers=headers, proxies=proxy,timeout = 2)
            text = response.content
        except ReadTimeout:
            print("超时")
        except HTTPError:
            print("HTTP错误")
        except RequestException:
            print("请求异常")
        else:
            soup = BeautifulSoup(text, features='lxml')
            aList = soup.find_all('a')
            for a in aList:
                if re.search(r'(公司简介)|(产品展示)|(企业发展)|(发展历史)|(企业概况)|(企业介绍)|(联系我们)', a.text):
                    try:
                        URL_compony.append(url + a.attrs['href'] + '        ')
                        flag = 1
                    except KeyError as e:
                        print(e)
            if flag == 0:
                URL_compony.append('该网站没有需要爬取的信息\n')
            else:
                URL_compony.append('\n')
            # print(URL_compony)
            num += 1
            print(num)
    try:
        with open(r"URL_Company.txt", 'w', encoding='utf-8') as f:
            f.writelines(URL_compony)
    except (FileNotFoundError, AttributeError, OSError) as e:
        print("错误：", e)
    finally:
        f.close()



