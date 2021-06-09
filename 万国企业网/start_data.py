#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start_data
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-09 9:09
@Desc   ：
=================================================='''
from time import sleep
import re

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}

proxiesNone = {
    "http": None,
    "https": None
}
jdbc = mySqlJdbc()
tool = MyToolUtil()
dataBD_data = "trustexporter_data"
dataBD_search = "trustexporter_search"
url_h_pj = "pn{}.htm"


def get_html(url):
    sleep(2.5)

    req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=7, allow_redirects=False)
    req_text = req.text
    return req_text


def get_xq_html(url):
    sleep(2.5)
    header_xq = {
        'User-Agent': ua.random,
        # 'Host': 'aagigf.cn.trustexporter.com',
        # 'Cookie':'Hm_lvt_908376e0e856e8b64f7af6081984a5d1 = 1623218519;Hm_lpvt_908376e0e856e8b64f7af6081984a5d1 = 1623218519;SMTKEFUXT_12565_LastActiveTime = 1623218520;SMTKF_visitor_id_12565 = 345937946;SMTKEFUXT_12565_AutoInviteNumber = 0;SMTKEFUXT_12565_ManualInviteNumber = 0',
    }
    # , proxies=proxiesNone
    req = requests.get(url=url, headers=header_xq, timeout=7, allow_redirects=False)
    req_text = req.text
    return req_text


def get_xq(url, name, zy):
    xq_lxr_dh_sj_xpath = "//div[6]/ul/li/text()"
    xq_dz_xpath = "//tr[2]/td[2]/text()"
    xq_html = get_xq_html(url)
    # print("详情页面的长度   ", len(xq_html))
    xq_etreeHtml = etree.HTML(xq_html)

    xq_lxr_dh_sj_list = xq_etreeHtml.xpath(xq_lxr_dh_sj_xpath)
    xq_dz_list = xq_etreeHtml.xpath(xq_dz_xpath)
    # print(len(xq_lxr_dh_sj_list))
    # print(len(xq_dz_list))
    #
    # print(xq_lxr_dh_sj_list)
    # print(xq_dz_list)
    dz = ""
    dzxq = ""
    dh = ""
    sj = ""
    lxr = ""
    for lxr_dh_sj in xq_lxr_dh_sj_list:
        if lxr_dh_sj.find("地址：") > -1:
            dzxq = lxr_dh_sj
        if lxr_dh_sj.find("电话：") > -1:
            dh = lxr_dh_sj
        if lxr_dh_sj.find("手机：") > -1:
            sj = lxr_dh_sj
        if lxr_dh_sj.find("联系人：") > -1:
            lxr = lxr_dh_sj
    for dzqz in xq_dz_list:
        if dzqz.find('\r') > 1 or dzqz.find('\n') > 1:
            dz = dzqz
            break
    dz = dz + dzxq
    # print(dh)
    # print(sj)
    # print(lxr)

    dz = tool.set_Qx_Data(dz)
    dh = tool.set_Qx_Data(dh)
    sj = tool.set_Qx_Data(sj)
    lxr = tool.set_Qx_Data(lxr)
    zy = tool.set_Qx_Data(zy)
    jdbc.inXqDate(dataBD=dataBD_data, name=name, url=url, lxr=lxr, dh=dh, sj=sj, dz=dz, zy=zy)
    print("--------------------" * 20)


def get_lb(url):
    print(url)
    xq_url_xpath = "//tr/td[1]/ul/li[1]/a/@href"
    xq_name_xpath = "//tr/td[1]/ul/li[1]/a/@title"
    xq_zy_xpath = "//tr/td[1]/ul/li[2]/text()"

    lb_html = get_html(url)

    etreeHtml = etree.HTML(lb_html)

    xq_url_list = etreeHtml.xpath(xq_url_xpath)
    xq_name_list = etreeHtml.xpath(xq_name_xpath)
    xq_zy_list = etreeHtml.xpath(xq_zy_xpath)
    # print(len(xq_url_list))
    for url, name, zy in zip(xq_url_list, xq_name_list, xq_zy_list):
        # get_lb(url, name, zy)
        pass
    # print(url)
    # print(name)
    # print(zy)


def start_list(url):
    lb_html = get_html(url)
    etreeHtml = etree.HTML(lb_html)
    zys_xpath = "//div[@class='pages']/cite/text()"

    # 下一页
    zys_list_str = etreeHtml.xpath(zys_xpath)
    xiy_url_ym = ""
    for zys_str in zys_list_str:
        print(zys_str)
        xiy_url_re = re.search(r"/([0-9]*?)页", zys_str, flags=re.S)

        if xiy_url_re:
            xiy_url_ym = xiy_url_re.group(1)
    xiy_url_ym = int(xiy_url_ym)
    for ym in range(1, xiy_url_ym + 1):
        print(url + url_h_pj.format(ym))
        get_lb(url + url_h_pj.format(ym))


"""
433    https://qiye.trustexporter.com/s32817/
434    https://qiye.trustexporter.com/s32807/
460    https://qiye.trustexporter.com/s27312/
464    https://qiye.trustexporter.com/s27494/
506    https://qiye.trustexporter.com/s28550/
520    https://qiye.trustexporter.com/s27685/
521    https://qiye.trustexporter.com/s27700/
527    https://qiye.trustexporter.com/s28410/
"""

if __name__ == '__main__':
    # print(get_xq_html("http://aagigf.cn.trustexporter.com/"))
    # exit()

    get_lb("https://qiye.trustexporter.com/s27494/")
    exit()

    db = jdbc.get_BD_Search(dataBD_search)
    for d in db:
        id = d[0]
        url = d[2]
        print(id, "  ", url)
