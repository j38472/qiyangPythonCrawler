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

    def in_dqname(self, dataBD, name_address):
        self.sql = "INSERT INTO {} (name_address,cs_count) VALUES('{}',0)".format(dataBD, name_address)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()

    def rmDataId(self, id, dataBD):
        self.sql = "DELETE FROM {} WHERE id = {};".format(dataBD, id)
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
    def setDataSjDh(self, id, dh ,sj, dataBD):
        self.sql = "UPDATE {} SET sj = '{}' ,dh = '{}'WHERE  id = {}".format(dataBD, sj,dh, id)
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

    def inSearch(self, url, name, dataBD):
        sql = "INSERT INTO {} (name,url,isOrNo) VALUES('{}','{}',{})".format(dataBD, name, url, 0)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def inIdSearch(self, IdSearch, dataBD):
        sql = "INSERT INTO {} (name,IdSearch,isOrNo) VALUES('{}',{})".format(dataBD, IdSearch, 0)
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def getLbUrl(self, dataBD):
        self.sql = "SELECT id,Url FROM {} WHERE isOrNo = 0".format(dataBD)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    # 获取对应数据表中存在的URL的个数
    def getUrlGs(self, url, dataBD):
        self.sql = "SELECT * FROM {} WHERE Url = '{}';".format(dataBD, url)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return len(self.results)

    # 获取对应数据表中存在的sj的个数
    def getSjGs(self, sj, dataBD):
        self.sql = "SELECT * FROM {} WHERE sj = '{}';".format(dataBD, sj)
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

    def get_BD_Data_xims(self, dataBD):
        self.sql = "SELECT * FROM {} WHERE ID < 13657;".format(dataBD)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    def getData_startID_endID(self, dataBD, startId, endId):
        """
        获取数据库信息   获取两个索引中间的数据  包头不包尾
        :param dataBD: 表名
        :param startId: 起始坐标 包含该坐标的数据
        :param endId: 结束坐标
        :return: 返回获取的坐标间数据集
        """
        self.sql = "SELECT * FROM {} WHERE {} <= ID AND  {} > ID;".format(dataBD, startId, endId)
        self.cursor.execute(self.sql)
        self.results = self.cursor.fetchall()
        return self.results

    def updata_zzDQName(self, count, idS):
        """
        :param count: 本郑州地区送搜索词的  价值码
        :param idS: 搜索词ID
        :return:
        """
        self.sql = "UPDATE zz_dqname SET cs_count={} WHERE id = {}".format(count, idS)
        print(self.sql)
        self.cursor.execute(self.sql)
        self.conn.commit()
