# 练习:  
#  定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样;  然后实例化几条狗, 然后统计实例化狗的数量
class dog:
    def __init__(self,color,name):
       self.color = color
       self.name = name   
    def bark(name):
        if name == 'A':
            return '汪汪'
        elif name == 'B':
            return '沃沃'
        else:
            return '嗷呜'
    
