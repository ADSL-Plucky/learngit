'''
请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
  例如:
  输入:aaaabbc，
  输出：a:4
'''
def Find_maximum_string(string):
    List = list(string)
    Tuple = {}
    for i in range(len(List)):
        if (List[i] in Tuple):
            Tuple[List[i]] = Tuple[List[i]] + 1
        else:
            Tuple[List[i]] = 1
    sortedDic = sorted(zip(Tuple.values(), Tuple.keys()), reverse=True)
    n = 1
    while sortedDic[n-1][0] <= sortedDic[n][0]:
        n += 1
        if n == len(sortedDic):
            break
    return sortedDic[:n]
string = input('请输入一个字符串：')
Re = Find_maximum_string(string)
print('该字符串中出现次数最多的字符：')
for i in range(len(Re)-1):
    print(Re[i][1],end = ',')
print(Re[len(Re)-1][1],':',Re[len(Re)-1][0])