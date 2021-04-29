#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> fromData
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/25 14:04
@Desc   ：用于给中国供应商发送搜索关键词的的方法 获取关键词的拼接目录  关键词一定要多  这个网站非常的大  一定要够多
        最后把这个关键词在该网站中的搜索字段全部保存起来
        每一个最多有三十页  一页最多有40个

        思路:::::  这个网站有点大   思路必须搞清楚

        获取列表页的数据时候 如果返回的状态码是 404 则说明本关键词 在本网站中没有相关搜索

        RE : search/[^\s]*.shtml 获取一个页面中所有的列表页面的链接关键词

        获取其他列表页从 "您可以找"  中 有很多列表页的链接  这个不要进入 先抓取存起来  还需要进行判断

        如果列表页中 包含分类的 例如 省份 适用范围 种类等等  则需要调用对应的方法 先判断一共有多少条  条数越多  没进入下一级细分 则判断一次  如果大于1200 则在向下一级细分 (例子1)反之开始采集信息  则将分类的更加精细

        例子1
        省份有三个       共有3600条
        进入其中一个省份   判断有多少条  大于1200 则开始下线以及细分
        进入适用范围   判断有多少条  小于1200  则不进入下一层细分领域  直接开始采集
        有点像是递归


不需要再去找请求  关键词了
下面的  relatedwords 里面 全都有

https://www.china.cn/relatedwords/  里面有一个 食品相关的目录 还有一个机械食品 相关


https://www.china.cn/relatedwords/niuroulei.html     ---- 牛肉类
https://www.china.cn/relatedwords/yangroulei.html    ---- 羊肉类


从列表页进入详情页时  应该从每个表单的的标题进入 而不是公司名字进入  从公司名字处的URL 可能是自己的页面 而从标题中进入的情况下 初步预计都有 中国供应商  的头部和尾部文件  尾部文件中有电话号和地址等信息  可以减少爬虫无效操作 提高效率


准备:::
1 先把 relatedwords 相关搜索的关键词 全部拿到   再用自己准备的一些关键词去请求 获取关键词的   然后看看是不是全部都有
2 进入列表页  主营产品在列表页
列表页有两种
        一中是包含细分 的各种属性的    根据例子1 处理
        一中是不包含的  根据本列表页一共出现的相关数据 来判断要不要进入其他的相关列表页



