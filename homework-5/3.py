# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/04/9 15:47:12
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''
def deco(func):
    def wrapper():
        Data = []
        try:
            with open("account.txt", "r", encoding="utf-8") as f:
                for line in f.readlines():
                    user = line.strip('\n').split(',')
                    Data.append(user)
            f.close()
        except FileNotFoundError:
            print("The file was not found!")
        except IOError:
            print("Open fail")
        username = input("请输入账号:")
        password = input("请输入密码:")
        for i in range(len(Data)):
            if username == Data[i][0] and password == Data[i][1]:
                print("验证成功！开始调用函数...")
                func()
                break
        else:
            print("验证失败!无法调用函数")
    return wrapper
@deco
def func():
    print('函数被调用')

if __name__ == '__main__':
    func()