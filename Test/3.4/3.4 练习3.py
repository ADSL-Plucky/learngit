# -*- encoding: utf-8 -*-
'''
@File    :   3.4 练习3.py
@Time    :   2020/03/04 08:41:53
@Author  :   ADSL 
@Version :   3.7.0
@Contact :  836046238@qq.com
'''
name = input("name:")
age = input("age:")
skill = input("skill:")
salary = input("salary:")
 
info = '''
  --- info of ''' + name + ''' 
  name: ''' + name + '''
  age: ''' + age + '''
  skill: ''' + skill + '''
  salary: ''' + salary + '''
'''
print(info)

info1 = '''
 --- info of %s ---
 Name:%s
 Age:%s
 Skill:%s
 Salary:%s
''' % (name,name,age,skill,salary) #注意这里的变量要一 一对应，缺少一个就会报错
print(info1)

info2 = '''
  --- info of {_name}
  Name：{_name}
  Age：{_age}
  Skill：{_skill}
  Salary：{_salary}
'''.format(_name=name, _age=age, _skill=skill, _salary=salary) #此处是赋值 
print(info2)

info3 = '''
  --- info of {0}---
  Name：{0}
  Age：{1}
  Skill：{2}
  Salary：{3}
'''.format(name, name, age, skill, salary)
 
print(info3)


