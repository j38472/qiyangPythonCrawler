#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> data_start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-16 10:23
@Desc   ：
=================================================='''
import re
from time import sleep

from myJDBC.jdbc import mySqlJdbc
import requests
from lxml import etree
from fake_useragent import UserAgent

from util.TOOL import MyToolUtil

dataDB_search = "agronet_search"
dataDB_data = "agronet_data"

ua = UserAgent()

proxiesNone = {
    "http": None,
    "https": None
}
url_q = "http://www.agronet.com.cn/"

jdbc = mySqlJdbc()
tool = MyToolUtil()



def getHeard():
    sjc13 = tool.get_SJC13()
    sjc10 = int(sjc13 / 1000) + 1
    # print(sjc13)
    # print(sjc10)
    # exit()
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        'Cookie': "Cookie: agronetCookie=D98233C159EF3AEA333D883B971C1FCA9B6F08A7476FD809; bdshare_firstime={}; Hm_lvt_8f396c620ee16c3d331cf84fd54feafe={}; Hm_lpvt_8f396c620ee16c3d331cf84fd54feafe={}".format(
            sjc13, sjc10, sjc10),

    }
    return header


def getSel(url):
    header = getHeard()
    # , proxies=proxiesNone
    req = requests.get(url=url, headers=header, proxies=proxiesNone)
    req.encoding = "utf-8"
    req_text = req.text
    # print(req_text)
    selector = etree.HTML(req_text)
    return selector


def getXQSel(url):
    sleep(1.25)
    header = getHeard()
    getUrl = url  # + "Contact.html"
    # , proxies=proxiesNone
    req = requests.get(url=getUrl, headers=header, proxies=proxiesNone)
    req.encoding = "utf-8"
    req_text = req.text
    # print(req_text)
    selector = etree.HTML(req_text)
    return selector


def getXQ(url, name, zy):
    sj = ""
    dh = ""
    dz = ""
    sel = getXQSel(url)
    data_V_xpath = "//ul[@class='left_tel']/li/span/text()"
    data_V_xpath_two = "//dd/ul/li/span/text()"


    data_V_list_c = sel.xpath(data_V_xpath)

    if len(data_V_list_c)<2:
        data_V_list_c = sel.xpath(data_V_xpath_two)

    lxr = data_V_list_c[0]
    dz_list = []
    for data_V in data_V_list_c:
        if sj == None or sj == "":
            sj = re.search(r"([0-9]{11})", data_V, flags=re.S)
        if dh == None or dh == "":
            dh = re.search(r"([0-9]{2,4}-[0-9]{7,9})", data_V, flags=re.S)
        dz_list.append(data_V)
    if sj:
        sj = sj.group(1)
        dz_list.remove(sj)

    if dh:
        dh = dh.group(1)
        dz_list.remove(dh)

    dz_list.remove(lxr)

    for data_dz_c in dz_list:
        dz+=tool.set_Qx_Data(data_dz_c)


    # print(name)
    # print(url)
    # print(lxr)
    # print(sj)
    # print(dh)
    # print(zy)
    # print(dz)

    jdbc.inXqDate(name=name,url=url,zy=zy,lxr=lxr,dh=dh,sj=sj,dz=dz,dataBD=dataDB_data)



def getLBList(url):
    sel = getSel(url)
    xq_url_list = "//span/h3/strong/a/@href"
    xq_name_list = "//span/h3/strong/a/text()"
    xq_zy_list = "//span/div/text()"
    url_list = sel.xpath(xq_url_list)
    name_list = sel.xpath(xq_name_list)
    zy_list_ = sel.xpath(xq_zy_list)
    zy_list = []
    for zy in zy_list_:
        zy = tool.set_Qx_Data(zy)
        if len(zy) > 1:
            zy_list.append(zy)

    for url, name, zy in zip(url_list, name_list, zy_list):
        getXQ(url, name, zy)
        # print(url)
        # print(name)
        # print(zy)


if __name__ == '__main__':
    # getXQ(url="http://24log.chacuo.net/my",name="",zy="")
    # exit()

    """
    0753-2232028
www.mzjfseed.com
13502333042
    """
    # v = "13502333042"
    # sj = re.search(r"([0-9]{11})",v , flags=re.S)
    # print(sj.group(1))
    # exit()

    # http://www.agronet.com.cn/c/503200/
    # http://www.agronet.com.cn/c/92324/
    # getXQ(url="http://www.agronet.com.cn/c/503200", name="", zy="")
    # exit()

    lb_list = jdbc.getLbUrl(dataDB_search)

    for lb in lb_list:
        id = lb[0]
        url_h = lb[1]
        url = url_q + url_h
        getLBList(url)
        exit()