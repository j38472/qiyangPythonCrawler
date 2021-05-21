#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> myRequests
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/28 14:41
@Desc   ：
=================================================='''
from time import sleep

import requests
from functools import partial

from requests.adapters import HTTPAdapter
from urllib3.exceptions import ProxyError

from 中国供应商.run import myIP, myJDBC
from fake_useragent import UserAgent

from 中国供应商.run.myIP import que_Ip
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError
from urllib3.exceptions import ProxyError as urllib3_ProxyError

proxiesNone = {
    "http": None,
    "https": None
}
ua = UserAgent()
header = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Host": "httpbin.org",
    # "Upgrade-Insecure-Requests": "1",
    # "X-Amzn-Trace-Id": "Root=1-60891a49-3617976f4355a9990e445588",
    #
    # "authority": "www.china.cn",
    # "referer": "https://www.china.cn/",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
#     Hm_lvt_60030dce41abe35fdcca4338a88126a7=1616742365; china_uv=159cf539ae72f5b08c378bc3f21dcb29
#     "cookie": "Hm_lvt_60030dce41abe35fdcca4338a88126a7=1616742365; china_uv=159cf539ae72f5b08c378bc3f21dcb29",
    'User-Agent': ua.random,
}
cont = 0
def getHtmlData(url):
    global cont
    # print("当前页面的URL  ",url)
    html="0"
    pmeta = myJDBC.getSqlProxyMeta()
    proxyMeta = pmeta[0][0]
    proxies = {
        # 根据请求方式（http/https）的不同，可以选择不同的代理
        # "http": proxyMeta,
        "https": proxyMeta
    }

    # {'http': 'http://183.155.111.253:46264'}
    # , proxies=proxies
    # 证书问题

    # 控制爬虫频率
    sleep(2.5)

    # requests.packages.urllib3.disable_warnings()
    # requests.get = partial(requests.get, verify=False, proxies=proxies)
    #
    # s = requests.Session()
    # s.mount('http://', HTTPAdapter(max_retries=3))
    # s.mount('https://', HTTPAdapter(max_retries=3))

    try:
        res = requests.get(url=url, proxies=proxies,headers=header, timeout=5)
        res.encoding = 'gbk'
        code = res.status_code
        html = "111111111111"
        html = res.text
        # print("html::",html)
        global cont
        print("当前请求页面的ip：：    ", proxies,"           ","状态码为:: ", code)
        # print(html)


        if code!=200 and cont < 3:
            print("封IP了啊啊啊啊啊啊")
            cont += 1
           # 更新资源
           #  requests.post(url="https://proxy.qg.net/replace?Key=F58B5B03A518E080", proxies=proxiesNone)
            myIP.rep_Ip()
            myIP.get_proxies()
            sleep(6)
            getHtmlData(url)

    except Exception as ce:
        if (isinstance(ce.args[0], MaxRetryError) and
            isinstance(ce.args[0].reason, urllib3_ProxyError)):
            # oops, requests should have handled this, but didn't.
            # see https://github.com/kennethreitz/requests/issues/3050
            print("Error")
            myIP.rep_Ip()
            myIP.get_proxies()
            print("Error")
            # getHtmlData(url)


    # proxies = {"http": None, "https": None}
    # resp = requests.get(url=url,proxies=proxies)
    # if len(html) < 3 :
    #     getHtmlData(url)
    return html



def getIPIS(url):
    data = que_Ip()
    # 代理服务器
    proxyHost = data["IP"]  # ip地址
    proxyPort = data["port"]  # 端口号

    proxyMeta = "%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }

    # pip install -U requests[socks] socks5代理
    # proxyMeta = "socks5://%(host)s:%(port)s" % {
    # "host" : proxyHost,
    # "port" : proxyPort,
    # }

    proxies = {
        'http': 'http://' + proxyMeta,
        'https': 'https://' + proxyMeta,
    }
    print(proxies)
    resp = requests.get(url, proxies=proxies)
    # resp = requests.get(url)
    print("-------------------------")
    print(resp.status_code)
    print(resp.text)

if __name__ == '__main__':
    # myIP.rep_Ip()
    # myIP.rep_Ip()
    # myIP.get_proxies()
    # url = "https://httpbin.org/ip"
    url = "https://www.china.cn/taiwan/z8p7c4.shtml"

    # getHtmlData(url)
    html = getHtmlData(url)
    print(html)