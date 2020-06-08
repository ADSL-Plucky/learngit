# 使用不定长参数定义一个函数;
# 实现对输入数据的封装(封装成一个列表和字典), 然后打印输出;
def PrintList(x,*args):
    print('第一个参数:', x)
    print('第二个参数:', args)
    list = [args]
    print(list)
def Print(**ver):
    for key,value in ver.items():
        print("["+key+"]的星座是："+value)
PrintList(11,12,13,14,15)
Print(一梦='水瓶座',冷意='射手座')
from random import randint
data1=[randint(-10,10) for _ in range(10)]
print(data1)
