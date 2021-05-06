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

from 中国供应商.run import myIP, myJDBC
from fake_useragent import UserAgent

from 中国供应商.run.myIP import que_Ip

ua = UserAgent()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "X-Amzn-Trace-Id": "Root=1-60891a49-3617976f4355a9990e445588",
    'User-Agent': ua.random
}
def getHtmlData(url):
    print("当前页面的URL  ",url)


    pmeta = myJDBC.getSqlProxyMeta()
    pmeta[0][0]
    proxyMeta = pmeta[0][0]
    # print(proxyMeta)
    proxies = {
        "http": proxyMeta,
    }
    print(proxies)
    # {'http': 'http://183.155.111.253:46264'}
    # , proxies=proxies
    resp = requests.get(url=url, proxies=proxies)

    # proxies = {"http": None, "https": None}
    # resp = requests.get(url=url,proxies=proxies)

    resp.encoding = 'gbk'
    code = resp.status_code
    html = resp.text
    # print("html::",html)
    cont = 0
    print("状态码为:: ", code)
    # print(html)
    sleep(3)
    if code == 520 and cont < 5:
        print("封IP了啊啊啊啊啊啊")
        cont += 1
        sleep(6)
        # 更新资源
        myIP.rep_Ip()
        myIP.get_proxies()
        getHtmlData(url)
    else:
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
    url = "http://httpbin.org/ip"
    # getHtmlData(url)
    getHtmlData(url)