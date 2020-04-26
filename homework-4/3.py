# -*- encoding: utf-8 -*-
'''
@File    :   3.py
@Time    :   2020/03/28 21:40:15
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
'''
import hashlib
def encrypted_storage(Data):
    with open("account.txt","w",encoding="utf-8") as f:
        for data in Data:
            md5 = hashlib.md5()
            md5.update(str(data[2]).encode("utf-8"))
            f.write("{},{},{}\n".format(data[0],data[1],md5.hexdigest()))
    f.close()
Data = []
for i in range(5):
    print("第{}位同学".format(i+1))
    name = input('请输入姓名:')
    username  = input("请输入账号:")
    password = input("请输入密码:")
    Data.append((name,username,password))
encrypted_storage(Data)