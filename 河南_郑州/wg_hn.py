#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> wg_hn
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-07 15:54
@Desc   ：
=================================================='''
import requests
from lxml import etree
from fake_useragent import UserAgent

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil
from util.ioTool import MyIoToolUtil

dataDb = "hnsj_data"

jdbc = mySqlJdbc()
ua = UserAgent()
tool = MyToolUtil()
ioTool = MyIoToolUtil()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}


def getCall(url):
    text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    sele = etree.HTML(text)
    xpaht_sj = "//ul/li[@class='f_gray'][2]/text()"
    sj_list = sele.xpath(xpaht_sj)
    return sj_list


def getQxSj(data):
    data = data.replace(" ", "")

    return data


def qxHnCall():
    hn_list = jdbc.get_BD_Data(dataBD=dataDb)
    cont = 0
    for hn in hn_list:
        print(hn)
        id = hn[0]
        url_dy = hn[1]
        sj = hn[2]
        rm_boo = False
        if sj == '':
            rm_boo = True
        if sj == 'None':
            rm_boo = True
        # if sj == "":
        #     rm_boo = True
        if rm_boo:
            jdbc.rmDataId(dataBD=dataDb, id=id)
        else:
            qx_sj = tool.set_Qx_Data(sj)
            qx_sj = tool.getsjCall(qx_sj)
            if len(qx_sj) < 10:
                jdbc.rmDataId(dataBD=dataDb, id=id)
            else:
                jdbc.setDataSj(dataBD=dataDb, sj=qx_sj, id=id)

        # cont += 1
        # if cont > 900:
        #     break


def sj_hg():
    hn_sj_list = jdbc.get_BD_Data(dataBD=dataDb)
    sj_list = []
    for hn_sj in hn_sj_list:
        # id = hn_sj[0]

        url = hn_sj[1]
        noOrYes = False
        if noOrYes == False and url.find("kaifeng") > -1:  # 开封
            noOrYes = True
        if noOrYes == False and url.find("luoyang") > -1:  # 洛阳
            noOrYes = True
        if noOrYes == False and url.find("xinxiang") > -1:  # 新乡
            noOrYes = True
        if noOrYes == False and url.find("xuchang") > -1:  # 许昌
            noOrYes = True
        if noOrYes == False and url.find("zhengzhou") > -1:  # 郑州
            noOrYes = True
        if noOrYes == False and url.find("jiaozuo") > -1:  # 焦作
            noOrYes = True
        if noOrYes:
            # sj = hn_sj[2]
            sj_list.append(hn_sj[2])
    print("开始生成    文件")
    ioTool.outXlsx(data=sj_list, dataFile="F:\\xexlsa\\hn.xlsx")


if __name__ == '__main__':

    """
    保留  郑州  新乡  开封  焦作 洛阳  许昌 

    """
    sj_hg()
    exit()

    qxHnCall()
    exit()

    list_href = ['http://www.trustexporter.com/anyang/', 'http://www.trustexporter.com/hebi/',
                 'http://www.trustexporter.com/jiaozuo/', 'http://www.trustexporter.com/kaifeng/',
                 'http://www.trustexporter.com/luohe/', 'http://www.trustexporter.com/luoyang/',
                 'http://www.trustexporter.com/nanyang/', 'http://www.trustexporter.com/pingdingshan/',
                 'http://www.trustexporter.com/puyang/', 'http://www.trustexporter.com/shangqiu/',
                 'http://www.trustexporter.com/xinxiang/', 'http://www.trustexporter.com/xinyang/',
                 'http://www.trustexporter.com/xuchang/', 'http://www.trustexporter.com/zhengzhou/',
                 'http://www.trustexporter.com/zhoukou/', 'http://www.trustexporter.com/zhumadian/',
                 'http://www.trustexporter.com/sanmenxia/']
    pn = "pn{}.htm"
    for href in list_href:
        for ym in range(1, 251):
            # print(href + pn.format(ym))
            url__ = href + pn.format(ym)
            sj_list = getCall(url__)
            if sj_list:
                for sj_data in sj_list:
                    jdbc.inHnSJ(url=url__, sj=sj_data, dataBD=dataDb)
                print(sj_list)
            else:
                break
            # exit()
