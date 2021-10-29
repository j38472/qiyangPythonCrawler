#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> DBqx
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-10-08 10:51
@Desc   ：

有很多的店铺是存在多个手机号  或者 座机号

=================================================='''

data1 = ['7', '郑州市金水区人民政府', '(0371)66712345,(0371)63526200,(0371)58579017,17337130202,17337130202', '郑州市金水区东风路16号', '2021-09-28 10:30:00']

sjanddh = data1[2]

print(data1[0])
print(data1[1])
print(sjanddh)
print(data1[3])
print(data1[4])

sjanddh = sjanddh.replace('(', '')
sjanddh = sjanddh.replace(')', '-')
sjanddh = sjanddh.split(',')
print("<<<<<<<<<<<<<<<<<<<       ", sjanddh)
