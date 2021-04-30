#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> test
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/29 14:20
@Desc   ：对数据库的各种大型操作 入去重表 search_copy1 去重后放入 search中
            Java 写多了  python 也不熟悉  写的代码 真的是  不伦不类的  不Java不python的  难顶
            去重  也可以 直接用set 去重  然后 清空 search  再将set  中的数据存入  本来 id 就是自增的  在这里没啥用  isOrNo 更是没必要修改   整个项目还没有开始  只有等下次咯  数据跑到一万多了
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

def delSearch(id):
    sql  = """
    DELETE FROM search WHERE id = %s;
    """%(id)
    print(sql)
    cursor.execute(sql)
    conn.commit()

if __name__ == '__main__':

    sql = " select * from search;"
    cursor.execute(sql)
    results = cursor.fetchall()
    results = list(results)
    resultsY = results
    i = 0
    y = 0
    while i < len(results):
        y = i + 1
        while y < len(results)-1:
            y = y + 1
            ri = results[i]
            ry = results[y]
            urli = ri[1]
            urly = ry[1]
            # print("i   ", i)
            # print("y   ", y)
            if urli == urly:
                print("--------------start")
                print("ri ",ri)
                print("ry ",ry)
                delSearch(ry[0])
                print("---------------end")

        i = i + 1

# a = [1, 2, 3]
# b = [1, 3]
#
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# for r in results:
#     for r2 in results1:
#         r1Url = r[1]
#         r2Url = r2[1]
#         if r1Url == r2Url:
#             print("啊啊啊啊啊啊啊啊啊啊啊")
#             print(r1Url)
#             print(r2Url)
#             print("id  ", r[0])
#             print("id  ",r2[0])
# print(len(results))
