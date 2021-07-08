#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> list_search
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-28 14:52
@Desc   ：
=================================================='''

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

ua = UserAgent()

sn_search = "sn_search"
sn_data = "sn_data"


header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}
url = "https://list.suning.com/"
req = requests.get(url=url, headers=header, proxies=proxiesNone)
req_text = req.text
# 餐厨用具
href_list_xpath_1 = "//div[@id='20061']/div[@class='title-box clearfix'][5]//a/@href"
name_list_xpath_1 = "//div[@id='20061']/div[@class='title-box clearfix'][5]//a/text()"
# 餐饮
href_list_xpath_2 = "//div[@id='505642']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_2 = "//div[@id='505642']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/text()"

# 厨卫电器 生活电器
href_list_xpath_3 = "//div[@id='20358']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_3 = "//div[@id='20358']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/text()"
# 冰箱/冷柜
href_list_xpath_4 = "//div[@id='20268']/div[@class='title-box clearfix'][3]/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_4 = "//div[@id='20268']/div[@class='title-box clearfix'][3]/div[@class='t-right fl clearfix']//a/text()"
# 餐椅
href_list_xpath_5 = "//div[@id='457529']/div[@class='title-box clearfix'][3]/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_5 = "//div[@id='457529']/div[@class='title-box clearfix'][3]/div[@class='t-right fl clearfix']//a/text()"
# 生鲜
href_list_xpath_6 = "//div[@id='503915']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_6 = "//div[@id='503915']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/text()"
# 食品保健/酒水饮料
href_list_xpath_7 = "//div[@id='500353']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_7 = "//div[@id='500353']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/text()"
# 进口食品
href_list_xpath_8 = "//div[@id='500354']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/@href"
name_list_xpath_8 = "//div[@id='500354']/div[@class='title-box clearfix']/div[@class='t-right fl clearfix']//a/text()"

selector = etree.HTML(req_text)

href_list_1 = selector.xpath(href_list_xpath_1)
name_list_1 = selector.xpath(name_list_xpath_1)

href_list_2 = selector.xpath(href_list_xpath_2)
name_list_2 = selector.xpath(name_list_xpath_2)

href_list_3 = selector.xpath(href_list_xpath_3)
name_list_3 = selector.xpath(name_list_xpath_3)

href_list_4 = selector.xpath(href_list_xpath_4)
name_list_4 = selector.xpath(name_list_xpath_4)

href_list_5 = selector.xpath(href_list_xpath_5)
name_list_5 = selector.xpath(name_list_xpath_5)

href_list_6 = selector.xpath(href_list_xpath_6)
name_list_6 = selector.xpath(name_list_xpath_6)

href_list_7 = selector.xpath(href_list_xpath_7)
name_list_7 = selector.xpath(name_list_xpath_7)

href_list_8 = selector.xpath(href_list_xpath_8)
name_list_8 = selector.xpath(name_list_xpath_8)

# print(href_list_1)
# print(" len(href_list)    ", len(href_list_1))
# print(name_list_1)
# print(" len(name_list)        ", len(name_list_1))
#
# print(href_list_2)
# print(" len(href_list)    ", len(href_list_2))
# print(name_list_2)
# print(" len(name_list)        ", len(name_list_2))
#
# print(href_list_3)
# print(" len(href_list)    ", len(href_list_3))
# print(name_list_3)
# print(" len(name_list)        ", len(name_list_3))
#
# print(href_list_4)
# print(" len(href_list)    ", len(href_list_4))
# print(name_list_4)
# print(" len(name_list)        ", len(name_list_4))
#
# print(href_list_5)
# print(" len(href_list)    ", len(href_list_5))
# print(name_list_5)
# print(" len(name_list)        ", len(name_list_5))
#
# print(href_list_6)
# print(" len(href_list)    ", len(href_list_6))
# print(name_list_6)
# print(" len(name_list)        ", len(name_list_6))
#
# print(href_list_7)
# print(" len(href_list)    ", len(href_list_7))
# print(name_list_7)
# print(" len(name_list)        ", len(name_list_7))
#
# print(href_list_8)
# print(" len(href_list)    ", len(href_list_8))
# print(name_list_8)
# print(" len(name_list)        ", len(name_list_8))

href_all = href_list_1 + href_list_2 + href_list_3 + href_list_4 + href_list_5 + href_list_6 + href_list_7 + href_list_8
name_all = name_list_1 + name_list_2 + name_list_3 + name_list_4 + name_list_5 + name_list_6 + name_list_7 + name_list_8
# print(len(href_all))
# print(len(name_all))
jdbc = mySqlJdbc()



for href, name in zip(href_all, name_all):
    jdbc.inSearch(url=href,name=name,dataBD=sn_search)

