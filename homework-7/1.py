# -*- encoding: utf-8 -*-
'''
@File    :   1.py
@Time    :   2020/05/2 20:43:32
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；
'''
import re
if __name__ == '__main__':
    pattern = r'http?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    try:
        with open('webspiderUrl.txt', 'r',encoding='utf-8') as f1:
            with open('url.txt', 'w',encoding='utf-8') as f2:
                content = f1.readlines()
                for line in content:
                    urls = re.findall(pattern, line)
                    for url in urls:
                        f2.write(url + '  ')
                    f2.write('\n')
    except (FileNotFoundError,AttributeError,OSError) as e1:
        print("错误：",e1)
    finally:
        f1.close()
        f2.close()
