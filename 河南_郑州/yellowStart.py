#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> yellowStart
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-17 14:29
@Desc   ：
=================================================='''

"""
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-0-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0-page-1.html

https://product.yellowurl.cn/search-htm-list-0-kw--typeid-0-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-2-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-1-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-3-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-5-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-4-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
    https://product.yellowurl.cn/search-htm-list-0-kw--typeid-4-kw--fields-0-catid-1-fromdate--todate--areaid-11-minprice--maxprice--order-0-page-2.html
    
    
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-1-kw--fields-0-catid-2-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-2-kw--fields-0-catid-3-fromdate--todate--areaid-11-minprice--maxprice--order-0.html

https://product.yellowurl.cn/search-htm-list-0-kw--typeid-1-kw--fields-0-catid-5480-fromdate--todate--areaid-11-minprice--maxprice--order-0.html
https://product.yellowurl.cn/search-htm-list-0-kw--typeid-2-kw--fields-0-catid-38-fromdate--todate--areaid-11-minprice--maxprice--order-0.html

"""
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


# url = "https://httpbin.org/ip"
# req = requests.get(url=url, headers=header, proxies=proxiesNone, verify=False)
# print(req)
# selector = etree.HTML(req.text)


def getHTml(url):
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, verify=False)
        return req.text
    except Exception as  e:
        print("getHTml   ", e)


if __name__ == '__main__':
    count = 0
    url = "http://search.114chn.com/searchresult.aspx?key=%e9%83%91%e5%b7%9e&type=1&pattern=1&page={}"