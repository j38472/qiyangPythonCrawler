#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> zz_coco
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-07 17:05
@Desc   ：
=================================================='''

url = "http://www.zz.ccoo.cn/phonebook/all/pn{}/"

for ym in range(1,167+1):
    url_C = url.format(ym)
    print(url_C)

xpath_dh = "//span[@class='phone']/a/text()"