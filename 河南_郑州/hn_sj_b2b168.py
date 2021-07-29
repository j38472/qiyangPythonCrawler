#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> hn_sj_b2b168
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-12 10:14
@Desc   ：

=================================================='''

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

ua = UserAgent()
jdbc = mySqlJdbc()
tool = MyToolUtil()
ioTool = MyIoToolUtil()

header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}

url_T = "https://www.b2b168.com/"
url_W = "l-{}.html"
dataDb = "hnsj_data_copy1"

def get_url_text(url):
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, verify=False)
        return req.text
    except Exception as e:
        print("get_url_sele    ",e)



def get_url_sele(url):
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, verify=False)
        sele = etree.HTML(req.text)
        return sele
    except Exception as e:
        print("get_url_sele    ",e)

def getSj(url):
    if url.find('//') == 0:
        url = "http:" + url
    # print(url)
    text = get_url_text(url)
    sj_list = tool.getSjAllList(text)
    if sj_list:
        sj_set = set(sj_list)
        print(sj_set)
        if set:
            for sj in sj_set:
                jdbc.inHnSJ(url=url, sj=sj, dataBD=dataDb)


def getXq(url_):
    for ym in range(1, 26):
        url = url_T + url_ + url_W.format(ym)
        print(url)
        sele = get_url_sele(url)
        if sele:
            href_list = sele.xpath("//ul[@class='list']/li/div[@class='biaoti']/a/@href")
            if href_list:
                for href in href_list:
                    getSj(href)
                # exit()
            else:
                break


def getLb():
    url = "https://www.b2b168.com/henan-zhengzhou-huagong/"
    selector = get_url_sele(url)
    if selector:
        href_list = selector.xpath("//ul[@class='app_list1'][2]/li/a/@href")
        print(href_list)
        for href in href_list:
            getXq(href)


if __name__ == '__main__':
    getLb()
