'''
题目内容：
一个斐波那契数列的前10项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89，对于一个最大项的值不超过n的斐波那契数列，求值为偶数的项的和。
输入格式:
一个正整数n，如100。
输出格式：
值为偶数的项的和，如 2 + 8 + 34 = 44。
输入样例：
100
输出样例：
44
'''
def Fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
    return a
i = 0
sum = 0
n = int(input("请输入一个正整数："))
while(Fibonacci(i) < n):
    if(Fibonacci(i) % 2 ==0):
        sum = sum + Fibonacci(i)
    i += 1
print("值为偶数的项的和为：",sum)
