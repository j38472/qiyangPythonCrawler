#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> mySqlJdbc
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/5/24 9:35
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

    def setSearch(self,id):
        self.MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sql = "UPDATE zgny_search SET isOrNo=2,shiJian = %s WHERE id = %s".format(self.MyTime,id)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
        pass

    def getIsOrNo(self,url):
        self.sql ="SELECT url FROM zgny_data WHERE url = '{}';".format(url)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    def inXqDate(self,name,url,zy,lxr,dh,sj,dz):
        self.MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sql = "INSERT INTO zgny_data (Name,Url,Zy,LXR,DH,SJ,DZ,ShiJian) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,url,zy,lxr,dh,sj,dz,self.MyTime)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
        pass

    def getLbUrl(self, tabedate):
        self.sql = "SELECT id,Url FROM {} WHERE isOrNo = 0".format(tabedate)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    def inSearch(self, url, name):
        MyTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        MyTime = '"' + MyTime + '"'
        sql = "INSERT INTO zgny_search (name,url) VALUES('{}','{}')".format(name, url)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
