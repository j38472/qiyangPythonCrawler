#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> demo
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-17 10:27
@Desc   ：
=================================================='''
import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

ua = UserAgent()
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
}

proxiesNone = {
    "http": None,
    "https": None
}

jdbc = mySqlJdbc()
"""
http://www.xiaomishu.com/citylist/
http://anshan.xiaomishu.com/shop/search-rAS0_TD-p46/
"""
dataDb = "xiaomishu_search"


def getHtml(url):
    req_text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    # print(req_text)
    return req_text


def getbjsearch():
    url_t = "http://bj.xiaomishu.com/"
    urlbj = "http://bj.xiaomishu.com/sitemap/#region"
    xzq_url_xpath = "//div[@class='dot pt10 pb5 pl10']/a[@class='g3']/@href"
    xzq_name_xpath = "//div[@class='dot pt10 pb5 pl10']/a[@class='g3']/text()"
    selector = etree.HTML(getHtml(urlbj))

    xzq_url_list = selector.xpath(xzq_url_xpath)
    xzq_name_list = selector.xpath(xzq_name_xpath)

    for xzq_url, xzq_name in zip(xzq_url_list, xzq_name_list):
        jdbc.inSearch(url=url_t + xzq_url, name="北京" + xzq_name, dataBD=dataDb)
        selector_ = etree.HTML(getHtml(url_t + xzq_url))
        name_list = selector_.xpath("//dd/a[@class='res_sch_link_a']/text()")
        href_list = selector_.xpath("//dd/a[@class='res_sch_link_a']/@href")

        for name, href in zip(name_list, href_list):
            jdbc.inSearch(url=url_t + href, name="北京" + xzq_name + name, dataBD=dataDb)


if __name__ == '__main__':
    # urlc = "http://chengdu.xiaomishu.com/"
    # getHtml(urlc)
    # exit()

    getbjsearch()
    exit()

    dq_href_xpath_one = "//a[@class='dib mr15 mb10 b']/@href"
    dq_name_xpath_one = "//a[@class='dib mr15 mb10 b']/text()"

    dq_href_xpath_two = "//a[@class='dib mr15 mb10 ']/@href"
    dq_name_xpath_two = "//a[@class='dib mr15 mb10 ']/text()"

    url = "http://www.xiaomishu.com/citylist/"

    selector = etree.HTML(getHtml(url))

    dq_href_list_one = selector.xpath(dq_href_xpath_one)
    dq_name_list_one = selector.xpath(dq_name_xpath_one)

    dq_href_list_two = selector.xpath(dq_href_xpath_two)
    dq_name_list_two = selector.xpath(dq_name_xpath_two)
    print(dq_href_list_two)
    print(dq_name_list_two)

    xq_href_xpath = "//div[1]/div/span/a/@href"
    xq_name_xpath = "//div[1]/div/span/a/text()"

    for href_one, name_one in zip(dq_href_list_one, dq_name_list_one):
        if name_one == "北京":
            print(href_one)
            print(name_one)
            # xq_selector = etree.HTML(getHtml(href_one))
            # xq_href_list = xq_selector.xpath(xq_href_xpath)
            # xq_name_list = xq_selector.xpath(xq_name_xpath)
            # print(xq_href_list)
            # for xq_href,xq_name in zip(xq_href_list,xq_name_list):
            #     jdbc.inSearch(url=href_one+xq_href,name=name_one+xq_name,dataBD=dataDb)
            # exit()

    # for href_two, name_two in zip(dq_href_list_two, dq_name_list_two):
    #     print(href_two)
    #     print(name_two)
    #     if name_two != "北京":
    #         xq_selector = etree.HTML(getHtml(href_two))
    #         xq_href_list = xq_selector.xpath(xq_href_xpath)
    #         xq_name_list = xq_selector.xpath(xq_name_xpath)
    #         print(xq_href_list)
    #         for xq_href, xq_name in zip(xq_href_list, xq_name_list):
    #             jdbc.inSearch(url=href_two + xq_href, name=name_two + xq_name, dataBD=dataDb)
