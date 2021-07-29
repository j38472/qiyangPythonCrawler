#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> hn_zb_zgazxxw
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-08 16:15
@Desc   ：
=================================================='''
from time import sleep

import requests
from lxml import etree
from fake_useragent import UserAgent

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

dataDb = "hnsj_data_copy1"

jdbc = mySqlJdbc()
ua = UserAgent()
tool = MyToolUtil()
ioTool = MyIoToolUtil()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}
url_T = "http://www.zgazxxw.com/"


def getSele(url):
    sleep(3.69)
    text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    sele = etree.HTML(text)
    return sele


def getText(url):
    sleep(0.69)
    text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    return text


url = "http://www.zgazxxw.com/hn-010001-{}.html"
"""
河南 
http://www.zgazxxw.com/hn-000001-4.html   
郑州:
http://www.zgazxxw.com/hn-010001-1.html

"""


def getCallsj(url):
    text = getText(url=url)
    reOut = tool.getSjList(data=text)
    if reOut:
        for sj in reOut:
            jdbc.inHnSJ(url=url,sj=sj,dataBD=dataDb)
    # print(reOut)


def startLb(url):
    # sele = getSele("http://www.zgazxxw.com/hn-010001-1.html")
    sele = getSele(url)
    xpath_xq = "//div[@class='list_zb02']/table/tbody/tr/td/a/@href"
    xq_href_list = sele.xpath(xpath_xq)
    for xq_href in xq_href_list:
        # print(url_T + xq_href)
        getCallsj(url_T + xq_href)
        # print("<><><><>"*16)

if __name__ == '__main__':
    # getCallsj("http://www.zgazxxw.com//zbpd/zhongbgg/202107/7540539.php")
    #
    # exit()

    for ym in range(0, 2736 + 1):
        print(url.format(ym))
        startLb(url.format(ym))

"""
河南招标网
"""
