#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> JDBC
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/26 9:16
@Desc   ：各种对数据库的操作
=================================================='''
import time

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    db="qiyang",
    user="root",
    password="root",
)
cursor = conn.cursor()


def inQGIp(ip):
    A = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    A = '"'+ A +'"'
    sql =  "INSERT INTO qg_ip (IP,SJ) VALUES({},{})".format(ip,A)
    cursor.execute(sql)
    conn.commit()

"""
获取当前ip 是否设置进 青果的白名单IP中
"""
def getQGIp(ip):
    pass
    sql =" SELECT IP FROM qg_ip WHERE IP = {};".format(ip)
    cursor.execute(sql)
    results = cursor.fetchall()
    return len(results)

def getUrlIsOrNo(url):
    pass
    sql = """
    SELECT Url FROM cn_china_cn WHERE Url = "%s";
    """ % (url)
    cursor.execute(sql)
    results = cursor.fetchall()
    return len(results)


"""
ip存储库
"""
def inProxyMeta(proxyMeta):
    sql = """ INSERT INTO proxies (url) VALUES('%s')
                            """ % (proxyMeta)
    cursor.execute(sql)
    conn.commit()
def getSqlProxyMeta():
    sql = " select url from proxies order by id DESC limit 1;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

"""
获取tableName 表 的所有
并形成二维数组 返回
"""


def getDataDb(tableName):
    sql = """SELECT * FROM %s  WHERE isOrNo<2 AND id >11741;
                        """ % (tableName)
    cursor.execute(sql)
    results = cursor.fetchall()
    # print(len(results))
    # cont = 0
    # for l in results:
    #     cont+=1
    #     print("第",cont,"个数据:: ",l)
    return results



"""
给我一个list 和表名  让我存入分类字段表(relatedwords)里
"""


def insGJ(dataList,titDb):
    for data in dataList:
        sql = """
        INSERT INTO %s (url) VALUES('%s')
                    """ % (titDb,data)
        cursor.execute(sql)
        conn.commit()


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

"""
修改isOrNo为1 表示其已经处理过了
"""
def updateIsOrNo(tableDb,id):
    A = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    A = '"'+ A +'"'
    sql = """
    UPDATE %s SET isOrNo=2,shiJian = %s WHERE id = %s
    """%(tableDb,A,id)
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return None

# except:
# 发生错误就回滚数据
# conn.rollback()


"""
存入详情页的数据
"""
def addDate(dataDb,name,url,zy,lxr,dh,sj,dz):
    A = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql = """INSERT INTO %s (Name,Url,Zy,LXR,DH,SJ,DZ,shiJian)VALUES('%s','%s','%s','%s','%s','%s','%s','%s');"""%(dataDb,name,url,zy,lxr,dh,sj,dz,A)
    cursor.execute(sql)
    conn.commit()
    print(sql)




# if __name__ == '__main__':
#     url = "https://jinshengjixie2015.cn.china.cn/contact-information/"

    # updateIsOrNo("search",1)
    # cursor.execute("SELECT Name,Url FROM ziyouname WHERE id<50;")
    # for data in cursor.fetchall():
    #     insDataAll(data)


