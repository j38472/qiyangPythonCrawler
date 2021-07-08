#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-06 14:48
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
url = "http://www.gucn.com/Service_CurioShop_MoreList.asp?ShopLevel={}"

data_name = "gucn_data"
gucn_httpT = "http://www.gucn.com/"

def getUtf(dataStr):
    data = ""
    for data in dataStr:
        data += data
    strgb2312 = data.encode(encoding='gb2312',errors='strict')
    utf_8_str = strgb2312.decode('UTF-8')
    return utf_8_str

def getHtmlSelector(url):
    req = requests.get(url=url, headers=header, proxies=proxiesNone)
    # print(req.text)
    # exit()
    selector = etree.HTML(req.text.encode('gbk').decode('utf-8'))
    return selector


def getXqData(url):
    url_a = gucn_httpT+url
    sele = getHtmlSelector(url_a)

    xpath_name = "//div[@class='ShopLogon_midd']/ul/li[1]/a/text()"
    xpath_hm = "//div[@class='ShopLogon_midd']/ul/li[@id='SpanMobile']/text()"
    xpath_dz = "//div[@class='ShopLogon_midd']/ul/li[9]/text()"
    xpath_zy = "//div[@class='ShopBox']/ul/li/label/a/text()"

    name_list = sele.xpath(xpath_name)
    hm_list = sele.xpath(xpath_hm)
    dz_list = sele.xpath(xpath_dz)
    zy_list = sele.xpath(xpath_zy)
    print(name_list)
    print(getUtf(name_list))
    print(getUtf(hm_list))
    print(getUtf(dz_list))
    print(getUtf(zy_list))

def getData(url):
    sele = getHtmlSelector(url)
    print(url)
    xpath_xq_list= "//div[@class='cxdp_dec']/dl/dt/a/@href"

    href_list = sele.xpath(xpath_xq_list)
    for href in href_list:
        getXqData(href)
    exit()
    pass


if __name__ == '__main__':

    url_from = "http://www.gucn.com/Service_CurioShop_MoreList.asp?CurrentBoardId=0&Search_ShopName=&Search_ShopUserName=&Search_ShopSellingItem=&Search_ShopArea=&Search_ShopClassID=&ShowPageSize=30&ShopLevel={}&page={}"

    ShopLevelList = [0, 1, 2, 3]
    pagelList = [998, 2, 58, 5]
    for shopLevel, page_max in zip(ShopLevelList, pagelList):
        # print(shopLevel,page)
        for page in range(1, page_max + 1):
            url = url_from.format(shopLevel, page)
            getData(url)

# print(req)
# selector = etree.HTML(req.text)
