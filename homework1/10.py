'''
@File    :   10.py
@Time    :   2020/03/06 23:15:12
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
word = "Given a paragraph of English text , count the number of occurrences of each word\
Print output , output from high to low according to word frequency"
Word = list(word.split(' '))
Tuple = {}
for i in range(len(Word)):
    if(Word[i] in Tuple):
        Tuple[Word[i]] = Tuple[Word[i]] + 1
    else:
        Tuple[Word[i]] = 1
print(Tuple)
sortedDic = sorted(zip(Tuple.values(),Tuple.keys()),reverse=True)
print(sortedDic)