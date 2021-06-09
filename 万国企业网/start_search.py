#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start_search
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-08 16:29
@Desc   ：
=================================================='''
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
dataBD="trustexporter_search"

def get_lb_two():
    Urllist = jdbc.getLbUrl(dataBD)
    for url_ in Urllist:
        id = url_[0]
        url = url_[1]
        requ_text = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=7, allow_redirects=False).text
        etreeHtml = etree.HTML(requ_text)
        urlC = etreeHtml.xpath("//span[@class='youbian']/a/@href")
        print(url)
        print(urlC)
        jdbc.setSearchUrl(id=id,url=urlC[0],dataBD=dataBD)


def get_lb_One():
    url = "https://www.trustexporter.com/"
    url_list_xpath = "//dl/dd/a/@href"
    name_list_xpath = "//dl/dd/a/@title"

    requ_text = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=7,allow_redirects=False).text
    etreeHtml = etree.HTML(requ_text)
    url_list = etreeHtml.xpath(url_list_xpath)
    name_list = etreeHtml.xpath(name_list_xpath)
    for k,v in zip(url_list,name_list):
        jdbc.inSearch(url=k,name=v,dataBD=dataBD)



if __name__ == '__main__':
    get_lb_two()