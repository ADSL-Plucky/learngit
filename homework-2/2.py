# 2 编写一个函数,接收n个数字，求这些参数数字的和;
def Sum(n):
    Type = [list,tuple,set]
    if type(n) in Type:
        return sum(n)
    elif type(n) == int:
        return n
a = [1,2,3,4,5,6]
b = (1,2,3,4,5,6)
c = {1,2,3,4,5,6}
d = 21
print(Sum(a))
print(Sum(b))
print(Sum(c))
print(Sum(d))

