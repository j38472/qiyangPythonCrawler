#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> JDBC
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/26 9:16
@Desc   ：各种对数据库的操作
=================================================='''

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    db="qiyangdata",
    user="root",
    password="root",
)
cursor = conn.cursor()

"""
插入数据   如果没有那个数据   也应该设置为空
"""
def insDataAll(data):
    # try:
        name = ""
        url = ""
        zy = ""
        lxr = ""
        dh = ""
        sj = ""
        dz = ""

        if data[0] != None:
            name = data[0]
        if data[1] != None:
            url = data[1]
        if data[2] != None:
            c = data[2]
        print(name)
        print(url)
        print(c)
        sql = """
            INSERT INTO ziyouname (Name,Url) VALUES('测试3%s','%s')
            """ % (name, url)
        # cursor.execute(sql)
        # conn.commit()

    # except:
        # 发生错误就回滚数据
        # conn.rollback()


if __name__ == '__main__':
    cursor.execute("SELECT Name,Url FROM ziyouname WHERE id<50;")
    for data in cursor.fetchall():
        insDataAll(data)
