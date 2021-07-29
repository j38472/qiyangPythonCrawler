#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start_data
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-07 14:50
@Desc   ：这代码 写的 好恶心  自己都没没眼看  脏眼睛  草
=================================================='''
import httpx
import time

import requests
from fake_useragent import UserAgent
from parsel import Selector
from myJDBC.jdbc import mySqlJdbc

ua = UserAgent()

proxiesNone = {
    "http://": None,
    "https://": None
}
jdbc = mySqlJdbc()
url_t = "https://biz.tech-food.com"
coent = 0

async def run_url_get_data(url_list):
    async with httpx.AsyncClient() as client:
        for url in url_list:
            try:
                print(url)
                response = await client.get(url=url)
                selector = Selector(response.text)
                print(selector)
                exit()
            except Exception:
                run_url_get_data(url)


def getHrader():
    t = str(int(time.time()))
    header = {
        'User-Agent': ua.random,
        'Cookie': 'Hm_lvt_cbe9e63b773c71f054072095d4bd3864=1622688445,1623038351; Hm_lpvt_cbe9e63b773c71f054072095d4bd3864={}'.format(t),
        # 'Connection': 'close',
        # 'Host': 'biz.tech - food.com',

    }
    return header


def get_data():
    pass


def get_xyy_url(html_lb):
    url_xyy_xpath_name = "//div[@class='div708'][2]/div[@class='number']/a/text()"
    url_xyy_xpath_url = "//div[@class='div708'][2]/div[@class='number']/a/@href"
    url_xyy_list_name = html_lb.xpath(url_xyy_xpath_name)
    url_xyy_list_url = html_lb.xpath(url_xyy_xpath_url)
    # print(len(url_xyy_list_url))
    for nameKV, urlKV in zip(url_xyy_list_name, url_xyy_list_url):
        name = nameKV.get()
        url = urlKV.get()
        if name.find('下一页') > -1 and url != None:
            return url


def get_html_Selector(url):
    # time.sleep(2.5)

    try:
        header = getHrader()
        # , proxies=proxiesNone
        httpx_get = httpx.get(url=url, headers=header, proxies=proxiesNone)
        # print(httpx_get.text)

        print(httpx_get.status_code)
        # print(type(httpx_get.status_code))
        # exit()
        if httpx_get.status_code == 200:
            httpx_html = httpx_get.text
            # 15041  报错
            # print(len(httpx_html))
            html_Selector = Selector(httpx_html)
            return html_Selector
        else:
            get_html_Selector(url)
    except httpx.ReadError:
        get_html_Selector(url)


def get_xq(url):
    html_sel = get_html_Selector(url)
    data_xpath = "//*[@id=\"sbody\"]/div[1]/div[11]"

    data = html_sel.xpath(data_xpath)
    print(data)
    # jdbc.inXqDate(name=name, url=url, zy=zy, lxr=lxr, dh=dh, sj=sj, dz=dz, dataBD="tech_food_data")
    # print(url)
    # print(name)
    # print(lxr)
    # print(dh)
    # print(sj)
    # print(zy)
    # print(dz)


def get_lb(url):
    url_xq_xpath = "//div[@class='ly_0']/div[@class='cb']/a/@href"
    html_lb = get_html_Selector(url)
    url_lb_list = set(html_lb.xpath(url_xq_xpath))
    for url_xq in url_lb_list:
        if url_xq.get().find("http") > -1:
            url_xq_get = url_xq.get()
            isOrNo = jdbc.getUrlGs(url=url_xq_get, dataBD="tech_food_data")
            if isOrNo < 1:
                get_xq(url_xq_get)
    xyy = get_xyy_url(html_lb)
    if xyy:
        xyy_all = url_t + xyy
        get_lb(xyy_all)


def get_list():
    pass


if __name__ == "__main__":

    # url = "https://win.tech-food.com/ft394094/"
    # get_xq(url)
    # exit()
    #
    # url = "https://biz.tech-food.com/info/pl4/"
    # get_lb(url)
    # exit()
    url_lb_list = jdbc.getLbUrl("tech_food_search")
    # print(len(url_lb_list))

    for url in url_lb_list:
        url = url[1]

        get_lb(url)

        # asyncio.run(run_url_get_data(url_xq_list))
