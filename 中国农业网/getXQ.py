#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> getXQ
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/5/24 9:47
@Desc   ：
=================================================='''
from time import sleep
from fake_useragent import UserAgent

import requests
from lxml import etree
import re

from 中国农业网.mySqlJdbc import mySqlJdbc

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}
jdbc = mySqlJdbc()
wyXpath = "//ul[@id='ContentPlaceHolder1_PagingHelper1']/span/a/@href"
lburl = "http://gp.zgny.com.cn/Companys/Page_{}.shtml"
url = "http://gp.zgny.com.cn/Companys/index.shtml"
boo = True


def start(c):
    print("启动start")
    try:
        # req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=5)
        # html = req.text
        # selector = etree.HTML(html)
        # wy = selector.xpath(wyXpath)
        # ym = wy[len(wy) - 1]
        # ym = re.search(r"Page_([0-9]*)", ym).group(1)
        # # print(ym)
        # # print(type(ym))
        # ym = int(ym)
        # print(type(ym))
        # print(ym)
        for i in range(1, 5174 + 1):
            # 445
            if i > 181 and i>c:
                print(i)
                strYm = str(i)
                lburlz = lburl.format(strYm)
                sleep(2.5)
                # print(i)
                requ = requests.get(url=lburlz, headers=header, proxies=proxiesNone, timeout=14)
                htmllburlz = requ.text
                # print(htmllburlz)
                # exit()

                selector = etree.HTML(htmllburlz)
                xqymURl = selector.xpath("//li/div/div[1]/a[1]/@href")
                for xqymurl in xqymURl:

                    isOrNo = jdbc.getIsOrNo(xqymurl)
                    if len(isOrNo) == 0:
                        print(lburlz)
                        print(xqymurl)
                        sleep(2)
                        reqxqymurl = requests.get(url=xqymurl, headers=header, proxies=proxiesNone, timeout=14).text
                        xpathName = "/html/body/div[7]/div[9]/div[1]/span/text()"
                        xpathLxr = "/html/body/div[7]/div[9]/div[1]/div/ul/li[1]/text()"
                        xpathDh = "/html/body/div[7]/div[9]/div[1]/div/ul/li[3]/text()"
                        xpathSj = "/html/body/div[7]/div[9]/div[1]/div/ul/li[2]/text()"
                        xpathZy = "/html/body/div[7]/div[10]/a/text()"
                        xpathDz = "/html/body/div[7]/div[9]/div[1]/div/ul/li[8]/text()"
                        selectorreqxqymurl = etree.HTML(reqxqymurl)
                        name = selectorreqxqymurl.xpath(xpathName)
                        lxr = selectorreqxqymurl.xpath(xpathLxr)
                        dh = selectorreqxqymurl.xpath(xpathDh)
                        sj = selectorreqxqymurl.xpath(xpathSj)
                        zy = selectorreqxqymurl.xpath(xpathZy)
                        dz = selectorreqxqymurl.xpath(xpathDz)
                        # print(name)
                        # print(lxr)
                        # print(dh)
                        # print(sj)
                        # print(zy)
                        # print(dz)
                        if name:
                            name = str(name[0])
                        if lxr:
                            lxr = str(lxr[0])
                        if dh:
                            dh = str(dh[0])
                        if sj:
                            sj = str(sj[0])
                        if zy:
                            zy = str(zy[0])
                        if dz:
                            dz = str(dz[0])
                        # print(name)
                        # print(lxr)
                        # print(dh)
                        # print(sj)
                        # print(zy)
                        # print(dz)
                        if len(name) == 0 and len(lxr) == 0 and len(dh) == 0 and len(sj) == 0 and len(zy) == 0 and len(
                                dz) == 0:
                            xpathName = "/html/body/div[6]/div[2]/div[1]/text()"
                            xpathLxr = "/html/body/div[6]/div[2]/div[2]/div[1]/ul/li[2]/text()"
                            xpathDh = "/html/body/div[6]/div[2]/div[2]/div[1]/ul/li[4]/a/text()"
                            xpathSj = "/html/body/div[6]/div[2]/div[2]/div[1]/ul/li[3]/a/text()"
                            xpathZy = "/html/body/div[6]/div[2]/div[2]/div[2]/p/text()"
                            xpathDz = "//div[6]/div[2]/div[2]/div[1]/ul/li[1]/text()"
                            name = selectorreqxqymurl.xpath(xpathName)
                            lxr = selectorreqxqymurl.xpath(xpathLxr)
                            dh = selectorreqxqymurl.xpath(xpathDh)
                            sj = selectorreqxqymurl.xpath(xpathSj)
                            zy = selectorreqxqymurl.xpath(xpathZy)
                            dz = selectorreqxqymurl.xpath(xpathDz)
                            if name:
                                name = str(name[0])
                            if lxr:
                                lxr = str(lxr[0])
                            if dh:
                                dh = str(dh[0])
                            if sj:
                                sj = str(sj[0])
                            if zy:
                                zy = str(zy[0])
                            if dz:
                                dz = str(dz[0])

                        if len(zy) > 200:
                            zy = zy[0:200]
                        if len(dh) == 0 and len(sj) == 0:
                            xpathDh = "//div[@class='JianJie_02']/div[@class='jjLeft']/ul/li[4]/text()"
                            xpathSj = "//div[@class='JianJie_02']/div[@class='jjLeft']/ul/li[3]/text()"
                            dh = selectorreqxqymurl.xpath(xpathDh)
                            sj = selectorreqxqymurl.xpath(xpathSj)
                            if dh:
                                dh = str(dh[0])
                            if sj:
                                sj = str(sj[0])
                        # print(xqUrl)
                        jdbc.inXqDate(url=xqymurl, name=name, lxr=lxr, dh=dh, sj=sj, zy=zy, dz=dz)
    except TimeoutError:
        start(i)
        pass
    except Exception:
        start(i)
        pass


if __name__ == '__main__':
    start(0)
