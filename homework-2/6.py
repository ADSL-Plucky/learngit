#  定义一个函数, 打印输出n以内的斐波那契数列;
def Fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
    return a
j = 0
n = int(input('请输入打印的Fibonacci数列的数量n：'))
for i in range(n):
    print(Fibonacci(i), end=' ')
    j += 1
    if j == 10:
        print()
        j = 0