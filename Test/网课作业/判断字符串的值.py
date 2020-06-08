# def Change(i):
#     if ord(i) >= 65 and ord(i)<=90:
#         return ord(i) - 64
#     elif ord(i) >= 97 and ord(i)<=122:
#         return ord(i) - 96
#     else:
#         return 0
def Change(i):
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    str2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if i in str1:
        return str1.find(i) + 1
    elif i in str2:
        return str2.find(i) + 1
    else:
        return 0
List = []
for i in range(3):
    a = raw_input()
    List.append(a)
for i in range(3):
    num = 0
    for j in List[i]:
        num = num + Change(j)
    print num

