#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> 键值对_字典
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/26 10:45
@Desc   ：
=================================================='''

# #1.键值对，在python中是字典，在C语言中是结构体
# name = {'green':5}
# print(name['green'])
# #2.访问键值对
# name = {'color':'green','point':5}#对是字符串要加引号，是数字不用
# space = name['point']#大括号针对整体，里面键值对用中括号
# print("woaini"+str(space)+" fwef")
# #3.添加键值对
# print(name)
# name['posion'] = 'dqwd'#牢记键要带引号，值上述说了分情况
# print(name)#键值对的排列顺序和添加顺序不同





#4.修改和删除

# name = {'color':'green','point':5}
# name['color'] = 'red'
# print(name)
# del name['color']#永久删除
# print(name)




#5.遍历字典中的所有键值对，键，值

# language = {'wu':'C',
#             'xing':'java',
#             'rui':'python'}
# for i,j in language.items():#items遍历键值对，我们叫方法items()
#     print("name "+i)
#     print("yuyan "+j)
#     print("\n")
# for i in language.keys():#keys()遍历键，我们叫方法keys()
#     print("name "+i)
# for i in sorted(language.keys()):#按照一定的顺序遍历
#     print("name "+i)
# for i in language.values():#遍历所有的值，发现重复项的值也会一样输出
#     print("language "+i)
# for i in set(language.values()):#使用set可删除重复的值
#     print("language "+i)




#6.列表存字典

line1 = {'color':'red','point':5}
line2 = {'color':'red','point':10}
line3 = {'color':'red','point':15}
line = [line1,line2,line3]
print(line)
#7.字典中存列表
name = {'color':'red',
        'point':[5,10],
        }
print(name)
print(name['point'])
#8.在字典中存字典
name = {'color':'red',
        'point':{'color':'green',
                 'point':10
                 }
        }
print(name)
print(name['color'])
print(name['point']['color'])#输出里面字典的信息


'''
#9.在列表中存列表
line = [1,2,3,4]
name = [5,4,1,line]#python中如果互换两行可能就不对了
print(name)'''
'''
#10.input()#把input括号里面的输出
message = "请输入你的名字:"
message+="当然你也可以输入你的绰号"
name = input(message)#将输入的字符串变为int类型，前后变量要一致
print("你好,"+name+",你长得真帅")
'''
'''
#11.while循环
prompt = '若果你不想玩了，请输入quit退出，如果还想玩请输入其他的'
message = ' '
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#12.标志
prompt = '若果你不想玩了，请输入quit退出，如果还想玩请输入其他的'
active = True
while active:
    message = input(prompt)
    if message =='quit':
        active = False
    else:
        print(message)#python中的break和continue与C语言一样，不列举了

#13.无限循环
a = 1
while a<2:
    print("我爱你")

#14.移动元素
name = [1,2,3,4,5]
current = []
while name:#name也可以当True，why？
    names = name.pop()#从name删除最后一个，并赋给names
    current.append(names)#把删除的那个也就是names加到current
print(current)#实现了列表name的元素移到列表current
'''

# #15.删除包含特定值的列表元素
# name = [1,2,3,4,5]
# while 4 in name:
#     name.remove(4)
# print(name)
# #16.使用用户的输入来填充字典
# name = {'color':'red','point':5}
# print(name)
# jian = input()
# zhi =input()
# name[jian] = zhi
# print(name)
