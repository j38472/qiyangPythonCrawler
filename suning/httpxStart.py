#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> httpxStart
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-30 9:18
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
code_ = 302

url_T = "http://shop.suning.com/jsonp/{}/shopinfo/shopinfo.html?callback=shopinfo"
id = 70000000

ua = UserAgent()
header = {
    'User-Agent': ua.random,
    # 'Cookie': 'tradeLdc=NJYH; tradeMA=71; _snma=1%7C162493069073585067%7C1624930690735%7C1624930693438%7C1624930694928%7C4%7C1; _snvd=1624930681478I7bAo/zqrT5; _snmc=1; _snsr=localhost%3A63342%7Creferral%7C%7C%7C; _snzwt=THtBDo17a556aa84bk9fj2c84; _df_ud=70b3a7c1-9584-400d-acac-25bfd3bb2f3d; _device_session_id=p_68361e6a-2555-4d07-a044-d23d3a569a75; hm_guid=b306566f-4a03-4bcb-8a03-cb3877281922',
    # 'Referer': 'http://localhost:63342/',
}

KW = "/keyword/getKeyword.html?callback=getKeyword"
jdbc = mySqlJdbc()
dataBD_data = "sn_data"


def getKW(url):
    # print("getKW   开始")
    jsonp = getdata(url=url)
    if jsonp.status_code == 200:
        parse_data_dice = eval(parse_jsonp(jsonp.text))
        zy = ""
        for key, value in parse_data_dice.items():
            # print(key, "  :   ", value)
            for v in value:
                zy += v + ","
        return zy


def parse_jsonp(jsonp_str):
    try:
        return re.search('^[^(]*?\((.*)\)[^)]*$', jsonp_str).group(1)
    except:
        raise ValueError('Invalid JSONP')


def getdata(url):
    # url = "http://shop.suning.com/jsonp/70080826/shopinfo/shopinfo.html?callback=shopinfo"
    req = requests.get(url=url, headers=header, proxies=proxiesNone)
    return req


# 主营业务  有两种获取方式
# 进入商铺主页时候  获取的所有的商品类目的名称  作为该商铺的主营业务 的xpath 规则
xapth_zy_lm = "//ul[@class='sf-navlist clearfix']/li/a/text()"


def get_zy(url):
    text = getdata(url).text
    selector = etree.HTML(text)
    zy_list = selector.xpath(xapth_zy_lm)
    zy = ""
    # print(zy_list)
    # print(url)
    for data in zy_list:
        # print(data)
        zy += data
    return zy


def get_dict(jsonp):
    # print(parse_jsonp(jsonp))
    parse_data_dice = eval(parse_jsonp(jsonp))
    # print(type(parse_data_dice))

    indexUrl = ""
    companyName = ""
    shopName = ""
    telPhone = ""
    companyAddress = ""
    supplierCode = ""
    zy = ""
    for key, value in parse_data_dice.items():
        if key == 'indexUrl':
            indexUrl = 'http:' + value
            # print(key, '   :    ', indexUrl)
        if key == "companyName":
            companyName = value
            # print(key, '   :    ', value)
        if key == "shopName":
            shopName = value
            # print(key, '   :    ', value)
        if key == "telPhone":
            telPhone = value
            # print(key, '   :    ', value)
        if key == "companyAddress":  # 地址
            companyAddress = value
            # print(key, '   :    ', value)
        if key == "supplierCode":  #
            supplierCode = value

            # print(key, '   :    ', value)
    if telPhone != "" and indexUrl != "http://shop.suning.com//index.html":
        zy = get_zy(indexUrl)
        if zy == "":
            url_zy_hotWord = "{}/jsonp/{}/keyword/getKeyword.html?callback=getKeyword".format(indexUrl, supplierCode)
            print(url_zy_hotWord)
            zy = getKW(url_zy_hotWord)

        # print("<<<<<<<<<<<<<<<<" * 8)
        # print("zy   主营业务", zy)
        # print(" indexUrl     URL   " + indexUrl)
        # print("companyName+shopName   公司名字      " + companyName + shopName)
        # print("telPhone      电话号码   " + telPhone)
        # print(" companyAddress     地址   " + companyAddress)

        jdbc.inXqDate(name=companyName + shopName,url=indexUrl,zy=zy,lxr="",dh=telPhone,sj=telPhone,dz=companyAddress,dataBD=dataBD_data)
        # print("-----------------------" * 8)

    else:
        pass
        # print("空的啊  宝贝  啊哈哈哈哈!")
        # if key == "":
        #     print(key, '   :    ', value)


async def request(client, url):
    try:
        resp = await client.get(url, timeout=3)
        # assert resp.status == 200
        text = resp.text
        # print(text)
        # exit()
        get_dict(text)
    except Exception as  e:
        # print(e)
        print("request  EEEEEEEEEEEEE ")


async def main():
    async with httpx.AsyncClient(proxies=proxiesNone) as client:
        """
            71411410
            70725278
            70080826
            70069021
        """
        task_list = []
        star_gs = 60000  # 初始商铺唯一id 值
        end_gs = 69000  # 最大商铺唯一id 值
        # star_gs = 69021  # 初始商铺唯一id 值
        # end_gs = 69100  # 最大商铺唯一id 值
        c_gs = 100  # 每次异步请求 包共有多个次请求
        for i in range(star_gs, 9999999):
            url = url_T.format(str(i + id))
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
            # if i == end_gs:
            #     exit()


if __name__ == '__main__':
    asyncio.run(main())

    # print(url)





    """
    http://ip.h5.ri01.sycdn.kuwo.cn/d780e10ce76db194ed8f0c0c4da6d329/60dbdecd/resource/n3/58/80/1702582647.mp3
    http://ip.h5.ri01.sycdn.kuwo.cn/d780e10ce76db194ed8f0c0c4da6d329/60dbdecd/resource/n3/58/80/1702582647.mp3
    http://ip.h5.ri01.sycdn.kuwo.cn/d780e10ce76db194ed8f0c0c4da6d329/60dbdecd/resource/n3/58/80/1702582647.mp3
    
    
    
    """
