#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> search
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-02 16:33
@Desc   ：爬取列表页的
=================================================='''

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

ua = UserAgent()
jdbc = mySqlJdbc()
header_UA = {
    'User-Agent': ua.random,
}
url = "http://china.makepolo.com/list/d16/"
req =  requests.get(url=url,headers=header_UA)
url_LB_xpath = "//dl/dd/a/@href"
url_lbName_xpath = "//dl/dd/a/text()"
selector_lb = etree.HTML(req.text)
lb_url_list = selector_lb.xpath(url_LB_xpath)
lb_name_list = selector_lb.xpath(url_lbName_xpath)
for n,u in zip(lb_name_list,lb_url_list):
    print(n)
    print(u)
    jdbc.inSearch(u,n,"mkbl_search")
# print(len(lb_url_list))
# print(lb_url_list)



