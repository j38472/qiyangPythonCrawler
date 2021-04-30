#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> crawList
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/28 9:17
@Desc   ：列表页的爬虫
        使用find的方法的返回的坐标值(-1则代表不存在)判断该列表页的url 是哪一种  采取哪一种的爬虫策略
=================================================='''
#
import re

import requests
from lxml import etree

from 中国供应商.run import myJDBC, craw

# 用于 存储ip
from 中国供应商.run.myRequests import getHtmlData

# 本次列表一共搜索出多少条数据
xpathLS = "//div[@class='location_an']/span[@class='fr']/span/text()"


def getListData(url, cont):
    cont += 1
    html = getHtmlData(url)
    # print(html)
    selector = etree.HTML(html)
    # 获取本页面所有的列表页链接  存入第二个列表页的表中 search_copy1  使用Re
    Re = "https://www.china.cn/[^\s]*.shtml"
    urlLbList = re.findall(Re, html)
    # print(len(urlLbList))

    # 判断该列表页还有没有数据了  //div[@class="nort"]
    xpathisOrNo = "//div[@class=\"nort\"]"
    isOrNo = selector.xpath(xpathisOrNo)
    # 似乎 不写这个也行  没有数据的情况下 自然没有下一页的URL 了
    if isOrNo:
        print("没有数据了")
    else:
        # 遍历 并去重  正式开始
        if cont <= 1:
            print("列表页URL  需要去重 存入search_copy1中的 ,len(urlLbList)去重前的URL  ", len(urlLbList))
            urlLbSet = set(urlLbList)
            myJDBC.insGJ(urlLbSet, "search_copy1")
        # 解析该页面 获取详情页的链接  并调用 craw   修改为从公司名字处获取 直接进入公司的主页面   联系方式URL 后缀需要拼接 /contact-information/   这个页面比较规范
        xpathXQUrl = "//ul[@class='extension_ul']/li/div[@class='extension_right']/p[1]/a/@href"
        XQUrlList = selector.xpath(xpathXQUrl)
        print("len(XQUrlList)  ", len(XQUrlList))
        # 去重
        XQUrlSet = set(XQUrlList)
        for sqUrl in XQUrlSet:
            sqUrl += "/contact-information/"
            print("sqUrl", sqUrl)
            # 爬取详情页信息
            craw.start(sqUrl)

        #    判断是不是有下一页
        xpathNext = "//a[@class='rollPage']/@href"

        next = selector.xpath(xpathNext)
        if next:
            # 如果再次只取到一个 （下一页|上一页）的链接  同时 该列表页的计数器 大于一的时候则退出该页面（说明本列表页没有了下一页了）
            if len(next) == 1 and cont > 1:
                return
            else:
                next = next[len(next) - 1]
                print("计数器为:", cont)
                print(next)
                getListData(next, cont)

    # print(len(urlLbSet))
    # for url in urlLbSet:
    #     print(url)

    # print("xpathLS ", xpathLS)
    # listLS = selector.xpath(xpathLS)
    # for ls in listLS:
    #     print("ls::", ls)
    # # 转为int  类型
    # i = 0
    # i += int(ls)


# {'http': 'http://114.231.104.192:21504'}

if __name__ == '__main__':
    # 每次开始  列表页的计数器就从零开始
    # getListData("https://www.china.cn/search/fyax3.shtml?p=15",0)

    # 正式开始
    # fd = "www.china.cn/search"
    listSearch = myJDBC.getDataDb("search")
    for search in listSearch:
        id = search[0]
        url = search[1]
        isOrNo = search[2]
        # 每次开始  列表页的计数器就从零开始
        print("url  ", url)
        if isOrNo < 1:
            getListData(url, 0)
        #     每一次处理完该条列表页 都需要修改isOrNo
        myJDBC.updateIsOrNo("search", id)
