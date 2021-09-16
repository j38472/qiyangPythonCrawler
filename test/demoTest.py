#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> demoTest
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-02 9:57
@Desc   ：
=================================================='''
from myJDBC.jdbc import mySqlJdbc
from util.httpTool import MyHttpToolUtil
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

httpTool = MyHttpToolUtil()
tool = MyToolUtil
ioTool = MyIoToolUtil
jdbc = mySqlJdbc()



if __name__ == '__main__':
    list_all = jdbc.get_BD_Data("xiaomishu_oneandtwo")
    data1 = list_all[0:200000]
    data2 = list_all[200000:400000]
    data3 = list_all[400000:600000]
    data4 = list_all[600000:800000]
    data5 = list_all[800000:]
    print(len(data1))
    print(len(data2))
    print(len(data3))
    print(len(data4))
    print(len(data5))
    # ioTool.outXlsx(data=chongqing, dataFile="F:\\list\\重庆市.xlsx")