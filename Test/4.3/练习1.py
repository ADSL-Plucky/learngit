# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# # -*- coding: utf-8 -*-
# 定义 createCounter() 这个函数
# # 测试:

def createCounter(a = 0):
    def counter():
        return a + 1
    return counter
counterA = createCounter()
print(counterA,counterA())
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')