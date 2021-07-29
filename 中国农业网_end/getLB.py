#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/5/24 9:22
@Desc   ：http://user.zgny.com.cn/  项目 启动器
=================================================='''

import requests
from lxml import etree

from 中国农业网_end.mySqlJdbc import inSearch

url = "http://user.zgny.com.cn/"
xpathLbUrl = "//div[@class='FeiLei']/a[@class='FeiLei_01']/@href"
xpathLbName = "//div[@class='FeiLei']/a[@class='FeiLei_01']/text()"

req = requests.get(url=url)
html = req.text
selector = etree.HTML(html)
listLbUrl = selector.xpath(xpathLbUrl)
listLbName = selector.xpath(xpathLbName)
# print(len(listLbUrl))
print(type(listLbName))
# exit()
for url,name in zip(listLbUrl,listLbName):
    print(url)
    print(name)
    inSearch(name=name,url=url)
    print("___________"*40)
