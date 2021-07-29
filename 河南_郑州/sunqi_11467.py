#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> sunqi_11467
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-12 14:57
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
dataDb1 = "hnsj_data_copy1"
dataDb2 = "hnsj_data_copy2"
dataDb3 = "hnsj_data_copy3"


def get_url_text(url):
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, verify=False)
        return req.text
    except Exception as e:
        print("get_url_sele    ", e)


def get_url_sele(url):
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, verify=False)
        sele = etree.HTML(req.text)
        return sele
    except Exception as e:
        print("get_url_sele    ", e)


def xqHrefList(url, ym_s):
    # print(get_url_text(url))
    print(url)

    sele = get_url_sele(url)
    xpath = "//div[@class='f_l']/h4/a/@href"
    href_list = sele.xpath(xpath)

    # print(href_list)
    if href_list:
        for href in href_list:
            if href.find("//") == 0:
                href = "http:" + href
                # print(href)
                xq_text = get_url_text(href)
                sj_set = set(tool.getSjAllList(xq_text))
                if sj_set:
                    for sj in sj_set:
                        sjGs1 = jdbc.getSjGs(sj=sj, dataBD=dataDb1)
                        sjGs2 = jdbc.getSjGs(sj=sj, dataBD=dataDb2)
                        sjGs3 = jdbc.getSjGs(sj=sj, dataBD=dataDb3)
                        if sjGs1 < 1 and sjGs2 < 1 and sjGs3 < 1:
                            jdbc.inHnSJ(url=href, sj=sj, dataBD=dataDb3)
                print(sj_set)

        """
            没啥用了
        xpath_href_xyy = "//div[@class='pages']/a/@href"
        href_xyy_list = sele.xpath(xpath_href_xyy)
        print(url)
        print(href_list)
        print(href_xyy_list)
        ym_href = href_xyy_list[len(href_xyy_list) - 1]
        print(ym_href)
        reString = r"p([0-9]{1,2})\.htm"
        ym_max = tool.getReData(ReStr=reString, data=ym_href)
    
        url_T_reString = ""
        ym_max = tool.getReData(ReStr=reString, data=url)
        """

        """
        由于页码的样式过多  这里统一全部按照25页处理    跳出页码循环使用则是在 抓不到详情页的hrefList 的时候
        全部都在   -{}.htm  之前加上-{}
        
        """
        for ym in range(ym_s, 26):
            rep_pd = tool.getReData0("-\d.htm", url)
            print(rep_pd)
            if rep_pd:
                url_x = url.replace(rep_pd, "-{}.htm".format(ym))
            else:
                url_x = url.replace(".htm", "-{}.htm".format(ym))
            ym += 1
            xqHrefList(url_x, ym)
            # print(url_x)
            # xqHrefList()

    exit()


def getYM_max():
    pass


def getLbUrl(url):
    xpath_hrefOne = "//ul[@class='listtxt']/li/dl/dd/a/@href"
    sele = get_url_sele(url)
    href_list_one = sele.xpath(xpath_hrefOne)
    print(href_list_one)
    ym_s = 2
    for href in href_list_one:
        # sele_lb = get_url_sele(href)
        # yema_list = sele_lb.xpath(xpath_href_xyy)
        # print("yema_list     ", yema_list)
        # exit()
        # if yema_list:
        #     ym = yema_list[len(yema_list) - 1]
        #     print(yema_list)
        #     print("ym    ", ym)
        #     exit()
        xqHrefList(href, ym_s)


if __name__ == '__main__':
    # url = "http://www.11467.com/zhengzhou/"
    url_list_dm= ["http://www.11467.com/zhengzhou/","http://www.11467.com/xinxiang/","http://www.11467.com/luoyang/"]
    """
    新乡
    开封
    焦作
    洛阳
    许昌
    
    """
    for href_url in url_list_dm:
        print("主入口URL!!!!!!!!!!!!",href_url)
        getLbUrl(href_url)
    exit()
    # print(get_url_text(url))
