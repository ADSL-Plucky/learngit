
'''
@File    :   1.py
@Time    :   2020/03/05 23:42:50
@Author  :   黎淞 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
# 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
import math
def is_primer(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
list1 = [x for x in range(0,51) if (x % 2 == 0)]
list2 = [x for x in range(0,51) if (x % 2 == 1)]
list3 = [x for x in range(0,51) if (is_primer(x))]
list4 = [x for x in range(0,51) if (x % 2 == 0 and x % 3 == 0)]
print("0~50之间的偶数有：",list1)
print("0~50之间的奇数有：",list2)
print("0~50之间的质数有：",list3)
print("0~50之间的能同时被2和3整除的数有：",list4)
