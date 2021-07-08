#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-16 8:56
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

dataDb = "guoshu"


def getHtmlSel(url):
    req_text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    selector = etree.HTML(req_text)
    return selector


def getxq_data(url):
    sel = getHtmlSel(url)

    lxr_xpath = "//tr[1]/td[@class='ceil-text']/text()"
    dh_sj_xpath = "//tr[2]/td[@class='ceil-text']/text()"
    dz_xpath = "//tr[4]/td[@class='ceil-text']/text()"
    name_xpath = "//h3[@class='store-name']/text()"
    zy_xpath = "//p[@class='store-intro']/text()"

    lxr_ = sel.xpath(lxr_xpath)
    dh_sj_ = sel.xpath(dh_sj_xpath)
    dz_ = sel.xpath(dz_xpath)
    name_ = sel.xpath(name_xpath)
    zy_ = sel.xpath(zy_xpath)

    lxr = ""
    dh_sj = ""
    dz = ""
    name = ""
    zy = ""

    if lxr_:
        lxr = lxr_[0]
    if dh_sj_:
        dh_sj = dh_sj_[0]
    if dz_:
        dz = dz_[0]
    if name_:
        name = name_[0]
    if zy_:
        zy = zy_[0]

    print(url)
    print(lxr)
    print(dh_sj)
    print(dz)
    print(name)
    print(zy)
    print("<><><><><><><><>"*20)


if __name__ == '__main__':
    url_cs = "http://www.guoshu.cn/company/index-htm-page-{}.html"


    for ym in range(1, 2096 + 1):
        url = url_cs.format(ym)
        xq_url_xpath = "//div[@class='com_sec media-body']/h2/a/@href"
        sel = getHtmlSel(url)
        xq_url_list = set(sel.xpath(xq_url_xpath))
        print(len(xq_url_list))
        for xq_url in xq_url_list:

            getxq_data(xq_url)

        exit()
