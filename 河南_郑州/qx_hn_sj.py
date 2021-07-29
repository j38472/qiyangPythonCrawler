#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> qx_hn_sj
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-14 9:14
@Desc   ：
=================================================='''

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

dataDb1 = "hnsj_data_copy1"
dataDb2 = "hnsj_data_copy2"
dataDb3 = "hnsj_data_copy3"

jdbc = mySqlJdbc()
tool = MyToolUtil()
ioTool = MyIoToolUtil()

if __name__ == '__main__':
    data_sj_1_set = set(jdbc.get_BD_Data(dataBD=dataDb1))
    # data_sj_2_set = set(jdbc.get_BD_Data(dataBD=dataDb2))
    # data_sj_3_set = set(jdbc.get_BD_Data(dataBD=dataDb3))
    # print(len(data_sj_1_list))
    # print(len(data_sj_2_list))
    # print(len(data_sj_3_list))
    set_sj_all = set()
    for data_sj_1 in data_sj_1_set:
        set_sj_all.add(data_sj_1[2])

    # for data_sj_1 in data_sj_2_set:
    #     set_sj_all.add(data_sj_1[2])
    #
    # for data_sj_1 in data_sj_3_set:
    #     set_sj_all.add(data_sj_1[2])
    print(len(set_sj_all))
