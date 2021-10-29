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
from datetime import time, datetime

import requests
from lxml import etree

from 中国供应商.run import myJDBC, craw, myIP

# 用于 存储ip
from 中国供应商.run.myJDBC import getUrlIsOrNo, getQGIp, inQGIp
from 中国供应商.run.myRequests import getHtmlData

# 本次列表一共搜索出多少条数据
xpathLS = "//div[@class='location_an']/span[@class='fr']/span/text()"

coent = 0

booIp = False
DAY_START = time(2, 00)
DAY_END = time(2, 5)
proxiesNone = {
    "http": None,
    "https": None
}


def setQGIp():
    pass
    global booIp
    current_time = datetime.now().time()
    if DAY_START < current_time < DAY_END and booIp:
        pass
        booIp = False
        urlGetIP = "https://httpbin.org/ip"
        ipText = requests.get(url=urlGetIP, proxies=proxiesNone).text
        ipTextEval = eval(ipText)
        ip = ipTextEval['origin']
        ipIsOrNo = getQGIp(ip)
        if ipIsOrNo == 0:
            setIP = "https://proxy.qg.net/whitelist/add?Key=F58B5B03A518E080&IP={}".format(ip)
            requests.post(url=setIP, proxies=proxiesNone)
            print("青果白名单ip添加成功")
            inQGIp(ip)
    if current_time < DAY_START and booIp == False:
        pass
        booIp = True


def getListData(url, cont):
    global coent
    coent += 1
    cont += 1
    html = getHtmlData(url)
    if html != 404:
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
                print("列表页URL 其他列表页的URL 需要去重 存入search_copy1中的 ,len(urlLbList)去重前的URL  共有条数 ", len(urlLbList))
                urlLbSet = set(urlLbList)
                # myJDBC.insGJ(urlLbSet, "search_copy1")
            # 解析该页面 获取详情页的链接  并调用 craw   修改为从公司名字处获取 直接进入公司的主页面   联系方式URL 后缀需要拼接 /contact-information/   这个页面比较规范
            xpathXQUrl = "//ul[@class='extension_ul']/li/div[@class='extension_right']/p[1]/a/@href"
            XQUrlList = selector.xpath(xpathXQUrl)
            print("len(XQUrlList)  ", len(XQUrlList))
            # 去重
            XQUrlSet = set(XQUrlList)
            for sqUrl in XQUrlSet:
                sqUrl += "/contact-information/"
                # print("sqUrl", sqUrl)
                # 爬取详情页信息
                i = getUrlIsOrNo(sqUrl)
                # 判断当前是否要向青果添加ip白名单
                # setQGIp()
                if i < 1:
                    print("个数 i：： ", i)

                    craw.start(sqUrl)

                else:
                    pass
                    # print("已经有这个URL的数据了,个数 i：： ",i)
            # if coent != 0 and coent % 20 == 0:
            #     print("（20次打印一下）当前详情页计数器： ", coent)
            #
            # if coent != 0 and coent % 80 == 0:
            #     print("当前详情页页计数器： ", coent)
            #     myIP.rep_Ip()
            #     myIP.get_proxies()

            #    判断是不是有下一页
            xpathNext = "//a[@class='rollPage']/@href"

            next = selector.xpath(xpathNext)
            if next:
                # 如果再次只取到一个 （下一页|上一页）的链接  同时 该列表页的计数器 大于一的时候则退出该页面（说明本列表页没有了下一页了）
                if len(next) == 1 and cont > 1:
                    return
                else:
                    next = next[len(next) - 1]
                    print("计数器为计数器为计数器为计器为计数器数器为计数器为计数器为计数器为计数器为计数器为计数器为计数器为:", cont)
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
    """
    https://www.china.cn/search/fhealh.shtml
    https://www.china.cn/search/rrf8a.shtml
    https://www.china.cn/search/mzyh2v.shtml
    https://www.china.cn/search/fi1h9p.shtml
    https://www.china.cn/search/3t8rx.shtml
    https://www.china.cn/search/3rbb4pe.shtml
    """
    urls = [
        # "https://www.china.cn/search/fhealh.shtml",
        "https://www.china.cn/search/rrf8a.shtml",
        "https://www.china.cn/search/mzyh2v.shtml",
        "https://www.china.cn/search/fi1h9p.shtml",
        "https://www.china.cn/search/3t8rx.shtml",
        "https://www.china.cn/search/3rbb4pe.shtml"
    ]
    for url in urls:
        getListData(url, 0)

    exit()

    # 每次开始  列表页的计数器就从零开始
    myIP.rep_Ip()
    myIP.get_proxies()
    # exit()
    #
    """
    数据库中已经修改为采集过了 。。。。。
    需要重新采集的列表页
     https://www.china.cn/search/37ba.shtml?p=7
    https://www.china.cn/search/5q95mi.shtml?p=6
    https://www.china.cn/search/fxd6od.shtml?p=4
    https://www.china.cn/search/4zwx.shtml?p=12
    https://www.china.cn/search/nnkgbd.shtml?p=12
    
    
    
    https://www.china.cn/search/5a2esa.shtml?p=5
    https://www.china.cn/search/rz0u1a.shtml?p=15
    https://www.china.cn/search/5a2esa.shtml?p=10    
    https://www.china.cn/search/5af8bx.shtml?p=5
    https://www.china.cn/search/zwh7wqb.shtml?p=3
    """
    # getListData("https://www.china.cn/search/5a2esa.shtml?p=5", 0)
    print("&" * 50)

    # 从id>11741的开始 。。。。  太多了  跳着爬吧  。。。。
    # 正式开始   已经改了 查询的sql 可以改一下  直接去获取应该爬取的数据  而不再程序中再去判断
    listSearch = myJDBC.getDataDb("search")
    for search in listSearch:
        id = search[0]
        url = search[1]
        isOrNo = search[2]
        # 每次开始  列表页的计数器就从零开始
        #    print("url  ", url)
        #    print(type(isOrNo))
        if isOrNo == None or isOrNo < 2:
            # myIP.rep_Ip()
            # myIP.get_proxies()
            print("列表页url  ", url)
            getListData(url, 0)
            #     每一次处理完该条列表页 都需要修改isOrNo
            myJDBC.updateIsOrNo("search", id)
