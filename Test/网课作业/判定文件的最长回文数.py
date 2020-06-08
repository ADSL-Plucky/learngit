# def Judge(s):
#     low = 0
#     high = len(s) - 1
#
#     while low < high:
#         if s[low] != s[high]:
#             return False
#         low += 1
#         high -= 1
#
#     return  True
def Judge2(s):
    if len(s) <=1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        else:
            return Judge2(s[1:-1])
f = open("names.txt",'r')
Len = 2
str = 'AA'
for line in f:
    line = line.strip()
    if Judge2(line):
        if len(line) > Len:
            str = line
            Len = len(line)
            print str,Len
print str
f.close()