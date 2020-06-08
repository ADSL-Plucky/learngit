#!/usr/bin/python3 
#！--encoding=utf-8--
'''
练习:
题目1：匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
'''
'''
正则表达式中用到普通字符，需在前面加转义字符\
'''
import re 
def main():
    text = 'A'
    while text != 'B':
        text = input("请输入163邮箱地址：\n")  
        if re.match(r'[0-9a-zA-Z_]{4,20}@163\.com$',text):
            print('邮箱地址正确!')  
            break
        else:  
            print('请输入正确的邮箱地址！') 
        print('---------------------------------')
# 判断是不是本文件运行
if __name__ == "__main__":
     main()