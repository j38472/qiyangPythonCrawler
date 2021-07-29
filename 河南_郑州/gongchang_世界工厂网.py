#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> gongchang_世界工厂网
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-26 11:15
@Desc   ：

一个列表分类链接只显示    五十页  1000 条 数据
已选：省份：河南
https://chanpin.gongchang.com/search-htm-catid-0-kw--areaid-17.html
已选：行业：工业品省份：河南
https://chanpin.gongchang.com/search-htm-catid-136132-kw--areaid-17.html
已选：行业：工业品子类：机械及行业设备省份：河南
https://chanpin.gongchang.com/search-htm-catid-29-kw--areaid-17.html
已选：行业：机械及行业设备子类：煤炭成型设备省份：河南
https://chanpin.gongchang.com/search-htm-catid-9064-kw--areaid-17.html
已选：行业：服装鞋帽子类：其他首饰省份：河南
https://chanpin.gongchang.com/search-htm-catid-423-kw--areaid-17-page-1.html


迭代  catid 值
    areaid   应该是省份地址
    page   页数
    kw 是搜索词   本项目暂时不需要

=================================================='''
from urllib import parse

from lxml import etree
from PIL import Image
import pytesseract

from myJDBC.jdbc import mySqlJdbc
from util.httpTool import MyHttpToolUtil
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

httpTool = MyHttpToolUtil()
tool = MyToolUtil
ioTool = MyIoToolUtil
jdbc = mySqlJdbc()

xpath_xq_href_list = "//div[@class='extension_right']/p/a/@href"

data_xq_data = "hnsj_data_gongchang"


def geSJ(xq_href_list):
    try:
        for xq_href in xq_href_list:
            url_is_gs = jdbc.getUrlGs(url=xq_href, dataBD=data_xq_data)
            if url_is_gs < 1:
                print(xq_href)
                text_xq = httpTool.getHtml_one_none(xq_href)
                sj_set = tool.getSjAllList(text_xq)
                for sj in sj_set:
                    sj_is_gs = jdbc.getSjGs(sj=sj, dataBD=data_xq_data)
                    if sj_is_gs < 1:
                        jdbc.inHnSJ(url=xq_href, sj=sj, dataBD=data_xq_data)
    except Exception as e:
        print("geSJ    ", e)


def geRun(aeraid):
    url_cs_one_test = "https://chanpin.gongchang.com/search-htm-catid-{}-kw--areaid-{}.html"
    url_cs_one_test_page = "https://chanpin.gongchang.com/search-htm-catid-{}-kw--areaid-{}-page-{}.html"
    try:
        for catid in range(1, 136133):
            url_no_page = url_cs_one_test.format(catid, aeraid)
            # print(url_no_page)
            sele_no_page = httpTool.getSele_one_none(url_no_page)
            xq_href_set_on_page = set(sele_no_page.xpath(xpath_xq_href_list))
            if xq_href_set_on_page:
                # print(xq_href_set_on_page)
                geSJ(xq_href_set_on_page)
                for page in range(2, 51):
                    url_yes_page = url_cs_one_test_page.format(catid, aeraid, page)
                    print(url_yes_page)
                    sele_yes_page = httpTool.getSele_one_none(url_yes_page)
                    xq_href_set_yes_page = set(sele_yes_page.xpath(xpath_xq_href_list))
                    if xq_href_set_yes_page:
                        # print(xq_href_set_yes_page)
                        geSJ(xq_href_set_yes_page)
                    else:
                        break
            else:
                break
    except Exception as e:
        print("geRun    ", e)


if __name__ == '__main__':
    """
    areaid
    "郑州",183
    "开封",184
    "洛阳",185
    "新乡",189
    "焦作",190
    "许昌",192
    """
    aeraid_list = [183, 184, 185, 189.190, 192]
    for aeraid in aeraid_list:
        geRun(aeraid)
    pass
