# -*- encoding: utf-8 -*-
'''
@File    :   5.py
@Time    :   2020/03/20 22:30:10
@Author  :   黎淞
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
'''
5 文件编程小项目
综合编程迷你项目，请完成下列文件(提示:您可以使用列表中的插入功能)
(1)创建一个文件Blowing in the wind.txt,
其内容是：
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
(2) 在文件头部插入歌名“Blowin’ in the wind”
(3) 在歌名后插入歌手名“Bob Dylan”
(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”
(5) 在屏幕上打印文件内容
'''

lyric = '''
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they\'re forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind     
'''
try:
    with open(r'E:\Python\homework\homework-3\Blowing in the wind.txt','w',encoding= 'utf-8')as f1:
        f1.write(lyric)
except IOError:
    print('cannot open')
finally:
    f1.close()

try:
    with open(r'E:\Python\homework\homework-3\Blowing in the wind.txt','r+')as f2:
        line = f2.readlines()
        line.insert(0,'‘Blowin’ in the wind\n')
        line.insert(1, 'Bob Dylan')
        line.append('1962 by Warner Bros. Inc.')
        f2.seek(0)
        f2.writelines(line)
except IOError:
    print('cannot open')
finally:
    f2.close()

try:
    with open(r'E:\Python\homework\homework-3\Blowing in the wind.txt', 'r')as f3:
        lines = f3.readlines()
        for i in range(len(lines)):
            print(lines[i])
except Exception:
    print("open error")
finally:
    f3.close()