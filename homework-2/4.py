# 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
def statistics(n):
    letter = 0
    number = 0
    space = 0
    other = 0
    for i in range(len(n)):
        if n[i] in '0123456789':
            number += 1
        elif n[i] in 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
            letter += 1
        elif n[i] == ' ':
            space += 1
        else:
            other +=1
    print("字母：{}，数字：{}，空格：{},其他字符：{}".format(letter,number,space,other))
Str = input('请输入字符串：')
statistics(Str)