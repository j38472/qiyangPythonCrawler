#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> test
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/26 10:08
@Desc   ：
=================================================='''
if __name__ == '__main__':
    sql = """
               DELETE FROM %s WHERE Url IN
                (SELECT Url FROM (SELECT Url FROM %s GROUP BY Url HAVING COUNT(Url)>1) e)
                AND Id NOT IN 
                (SELECT Id FROM (SELECT MIN(Id) AS Id FROM %s GROUP BY Url HAVING COUNT(Url)>1) t);
               """ % ("table_name", "table_name", "table_name")
    print(sql)
