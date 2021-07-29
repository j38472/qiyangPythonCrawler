#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-06 14:59
@Desc   ：
=================================================='''
from time import sleep

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

# ua = UserAgent()
# header = {
#     'User-Agent': ua.random,
# }
# proxiesNone = {
#     "http": None,
#     "https": None
# }
# urlcccc = "http://www.gucn.com/Service_Shop_Detail.asp?Id=395"
# req = requests.get(url=urlcccc, headers=header, proxies=proxiesNone)
# print(req.text)
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil
import pandas as pd
import numpy as np

jdbc = mySqlJdbc()
tool = MyToolUtil()
ioTool = MyIoToolUtil()

dataDb = "hnsj_data_copy4"

xlsx1 = "F:\\xexlsa\\zj\\two.xlsx"
xlsx2 = "F:\\xexlsa\\zj\\set_sj_all.xlsx"


def qxTwoSj_all():
    df1 = pd.read_excel(xlsx1)
    sj_all_zz_set = set()
    for idx, row in df1.iterrows():
        # print(row['sj'])
        sj_all_zz_set.add(row['sj'])

    df2 = pd.read_excel(xlsx2)
    for idx, row in df2.iterrows():
        # print(row['sj'])
        # sleep(0.1)
        sj_all_zz_set.add(row['sj'])
    print(len(sj_all_zz_set))
    ioTool.outXlsx(sj_all_zz_set, "F:\\xexlsa\\zj\\sj_all_zz_set.xlsx")
    # print()
    pass


if __name__ == '__main__':
    qxTwoSj_all()
    exit()

    hn_sj_list = jdbc.get_BD_Data(dataDb)
    set_sj = set()
    for hn_sj in hn_sj_list:
        sj = tool.getsjCall(hn_sj[2])
        set_sj.add(sj)
    print(len(set_sj))
    ioTool.outXlsx(set_sj, "G:\\two.xlsx")
