# 练习:  定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;
# def outer(func):
#     def inner(func):
#         func()
#         print("执行了加法")
#     return inner

# @outer
# def add(a,b):
#     return a + b
# print(add(1,2))
def outer(func):  # 将index的地址传递给func
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)   # fun = index  即func保存了外部index函数的地址;
        return result
    return inner  # 返回inner的地址
@outer
def add(a,b):
    return a + b
print(add(1,2))


