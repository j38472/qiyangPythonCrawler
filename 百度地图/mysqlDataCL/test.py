#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> test
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-10-19 11:11
@Desc   ：
=================================================='''
from myJDBC.jdbc import mySqlJdbc

"""
再建立一个新的表  将整理出的数据  导入新表中

把电话号存在两个的数据 

拆分未两条



"""

data_DB_name = "map_baidu_data_jg_one"

jdbc = mySqlJdbc()

data_list = jdbc.get_BD_Data(dataBD=data_DB_name)

print(len(data_list))

for data in data_list:
    # print(data)
    id = data[0]
    name = data[1]
    sj = data[6]
    dz = data[7]


    # 先把手机号和电话后的   小括号给清除一下
    sj = sj.replace("(", "")
    sj = sj.replace(")", "-")

    # 再根据逗号分割
    sjList = sj.split(",")

    sj_JG = ""
    dh_jg = ""

    for sjdata in sjList:
        # 如果是电话号就存入电话字段
        if sjdata.find("-") > 0:
            dh_jg = sjdata
        else:
            if sj_JG == "":
                # 手机号为空
                sj_JG = sjdata
            else:
                #         再插入一条数据
                jdbc.inXqDate(name=name, url="", zy="", lxr="", dh="", sj=sj_JG, dz=dz, dataBD=data_DB_name)
    jdbc.setDataSjDh(id=id, dh=dh_jg, sj=sj_JG, dataBD=data_DB_name)


