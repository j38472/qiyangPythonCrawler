#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-08 14:07
@Desc   ：
=================================================='''

from myJDBC.jdbc import mySqlJdbc

jdbc = mySqlJdbc()

allLIst = jdbc.get_BD_Data("zz_dqname")

print(len(allLIst))

for dataA in allLIst:
    id = dataA[0]
    addrss = dataA[1]
    print(id)
    for dataB in allLIst[id:]:
        # print(dataB[0])
        # print("<><><><><><><><>")
        if addrss == dataB[1]:
            jdbc.rmDataId(dataB[0], dataBD="zz_dqname")
