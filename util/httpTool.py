#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> httpTool
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-17 15:03
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
requests.packages.urllib3.disable_warnings()


class MyHttpToolUtil:
    def getReq_one_none(self, url):
        try:

            req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=3, verify=False)
            return req
        except Exception as e:
            print("getReq_one_none    ", e)

    def getSele_one_none(self, url):
        try:

            req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=3, verify=False)
            # print(req.text)
            # exit()
            sele = etree.HTML(req.text)
            return sele
        except Exception as e:
            print("getSele_one_none    ", e)

    def getHtml_one_none(self, url):
        try:
            req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=6, verify=False)
            # print(req.text)
            return req.text
        except Exception as e:
            print("getHtml_one_none    ", e)
        pass

    def dow_img(self, url, name):
        # print(url)
        # time.sleep(1.5)
        try:
            req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=6, verify=False)
            # 拼接图片名
            file_name = name + ".jpg"
            # print(file_name)
            # 将图片存入本地
            fp = open(file_name, 'wb')
            # 写入图片
            fp.write(req.content)
            fp.close()
        except Exception:
            print("cccc")
