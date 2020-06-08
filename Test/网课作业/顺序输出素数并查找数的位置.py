
import  math
def prime(x):
    num = 2
    list1 = []
    while num < x:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            list1.append(num)
        num += 1
    return list1
def bi_search(num,list1,high,low):
    if low > high:
        return -1
    mid = low + (high - low) / 2
    if num == list1[mid]:
        return mid
    elif num < list1[mid]:
        return bi_search(num, list1,mid - 1,low)
    else:
        return bi_search(num, list1,high,mid + 1)
n = int(raw_input())
list1 = prime(n)
print(list1)
for i in range(3):
    num = int(raw_input())
    low = 0
    high = len(list1) -1
    print bi_search(num,list1,high,low)

