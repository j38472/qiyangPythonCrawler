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
    sql = """SELECT * FROM %s;
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
    sql = """
    UPDATE %s SET isOrNo=1 WHERE id = %s
    """%(tableDb,id)
    # print(sql)
    cursor.execute(sql)
    conn.commit()
    return None

# except:
# 发生错误就回滚数据
# conn.rollback()




if __name__ == '__main__':
    getDataDb("relatedwords")
    # cursor.execute("SELECT Name,Url FROM ziyouname WHERE id<50;")
    # for data in cursor.fetchall():
    #     insDataAll(data)


