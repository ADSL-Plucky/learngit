# 定义一个函数,  打印输出列表里面的元素;
# 然后增加列表中的元素, 然后再输出新的列表;
# 主程序中,打印这个列表的地址(传参之前,传参之后);
def changeme(mylist):
   print("原参数的值: ", mylist)
   print("修改前函数的地址：", id(mylist))
   mylist.append([1,2,3,4])
   print("修改后的值: ", mylist)
   print("修改后函数的地址：", id(mylist))
   return

# 调用changeme函数
mylist = [10,20,30]
print("传参前函数的地址：",id(mylist))
changeme(mylist)
print("函数外取值: ", mylist)
print("传参后函数的地址：",id(mylist))