=================================================='''
import datetime
from urllib.parse import quote, unquote

from fake_useragent import UserAgent
from lxml import etree

import requests
from requests.adapters import HTTPAdapter

import re

from 中国供应商.run import myJDBC

import myIP

gjc = [
    # 肉类 后缀是肉
    "牛肉", "羊肉", "兔肉", "猪肉", "鸡肉", "鸭肉", "驴肉", "鹅肉", "虾肉", "鱼肉", "羊肉", "羊肉", "羊肉", "腊肉",

    "海产", "水产", "海鲜", "农产", "海产", "海产", "海产",
    # 蛋类
    "鸡蛋", "鸭蛋", "鸵鸟蛋", "鹌鹑蛋",
    # 米面类
    "鸡蛋", "鸭蛋", "鸵鸟蛋", "鹌鹑蛋",
    "羊肉",
    # 各种调味品相关的
    "调味", "香料",

    "食品添加剂"
    , "腌菜", "酱菜", "蔬菜", "腌菜", "腌菜"

    # 饮品
    , "饮料", "酱菜", "腌菜", "腌菜", "腌菜"
    # 食品机械
    , "饮料", "酱菜", "腌菜", "腌菜", "腌菜"
]
ua = UserAgent()
oRA = True
proxies = []
def getHtmlData(url):
    global proxies
    if len(proxies)== 0:
        proxies.append(myIP.get_proxies())
    proxie = proxies[0]
    resp = requests.get(url=url, proxies=proxie)
    code = resp.status_code
    html = resp.text
    cont = 0
    if code == 520 and cont<5:
        cont+=1
        # 更新资源
        myIP.rep_Ip()
        proxies = []
        proxies.append(myIP.get_proxies())
        getHtmlData(url)
    else:
        return html


def getData(url, cont):

    print("当前URL为::  ", url)
    cont += 1
    response = getHtmlData(url)
    # print(response)
    selector = etree.HTML(response)
    li_list = selector.xpath("//div[@class='yBanner']/div[@class='yBannerList']/div[@class='yKeyword']/a/@href")
    print(len(li_list))
    # # 获取所有下级页面链接
    # for l in li_list:
    #     print(l)

    #    判断是不是有下一页
    xpathNext = "//a[@class='rollPage']/@href"
    next = selector.xpath(xpathNext)
    # 如果再次只取到一个 下一页的链接  则判断下 该列表页的计数器 大于一的时候则退出该页面
    if next:
        if len(next) == 1 and cont > 1:
            return
        next = next[len(next) - 1]
        print("计数器为:", cont)
        # myJDBC.insGJ(li_list, "search")
        if next:
            getData(next, cont)
            print()


"""
生成列表页表单的链接
"""


def getListData(str):
    nameList = myJDBC.getDataDb("relatedwords")
    for n in nameList:
        url = """https://www.china.cn/relatedwords/%s.html""" % (n[1])
        print(url)


"""
获取所有的 relatedwords 后接子分类的 关键词 
"""


def getGJZList():
    # 食品/饮料/餐饮生鲜   整个分类的全部
    xpath = "//div[2]/div[15]/div/p/a/@onclick"
    # 机床/机械设备 ---> 食品、饮料加工及餐饮行业设备
    xpath1 = "//div[2]/div[3]/div[2]/p/a/@onclick"
    # 机床/机械设备 ---> 农业机械
    xpath2 = "//div[2]/div[3]/div[4]/p/a/@onclick"
    # 机床/机械设备 ---> 锅、炉及配件
    xpath4 = "//div[2]/div[3]/div[21]/p/a/@onclick"
    # 机床/机械设备 ---> 制冷设备
    xpath4_2 = "//div[2]/div[3]/div[25]/p/a/@onclick"
    # 数码/安防/印刷/家电 ---> 厨房电器
    xpath6 = "//div[2]/div[4]/div[49]/p/a/@onclick"
    # 化工 ----> 食品添加剂
    xpath3 = "//div[2]/div[18]/div[2]/p/a/@onclick"
    # 化工 ----> 香料、香精
    xpath3_2 = "//div[2]/div[18]/div[20]/p/a/@onclick"
    # 汽摩及配件/包装/能源 ---> 食品包装
    xpath5 = "//div[2]/div[9]/div[23]/p/a/@onclick"





    headers = {'User-Agent': ua.random}
    url = "https://www.china.cn/relatedwords/"
    response = requests.get(url, headers=headers).text
    Selector = etree.HTML(response)
    # 企业信息获取
    li_list = Selector.xpath(xpath3_2)
    li_list1 = Selector.xpath(xpath4_2)
    # li_list2 = Selector.xpath(xpath2)
    # li_list3 = Selector.xpath(xpath3)
    # li_list4 = Selector.xpath(xpath4)
    # li_list5 = Selector.xpath(xpath5)
    # li_list6 = Selector.xpath(xpath6)

    # print(len(li_list))
    # print(len(li_list1))
    # print(len(li_list2))
    # print(len(li_list3))
    # print(len(li_list4))
    # print(len(li_list5))
    # print(len(li_list6))

    listAll = [li_list, li_list1]
    # 存储结果
    listDataAll = []
    i = 0
    for list in listAll:
        for data in list:
            print(data)
            rJ = re.search(r"'(.*?)'", data, flags=re.S).group(1)
            print(rJ)
            i += 1
            print(i)
            listDataAll.append(rJ)
    print(len(listDataAll))
    # myJDBC.insGJ(listDataAll, "relatedwords")

    # data.
    # print(li_list)

    # print(response.text)


if __name__ == '__main__':
    getGJZList()


    # https://www.china.cn/relatedwords/zhiwuyou.html?p=2
    # getListData("cccc")

    list = myJDBC.getDataDb("relatedwords")
    for data in list:
        # if data[2]==None or data[2]==0:
            url = """http://www.china.cn/relatedwords/%s.html"""%(data[1])
            getData(url, 0)
        # myJDBC.updateIsOrNo("relatedwords",data[0])

    # url = "https://www.china.cn/relatedwords/niu.html?p=3"
    # getData(url,0)

    # for g in gjc:
    #     gquote = quote(g)
    #     print(gquote)
    #     print(unquote(gquote))
