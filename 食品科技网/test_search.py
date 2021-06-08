#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> test
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-07 12:01
@Desc   ：
=================================================='''
import httpx
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

ua = UserAgent()
header = {
    'User-Agent': ua.random,
    # 'Cookie': 'UM_distinctid=178e8b45023384-0c653d29ec84b5-d7e1938-125f51-178e8b45024845; safedog-flow-item=F0B06A15A0414431C327A36A76D67417; ASP.NET_SessionId=pnd4kr45hhns2k45ddbyof45; Hm_lvt_e2689ecbba89d681b31e360cb5d08d80=1622688527,1623029717; Hm_lpvt_e2689ecbba89d681b31e360cb5d08d80=1623030910; CNZZDATA1973171=cnzz_eid%3D515471263-1618809838-%26ntime%3D1623026108'
}
proxiesNone = {
    "http://": None,
    "https://": None
}
url = "https://www.tech-food.com/"
url_lb_xpath = "//*[@id=\"c4l\"]/div/ul/li/a/@href"
name_lb_xpath = "//*[@id=\"c4l\"]/div/ul/li/a/text()"

jdbc = mySqlJdbc()

if __name__ == '__main__':
    httpx_html = httpx.get(url=url, headers=header,proxies = proxiesNone).text
    html = etree.HTML(httpx_html)
    url_lb_list = html.xpath(url_lb_xpath)
    name_lb_list = html.xpath(name_lb_xpath)
    for url,name in zip(url_lb_list,name_lb_list):
        print(url,"      ",name)
        jdbc.inSearch(url=url,name=name,dataBD="tech_food_search")