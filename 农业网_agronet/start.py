#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-16 10:00
@Desc   ：
=================================================='''
import requests
from lxml import etree

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil

url = "http://www.agronet.com.cn/Company/"
data_DB = "agronet_search"
jdbc = mySqlJdbc()


req = requests.get(url=url)
req.encoding = "utf-8"
req_text = req.text
name_xpath = "//dd[@class='overview_list']//a[@ target='_blank']/text()"
url_xpath = "//dd[@class='overview_list']//a[@ target='_blank']/@href"

selector = etree.HTML(req_text)
name_list = selector.xpath(name_xpath)
url_list = selector.xpath(url_xpath)

for name,url in zip(name_list,url_list):
    print(name,"   ",url)
    jdbc.inSearch(url=url,name=name,dataBD=data_DB)
    print("<><><><><><>"*10)
