# Python 斐波那契数列实现

#定义计算斐波那契数列的第n个数的函数

'''--------递推方法-----------------'''

def Fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b    # 注意这个表达式的含义
    return a

for i in range(10):
    print(Fibonacci(i), end=' ')

'''--------递归函数-----------------'''

def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print(fib_recur(i), end=' ')

'''--------生成器-----------------'''

def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a

for i in fib_loop_while(10):
    print(i)