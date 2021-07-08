#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> jdbc
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-05-31 11:42
@Desc   ：
=================================================='''
import time

import pymysql


class mySqlJdbc:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=6606,
            db="qiyang",
            user="root",
            password="",
        )
        self.cursor = self.conn.cursor()

    def rmDataId(self,id,dataBD):
        self.sql = "DELETE FROM {} WHERE id = {};".format(dataBD,id)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()

    def inHnSJ(self, url, sj, dataBD):
        self.sql = "INSERT INTO {} (Url,SJ) VALUES('{}','{}')".format(dataBD, url, sj)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()

    def setSearch(self, id, dataBD):
        self.MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sql = "UPDATE {} SET isOrNo=2,shiJian = '{}' WHERE  id = {}".format(dataBD, self.MyTime, id)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
        pass

    def setSearchUrl(self, id, url, dataBD):
        self.sql = "UPDATE {} SET url = '{}' WHERE  id = {}".format(dataBD, url, id)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()

    def setDataSj(self, id, sj, dataBD):
        self.sql = "UPDATE {} SET sj = '{}' WHERE  id = {}".format(dataBD, sj, id)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()

    def inXqDate(self, name, url, zy, lxr, dh, sj, dz, dataBD):
        self.MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sql = "INSERT INTO {} (Name,Url,Zy,LXR,DH,SJ,DZ,ShiJian) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            dataBD, name, url, zy, lxr, dh, sj, dz, self.MyTime)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
        pass

    def inSearch(self, url, name, dataBD):
        sql = "INSERT INTO {} (name,url,isOrNo) VALUES('{}','{}',{})".format(dataBD, name, url, 0)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def getLbUrl(self, dataBD):
        self.sql = "SELECT id,Url FROM {} WHERE isOrNo = 0".format(dataBD)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    # 获取对应数据表中存在的URL的个数
    def getIsOrNo(self, url, dataBD):
        self.sql = "SELECT * FROM {} WHERE Url = '{}';".format(dataBD, url)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return len(self.results)

    def get_BD_Search(self, dataBD):
        self.sql = "SELECT * FROM {};".format(dataBD)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    def get_BD_Data(self, dataBD):
        self.sql = "SELECT * FROM {};".format(dataBD)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results
