# 定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算;
def Price():
    wigth = int(input("苹果的重量为："))
    price = int(input("苹果的价格为："))
    return wigth * price
print("购买苹果的总价格  = ", Price())


