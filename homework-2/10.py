'''
 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
'''
def cacluate(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return '除数不能为0！'
        else:
            return a / b
    else:
        return '运算符输入错误！'

try:
    a = float(input('请输入数字A：'))
    b = float(input('请输入数字B：'))
    operator = input('请输入运算符：')
    print(cacluate(a, b, operator))
except ValueError:
    print("您输入的不是数字，请再次尝试输入！")
