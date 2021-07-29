#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> sart
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-09 16:10
@Desc   ：
=================================================='''

import time

import asyncio

from lxml import etree

import httpx

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil

proxiesNone = {
    "http://": None,
    "https://": None
}

from fake_useragent import UserAgent

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}
code_ = 302
# lxwm = "Contact/"
"""
清洗   说明 list
"""
jdbc = mySqlJdbc()
tool = MyToolUtil()
dataBD = "vipveg_data"


async def request(client, url):
    name = ""
    lxr = ""
    dz = ""
    dzxq = ""
    sj = ""
    dh = ""
    zy = ""
    try:
        resp = await client.get(url)
        # assert resp.status == 200
        text = resp.text
        if len(text) > 9000:
            # print(text)
            selector = etree.HTML(text)
            name_list = selector.xpath("//tr/td/p[1]/strong/text()")
            lxr_list = selector.xpath("//tr/td/p[2]/strong/text()")
            zy_list = selector.xpath("//td[@class='class_bg']/a/text()")

            p3_list = selector.xpath("//tr/td/p[3]/text()")
            p4_list = selector.xpath("//tr/td/p[4]/text()")
            p5_list = selector.xpath("//tr/td/p[5]/text()")
            p6_list = selector.xpath("//tr/td/p[6]/text()")
            p7_list = selector.xpath("//tr/td/p[7]/text()")
            p8_list = selector.xpath("//tr/td/p[8]/text()")
            p9_list = selector.xpath("//tr/td/p[9]/text()")

            p_all_list = []
            if p3_list:
                p_all_list.append(p3_list[0])
            if p4_list:
                p_all_list.append(p4_list[0])
            if p5_list:
                p_all_list.append(p5_list[0])
            if p6_list:
                p_all_list.append(p6_list[0])
            if p7_list:
                p_all_list.append(p7_list[0])
            if p8_list:
                p_all_list.append(p8_list[0])
            if p9_list:
                p_all_list.append(p9_list[0])

            for p in p_all_list:
                if p.find('手机：') > -1:
                    sj = p
                if p.find('电话：') > -1:
                    dh = p
                if p.find('联系地址') > -1:
                    dz = p

            dzxq_ = p_all_list[len(p_all_list) - 1]
            if dzxq_.find('：') == -1:
                dzxq = dzxq_

            if name_list:
                name = name_list[0]
            if lxr_list:
                lxr = lxr_list[0]
            for zy_ in zy_list:
                zy +=zy_+","


            print("url   ", url)
            print("name  ", name)
            print("lxr  ", lxr)
            print("dz   ", dz)
            print("dz+dzxq   ", dz + dzxq)
            print("sj  ", sj)
            print("dh   ", dh)
            print("zy   ", zy)
            jdbc.inXqDate(name=name,url=url,zy=zy,lxr=lxr,dh=dh,sj=sj,dz=dz + dzxq,dataBD=dataBD)
    except Exception as  e:
        print(e)


async def main():
    # proxies=proxiesNone,
    async with httpx.AsyncClient(headers=header) as client:
        # url_c = "http://www.chinafoods.com.cn/UserCenter/Index.aspx?uid={}"
        url_c = "http://www.vipveg.com/C/{}/Contact/"
        task_list = []
        for i in range(40, 29935 + 1):
            url = url_c.format(str(i))
            req = request(client, url)
            task = asyncio.create_task(req)
            task_list.append(task)
            if i % 10 == 0:

                # print(url_list)
                start = time.time()
                await asyncio.gather(*task_list)
                task_list = []
                end = time.time()
                print(f'异步：发送10次请求，耗时：{end - start},i的页码数为  {i}')
                if i > 30:
                    exit()


if __name__ == '__main__':
    # print('联系地址：河南 > 商丘 > 夏邑'.find('地址：'))
    # exit()
    asyncio.run(main())
