#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-06 14:59
@Desc   ：
=================================================='''
import requests
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}
urlcccc = "http://www.gucn.com/Service_Shop_Detail.asp?Id=395"
req = requests.get(url=urlcccc, headers=header, proxies=proxiesNone)
print(req.text)