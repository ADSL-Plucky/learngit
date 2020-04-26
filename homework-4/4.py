# -*- encoding: utf-8 -*-
'''
@File    :   4.py
@Time    :   2020/03/28 22:00:01
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
4  (继续上面的练习) 模拟用户登录:q
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
     系统提示,请输入登录同学姓名, 
     正确后,请输入账号, 
     正确后,提示请输入密码（输入明文）;  
     如果都正确,打印提示, 您登录成功(失败);
'''
import hashlib
def get_ret(s):
    md5 = hashlib.md5()
    md5.update(s.encode("utf-8"))
    ret = md5.hexdigest()
    return ret
def Login(Data):
    name = input("请输入姓名:")
    for i in range(len(Data)):
        if name == Data[i][0]:
            account = input("请输入账号:")
            if account == Data[i][1]:
                password = input("请输入密码:")
                if get_ret(password) == Data[i][2]:
                    print("登录成功!")
                    break
    else:
        print("登录失败!")
Data = []
with open("account.txt","r",encoding="utf-8") as f:
    for line in f.readlines():
        user = line.strip('\n').split(',')
        Data.append(user)
f.close()
Login(Data)
