# 练习1:
#       定义一个高阶函数, 实现加,减,乘,除计算器功能;
def plus(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def fnc(a,b,foo):
    return foo(a,b)
print(fnc(10,2,plus))
print(fnc(10,2,subtract))
print(fnc(10,2,multiply))
print(fnc(10,2,divide))

