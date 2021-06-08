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


class mySqlJdbc():
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=6606,
            db="qiyang",
            user="root",
            password="",
        )
        self.cursor = self.conn.cursor()

    def setSearch(self,id,dataBD):
        self.MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sql = "UPDATE {} SET isOrNo=2,shiJian = '{}' WHERE  id = {}".format(dataBD,self.MyTime,id)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
        pass

    # 获取对应数据表中存在的URL的个数
    def getIsOrNo(self,url,dataBD):
        self.sql ="SELECT * FROM {} WHERE Url = '{}';".format(dataBD,url)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return len(self.results)

    def inXqDate(self,name,url,zy,lxr,dh,sj,dz,dataBD):
        self.MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sql = "INSERT INTO {} (Name,Url,Zy,LXR,DH,SJ,DZ,ShiJian) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(dataBD,name,url,zy,lxr,dh,sj,dz,self.MyTime)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
        pass

    def getLbUrl(self, dataBD):
        self.sql = "SELECT id,Url FROM {} WHERE isOrNo = 0".format(dataBD)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    def inSearch(self, url, name,dataBD):
        sql = "INSERT INTO {} (name,url,isOrNo) VALUES('{}','{}',{})".format(dataBD,name, url,0)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()