#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> shanghai
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-08-24 13:54
@Desc   ：
=================================================='''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> data
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-17 13:43
@Desc   ：
=================================================='''
import re
from time import sleep

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil

ua = UserAgent()
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
}

proxiesNone = {
    "http": None,
    "https": None,
}

jdbc = mySqlJdbc()
tool = MyToolUtil()

data_search = "xiaomishu_search"
data_data = "xiaomishu_data"


def getHtmlSel(url):
    sleep(1.24)
    req_text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    # print(req_text)
    selector = etree.HTML(req_text)
    return selector


def get_xq(url, name):
    sel = getHtmlSel(url=url)
    dz_list_xpath = "//div[@class='p10 fix']/div[@class='pb2']/p/text()"
    dhOrSj_list_xpath = "//div[@class='float_two'][2]/p/text()"
    zy_list_xpath = "//p[@class='cell']/a[@class='g3 tdl dib']/text()"

    dz_list = sel.xpath(dz_list_xpath)
    dhOrSj_list = sel.xpath(dhOrSj_list_xpath)
    zy_list = sel.xpath(zy_list_xpath)

    dz = ""
    dhOrSj = ""
    zy = ""
    for dz_ in dz_list:
        dz_ = tool.set_Qx_Data(dz_)
        dz += dz_

    for dhOrSj_ in dhOrSj_list:
        dhOrSj_ = tool.set_Qx_Data(dhOrSj_)
        dhOrSj += dhOrSj_

    for zy_ in zy_list:
        zy_ = tool.set_Qx_Data(zy_)
        zy += zy_

    # print(zy)
    # print(url)
    # print(name)
    # print(dz)
    # print(dhOrSj)
    # print("<>"*40)
    jdbc.inXqDate(name=name, url=url, zy=zy, lxr="", dh=dhOrSj, sj=dhOrSj, dz=dz, dataBD=data_data)


def get_lb_url(url, url_t):
    print(url,"      ",url_t)
    sel = getHtmlSel(url=url)
    xq_href_list = sel.xpath("//div[@class='title clearfix']/a[@class='db name l mr15']/@href")
    xq_name_list = sel.xpath("//div/div/div[1]/a/h4/text()")

    for xq_href, xq_name in zip(xq_href_list, xq_name_list):
        get_xq(url_t + xq_href, xq_name)

    xyy_name = sel.xpath("//div/a[@class='page_able']/text()")
    xyy_href = sel.xpath("//div/a[@class='page_able']/@href")
    for name, href in zip(xyy_name, xyy_href):
        if name.find("下一页") > -1:
            get_lb_url(url_t + href, url_t)


if __name__ == '__main__':
    # url = "http://chongqing.xiaomishu.com/shop/search-rCQ_TN/"

    get_lb_url(url="http://www.xiaomishu.com/shop/search",url_t = "http://www.xiaomishu.com/")
    exit()

