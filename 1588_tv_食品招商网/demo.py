#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> demo
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-07 9:56
@Desc   ：
=================================================='''
import httpx

url = "http://www.1588.tv/company/1"
html = httpx.get(url=url).text
print(html)