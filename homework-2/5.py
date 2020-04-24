# 写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
def examine_dic(Dic):
    for key,value in Dic.items():
        if len(value) > 2:
            Dic[key] = value[:2]
    return Dic
Dic = {'qq':'836046238','名字':'黎淞','学号':'120181080106','性别':'男'}
Dic = examine_dic(Dic)
for key,value in Dic.items():
    print(key,value)
