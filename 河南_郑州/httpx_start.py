#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> httpx_start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-06 15:14
@Desc   ：
=================================================='''
import asyncio
import re
import time
import requests
from fake_useragent import UserAgent
from lxml import etree

import httpx

from myJDBC.jdbc import mySqlJdbc

proxiesNone = {
    "http://": None,
    "https://": None
}

url_C = "http://www.gucn.com/Service_Shop_Detail.asp?Id={}"

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}

jdbc = mySqlJdbc()
dataBD_data = ""


def getdata(url):
    # url = "http://shop.suning.com/jsonp/70080826/shopinfo/shopinfo.html?callback=shopinfo"
    req = requests.get(url=url, headers=header, proxies=proxiesNone)
    return req


def getUtf(dataStr):
    data = ""
    for data in dataStr:
        data += data
    utf_8 = data.encode('utf-8')
    return utf_8


async def request(client, url):
    try:
        resp = await client.get(url, timeout=3)
        # assert resp.status == 200
        text = resp.text
        # gb2312

        sele = etree.HTML(text)
        print(url)

        xpath_name = "//div[@class='ShopLogon_midd']/ul/li[1]/a/text()"
        xpath_hm = "//div[@class='ShopLogon_midd']/ul/li[@id='SpanMobile']/text()"
        xpath_dz = "//div[@class='ShopLogon_midd']/ul/li[9]/text()"
        xpath_zy = "//div[@class='ShopBox']/ul/li/label/a/text()"

        name_list = sele.xpath(xpath_name)
        hm_list = sele.xpath(xpath_hm)
        dz_list = sele.xpath(xpath_dz)
        zy_list = sele.xpath(xpath_zy)
        print(name_list)
        print(getUtf(name_list))
        print(getUtf(hm_list))
        print(getUtf(dz_list))
        print(getUtf(zy_list))

    except Exception as  e:
        print(e)


async def main():
    async with httpx.AsyncClient(proxies=proxiesNone) as client:
        """
            71411410
            70725278
            70080826
            70069021
        """
        task_list = []
        star_gs = 300  # 初始商铺唯一id 值
        end_gs = 69000  # 最大商铺唯一id 值
        # star_gs = 69021  # 初始商铺唯一id 值
        # end_gs = 69100  # 最大商铺唯一id 值
        c_gs = 400  # 每次异步请求 包共有多个次请求
        for i in range(star_gs, 99999):
            url = url_C.format(str(i))
            req = request(client, url)
            task = asyncio.create_task(req)
            task_list.append(task)
            if i % c_gs == 0:
                # print(url_list)
                url_list = []
                start = time.time()
                await asyncio.gather(*task_list)
                end = time.time()
                print(f'异步：发送{c_gs}次请求，耗时：{end - start}')
                time.sleep(2.5)
                exit()
            # if i == end_gs:
            #     exit()


if __name__ == '__main__':
    r= "¾Û±¦ÌÃ"
    data = r.encode("gb18030").decode("utf-8")
    print(data)
    # asyncio.run(main())
