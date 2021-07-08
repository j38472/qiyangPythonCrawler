#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> hnzz
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-06 17:04
@Desc   ：
=================================================='''
import re
from time import sleep

import requests
from fake_useragent import UserAgent
from lxml import etree
import base64

from fontTools.ttLib import TTFont
import httpx

from myJDBC.jdbc import mySqlJdbc

"""

马可波罗   页面结构有点复杂

https://www.chyxx.com/minglu/410000/list_2.html    不用写  之前的数据  就有了

http://www.agronet.com.cn/Company/List_ar410000_p2.html

http://b2b.huangye88.com/henan/

http://www.trustexporter.com/zhengzhou/



"""

url_list = ["http://www.agronet.com.cn/Company/List_ar410000_p1.html", "http://www.trustexporter.com/zhengzhou/"]

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}
jdbc = mySqlJdbc()



def getHtmlSel(url):
    # sleep(0.69)
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone)
        sele = etree.HTML(req.text)
        return sele
    except Exception as e:
        print(e)


def getHtmlText(url):
    req = requests.get(url=url, headers=header, proxies=proxiesNone)
    return req.text


nameWoff = "ztku.woff"
nameXml = "ztku.xml"
dataDb = "hnsj_data"


def saveWoffXml(response):
    result = re.search(r"base64,(.*?)\)", response, flags=re.S).group(1)
    """ 解密base64  """
    b64DeStr = base64.b64decode(result)
    # print(b64DeStr)
    """ 生成 woff 文件 """
    with open(nameWoff, "wb")as f:
        f.write(b64DeStr)
    # 读取woff文件
    fonts = TTFont(nameWoff)
    # 生成xml文件
    fonts.saveXML(nameXml)  # 保存成xml 文件
    pass


def getsjh(url):
    xpath = "//span[@class=\"secret\"]/text()"
    xpath_list = '//span[@class =  "secret"]/text()'

    text = getHtmlText(url)
    saveWoffXml(text)
    text = text.replace("&#x", "uni")
    sele = etree.HTML(text)
    sj_list = sele.xpath(xpath_list)
    print(text)
    print(sj_list)
    exit()


def reGetsj(data):
    try:
        sj = re.search(r"1[0-9]{10}", data, flags=re.S).group(0)
        return sj
    except Exception as e:
        print(e)
    return ""


def getAppSj(url):
    seleX = getHtmlSel(url)
    if seleX:
        sjList = seleX.xpath('//a/@href')
        sjS = ""
        for sj_ in sjList:
            sjS += sj_
        sj = reGetsj(sjS)
        return sj


def getb2bxqData(url):
    seleX = getHtmlSel(url)
    name_list_xpath = '//*[@itemprop="name"]/text()'
    href_list_xpath = '//*[@itemprop="name"]/@href'
    name_list = seleX.xpath(name_list_xpath)
    href_list = seleX.xpath(href_list_xpath)

    for name, href in zip(name_list, href_list):
        sj = reGetsj(href)

        if len(sj) == 11:
            jdbc.inHnSJ(url=href, sj=sj, dataBD=dataDb)
        else:
            if href.find("http://b2b") > -1:
                '''
                http://b2b.huangye88.com/qiye2491311/
                http://b2b.huangye88.com/qiye2491311/company_contact.html
                http://m.huangye88.com/qiye/2491311/contact.html
                '''
                url_end = "contact.html"
                url_start = "http://m"
                url__ =  href.replace("http://b2b",url_start)
                url__ = url__+url_end
                sj = getAppSj(url__)
                # print(sj)
                # print(urlzj_app)
                # exit()
                jdbc.inHnSJ(url=url__, sj=sj, dataBD=dataDb)
            else:
                gsdataurlW = "company_contact.html"
                gsdataurlW_app = "m/contact.html"
                # print(name, href)
                urlzj_app = href + gsdataurlW_app
                # print(urlzj)
                # print(urlzj_app)
                sj = getAppSj(urlzj_app)
                # print(sj)
                # print(urlzj_app)
                # exit()
                jdbc.inHnSJ(url=urlzj_app, sj=sj, dataBD=dataDb)
                # getsjh(urlzj)
                # seleX = getHtmlSel()
                # '''
                # http://kaidijx.b2b.huangye88.com/company_contact.html
                # http://m.huangye88.com/qiye_kaidijx/contact.html
                # '''

def getb2b():
    url = "http://b2b.huangye88.com/henan/"
    seleX = getHtmlSel(url)
    xpath_lb_name = "//div/ul[@class='clearfix']/li/a/text()"
    xpath_lb_href = "//div/ul[@class='clearfix']/li/a/@href"
    lb_href_list = seleX.xpath(xpath_lb_href)
    lb_name_list = seleX.xpath(xpath_lb_name)
    # print(len(lb_href_list))
    # print(len(lb_name_list))
    # print(lb_href_list)
    # print(lb_name_list)

    '''
        河南机械企业名录 http://b2b.huangye88.com/henan/jixie/
     河南工程机械企业名录 http://b2b.huangye88.com/henan/gongcheng/
        河南环保企业名录 http://b2b.huangye88.com/henan/huanbao/
        河南五金企业名录 http://b2b.huangye88.com/henan/wujin/
        河南电气企业名录 http://b2b.huangye88.com/henan/dianqi/
        河南机床企业名录 http://b2b.huangye88.com/henan/jichuang/
    '''
    xyy_ON_yes = True
    for name, href in zip(lb_name_list, lb_href_list):
        print(name, href)
        for i in range(1, 51):
            url_C = href + "pn{}/".format(str(i))
            print(url_C)
            getb2bxqData(url_C)
            print("-----------" * 5)
            # exit()
        print("<><><><><><><>" * 19)


if __name__ == '__main__':
    # print(reGetsj("javascript:void(0);http://yg2021.b2b.huangye88.com/m/renzheng.htmltel:13674981708mqqwpa://im/chat?chat_type=wpa&uin=534240838&version=1&src_type=web&web_src=huangye88.com"))
    # exit()
    # print(getHtmlText("http://yg2021.b2b.huangye88.com/m/contact.html"))
    # getsjh("http://yg2021.b2b.huangye88.com/company_contact.html")
    getb2b()
    # getb2bxqData("http://b2b.huangye88.com/henan/jixie/")
