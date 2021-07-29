#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-05-31 10:41
@Desc   ：https://www.chyxx.com/minglu/list_12832.html
=================================================='''
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

jdbc = mySqlJdbc()

ua = UserAgent()

proxiesNone = {
    "http": None,
    "https": None
}

urlLBCS = "/minglu/list_{}.html"
url = "https://www.chyxx.com"
dataBD = "chyxx_com"

GJZList = {"水产", "海产", "土产", "包子", "凉皮", "罐头", "消毒",
           "灌装", "封尾", "旋盖", "贴标", "包装", "输送", "喷码", "封口", "速冻",
           "咖啡", "调味", "汉堡", "消毒", "清洗", "灭菌", "切片", "花生", "咖喱", "添加剂", "膨化", "搅拌",
           "农", "葵", "豆", "薯", "果", "菌", "肉", "稻"
    , "猪", "牛", "羊", "鱼", "鸟", "鸡", "蛋", "米", "麦", "酱", "谷", "鸭", "鹅", "兔", "瓜", "食"
    , "饼", "菜", "粮", "餐", "素", "骨", "枣", "栗", "面", "糖", "奶", "饺", "茄", "麸", "糯",
           "炒", "煎", "炸", "炖", "煮", "泡", "煸", "煲", "烘", "蒸", "烤", "炖", "烧", "腌", "熏",
           "汤", "粥", "料", "渔", "筋", "萝", "姜", "蒜", "葱", "辣", "冰", "浆", "糕", "厨", "盐",
           "糖", "笋", "炉", "榨", "碗", "屠", "吃", "腐", "禽", "畜", "麻"  "馍", "馒", "蹄", "饮", "盆", "勺", "筷", "锅", "叉",
           "蜜", "孜", "馅", "丸", "罐", "汁水", "蘸", "醒", "酥", "椒", "茶", "酸", "菇"
           }

"""
清洗详情数据的函数
"""


def getData_QX(dataList):
    i = 0
    indx = 0;
    retDataList = None
    for data in dataList:
        indx += 1
        # print(data)
        if data.find('：') > -1:
            i += 1
            if i == 2:
                retDataList = dataList[indx - 1:]
    return retDataList


def getHtml(pathurl):
    global url
    time.sleep(2.5)
    t = int(time.time())
    print(pathurl)
    header = {
        'User-Agent': ua.random,
        'path': pathurl,
        'cookie': 'Hm_lpvt_92877e89b7b6871e4dbbf66d5839d430={}; Hm_lpvt_303541224a8d81c65040eb747f5ee614={}'.format(
            str(t), str(t + 1))
    }
    url_ = url + pathurl
    req = requests.get(url=url_, headers=header, proxies=proxiesNone, timeout=14,verify=False)
    reqHtml = req.text
    # print(reqHtml)
    # exit()
    return reqHtml


"""
清洗   说明 list
"""


def get_SM(list_sm):
    reList = list()
    for sm in list_sm:
        reList.append(sm.replace("\u3000", ""))
    return reList


def get_DZDZ(DZDZ_List):
    pass
    dz_All = ""
    for dz in DZDZ_List:
        dz_All += dz
    return dz_All


def get_xq_data(K_List, V_list, Qdz, url_path, name):
    global url
    lxr = ""
    dh = ""
    sj = ""
    dz = ""
    zy = ""
    cent = 0
    for my_data_k in K_List:
        if my_data_k.find("地址") > -1:
            dz = Qdz + V_list[cent].replace("：", "")
        if my_data_k.find("电话") > -1:
            dh = V_list[cent].replace("：", "")
        if my_data_k.find("经营范围") > -1:
            zy = V_list[cent].replace("：", "")
        cent += 1
    jdbc.inXqDate(name, url_path, zy, lxr, dh, sj, dz, dataBD)


def getXQ(pathurl):
    HtmlXQ = getHtml(pathurl)
    # print(HtmlXQ)
    selector = etree.HTML(HtmlXQ)
    # 说明
    K_List = selector.xpath("//*[@id=\"contentBody\"]/p/strong/text()")
    # 大致地址
    DZDZList = selector.xpath("//div[@id='contentBody']/p/a/text()")
    # 数据
    dataList = selector.xpath("//*[@id='contentBody']/p/text()")
    # 名字
    name = selector.xpath("//h1[@class='title']/text()")
    if len(name) > 0:
        name = name[0]
    # exit()
    K_List = K_List[1:]
    K_List = get_SM(K_List)
    V_list = getData_QX(dataList)
    dz = get_DZDZ(DZDZList)
    get_xq_data(K_List, V_list, dz, pathurl, name)


if __name__ == '__main__':
    for i in range(192+1, 12832 + 1):
        print("<><><><><><<><><><><>",i,"<><><><><><<><><><><>")
        ymStr = str(i)
        path = urlLBCS.format(ymStr)
        HtmlLB = getHtml(path)
        selector = etree.HTML(HtmlLB)
        xqymURlList = set(selector.xpath("//div[@class='compnay-list']/div/h3/a/@href"))
        for pathurl in xqymURlList:
            isOrNo = jdbc.getUrlGs(pathurl, dataBD)
            if isOrNo < 1:
                getXQ(pathurl)
            else:
                print("已经有了这个url的数据了", pathurl)
            print("--------------------------------------------------------------------------------------------")
        # if i == 102:
        #     exit()
