# -*- encoding: utf-8 -*-
'''
@File    :   6.py
@Time    :   2020/03/20 23:20:15
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;
   并分别输出统计结果到另外的文件存放;
   比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
'''
import os
def statistics(readfilename,printfilename):
    List = []
    Dic = {}
    chars = ['','\n']
    try:
        f1 = open(readfilename,"r",encoding = "UTF8")
        for Line in f1.readlines():
            List.append(Line)
        f1.close()
        for item in List:
            Words = item.split(" ")
            for word in Words:
                if word not in Dic.keys():
                    Dic[word] = 1
                else:
                    Dic[word] = Dic[word] + 1
        sortedDic = sorted(zip(Dic.values(), Dic.keys()), reverse=True)
        with open(printfilename,'w',encoding='utf-8')as f2:
            for x in sortedDic:
                if x[1] not in chars:
                    f2.write("%s\t%s\n" % (x[0], x[1]))
        f2.close()
    except Exception as e1:
        print(e1)
def Compare(file1,file2):
    try:
        f1 = open(file1, "r", encoding="UTF8")
        f2 = open(file2, "r", encoding="UTF8")
        SameWord = 0
        List1 = [Line.strip('\n').split('\t') for Line in f1.readlines()]
        List2 = [Line.strip('\n').split('\t') for Line in f2.readlines()]
        f1.close()
        f2.close()

        for i in range(10):
            if List1[i][1] == List2[i][1]:
                SameWord += 1
        similarity = SameWord / 10
        simi_str = "这两篇文章的相似度为：{:.2%}".format(similarity)
        with open('Compare.txt','w',encoding='utf-8') as f3:
            f3.writelines(simi_str)
        print("这两篇文章的相似度为：{:.2%}".format(similarity))
    except Exception as e1:
        print(e1)
statistics('literature 1.txt','Statistical_result 1.txt')
statistics('literature 2.txt','Statistical_result 2.txt')
Compare('Statistical_result 1.txt','Statistical_result 2.txt')
