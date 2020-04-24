# 1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def Return_Len(a):
    return len(a)
a = 'dfazgd'
c = [123,15,156865]
b = (123,12,12)
print(Return_Len(a))
print(Return_Len(b))
print(Return_Len(c))