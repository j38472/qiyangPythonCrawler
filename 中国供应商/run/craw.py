'''=================================================
@Project -> File   ：qiyangPythonCrawler -> craw
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/25 14:04
@Desc   ：爬虫代码
            python 写起来的感觉真的有点怪啊   单位内容太多了  几行代码包含的太多了.....
            接收匹配出的base64  解密出 并生成对应的woff文件 和 xml 文件
            匹配出页面中的电话号 当前页面的 unic  值  并进入当前页面生成的xml 文件中  获取对应的数值  用该数值和标准xml（ztkuBZ.xml） 字体库匹配数值
            根据获取的电话号的unic值的顺序  输出电话号 和手机号
            如此字体中国供应商 字体的反爬 突破成功
================================================='''

import base64
import re
import time
import requests

from xml.dom.minidom import parse
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont
from lxml import etree

from 中国供应商.run import myJDBC, myIP
from 中国供应商.run.myRequests import getHtmlData

nameWoff = "ztku.woff"
nameXml = "ztku.xml"


def saveWoffXml(result):
    """ 解密base64  """
    b64DeStr = base64.b64decode(result)
    # print(b64DeStr)
    """ 生成 woff 文件 """
    with open(nameWoff, "wb")as f:
        f.write(b64DeStr)
    # 读取woff文件
    fonts = TTFont(nameWoff)
    # 生成xml文件
    fonts.saveXML(nameXml)  # 保存成xml 文件


"""
获取详情页面的电话号码的uni值 
"""


def getHTmlUni(response, isNo):
    # 替换一下  不然会乱码 而且 现在不替换 之后也需要处理的
    response = response.replace("&#x", "uni")
    # print(response)

    # 获取本页面电话号的 unic码值
    html = etree.HTML(response)
    # print(html)
    # 获取本页面电话 uni
    # DhOrSj = set(re.findall(Re, response))
    # r"'(.*?)'"
    sjordh = ""
    if isNo == 0:
        sjOrDh = re.search(r"手机：(.*?)</span>", response, flags=re.S)
        if sjOrDh:
            sjOrDh = sjOrDh.group(1)
    else:
        sjOrDh = re.search(r"电话：(.*?)</span>", response, flags=re.S)
        if sjOrDh:
            sjOrDh = sjOrDh.group(1)
    # print("---------------------------------------------")
    # print(rJ)
    # print()

    # # DH = html.xpath("//input[@id=\"phone_a\"][@type=\"hidden\"]/@value")[0]
    # xpathDh = "//input[@id=\"" + strXpath + "\"][@type=\"hidden\"]/@value"
    # print(xpathDh)
    # DH = html.xpath(xpathDh)
    # # DH = html.xpath("//div[@class=\"footer_txt\"]/p/span[@class=\"secret\"]/text()")
    # print(DH)
    if sjOrDh:
        sjordh = sjOrDh.split(";")
    # for dh in sjOrDh:
    #     print("adadasdsa     ", dh)
    return sjordh


"""
解析xml 根据页面的uni拿到xmlz中的不变数据  对比数据 
获得真正的电话或者手机号码
并返回
"""


def getDh(dhDataList):
    # 标准xml
    domTreeBz = parse("ztkuBZ.xml")
    # 文档根元素
    rootNode = domTreeBz.documentElement
    # print(rootNode.nodeName)
    # 获取所有 CharString 标签元素
    customers = rootNode.getElementsByTagName("CharString")
    # dh = []
    dh = ""
    for dhData in dhDataList:
        for customer in customers:
            dhBz = customer.getAttribute("name")
            dataBz = customer.childNodes[0].data
            # 判断两个的字体长度是否一样  先要消除掉空格  如果一样长的话 就说明找到对应的手机号码了
            if len(dhData.replace(" ", "")) == len(dataBz.replace(" ", "")):
                # print("找到了啊啊啊啊啊 !!!!!!!!!!!!!")
                dh += dhBz
                # dh.append(dhBz)
                # print("数字为:", dhBz)
                # print("data:", dataBz)
    return dh


"""
获取当前页面的 uni值所对应的内部数据
"""


def getuniData(DHNuiList):
    domTree = parse(nameXml)
    # 文档根元素
    rootNode = domTree.documentElement
    # print(rootNode.nodeName)
    # 获取所有 CharString 标签元素
    customers = rootNode.getElementsByTagName("CharString")
    # 用于存储电话号内部不变的数据
    dhData = []
    # 遍历当前页面的 uni
    for dhuni in DHNuiList:
        # 遍历从当前页的获取到的xml 的 charString 标签列表
        for customer in customers[1:]:
            # 获取当前charString标签内部 的name 所对应的值 也就是 uni
            dh = customer.getAttribute("name")
            # 获取当前charString标签内部 的data  也就是不变的数据
            data = customer.childNodes[0].data
            # 如果相等 则说明是该uni所对应的 不变数据
            if dhuni == dh:
                # 将不变的数据存入列表中
                dhData.append(data)
                # print("数字为:", dh)
                # print("data:", data)
    # 返回这个包含用于判断不变数据的数组
    return dhData


"""
传来一个详情页的url  解析该详情页面  获取电话号和手机号
"""


def start(url):
    dh = ""
    sj = ""
    name = ""
    lxr = ""
    dz = ""
    zy = ""
    response = getHtmlData(url)
    if response != 404:
        # print(response)
        dataXpaht = "//script[@type=\"text/javascript\"]/@data-gisjs"

        xpathDz = "//div/div[2]/div[2]/p[1]/span[3]/text()"
        xpathName1 = "//a[@class=\"company-name\"]/text()"
        xpathName2 = "//a[@class=\"corpname\"]/text()"
        xpathlxr = "//div[1]/div[2]/dl/dd[1]/div/span[1]/text()"
        xpathZy1 = "//*[@id=\"signboard\"]/div[1]/div[1]/h2/text()"
        xpathZy2 = "//div[@class=\"business\"]/text()"
        selector = etree.HTML(response)
        nameList = selector.xpath(xpathName1)
        lxrList = selector.xpath(xpathlxr)
        zyList = selector.xpath(xpathZy1)
        if len(zyList) == 0:
            zyList = selector.xpath(xpathZy2)
        if len(nameList) == 0:
            nameList = selector.xpath(xpathName2)

        if zyList:
            zy = zyList[0]
        if lxrList:
            lxr = lxrList[0]
        if nameList:
            name = nameList[0]
        # print(lxrList)
        # print(len(lxrList))
        # print(type(lxrList))

        data = selector.xpath(dataXpaht)
        # print(type(data))
        # print(len(data))
        if data:
            data = data[0]
            data = data.split(",")
            for d1 in data:
                # print(d1)
                d2 = d1.split(":")
                # print(d2[0])
                if d2[0].find('address') > -1:
                    # print("地址找到了")
                    dz = d2[1]
                    # print(d2[1])

        # print((dzList))
        # print((nameList))
        # print((lxrList))
        # print((zyList))

        # print(response)
        """ 获取base64 """
        result = re.search(r"base64,(.*?)\)", response, flags=re.S)
        # 有些页面他就没有 数字 所以也叫没有  字体库
        if result:
            result = result.group(1)
            # 生成当前页面的woff  和xml
            saveWoffXml(result)
            # 获取当前页的的 uni
            DHNuiList = getHTmlUni(response, 1)
            SJNuiList = getHTmlUni(response, 0)
            # 获取不变的重要数据
            # 获取对比 产出 号码
            if DHNuiList:
                dhDataList = getuniData(DHNuiList)
                dh = getDh(dhDataList)
            if SJNuiList:
                sjDataList = getuniData(SJNuiList)
                sj = getDh(sjDataList)

        # print("--------------------------------------------------------------")
        name = name.replace("'", "")
        dz = dz.replace("'", "")
        zy = zy.replace("'", "")
        lxr = lxr.replace("'", "")
        # 现在的速度是 3-7秒左右 一个解析出一条数据  还行.....

        # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        #
        # print("name 公司名字  ",name)
        # print("lxr 联系人  ",lxr)
        # print("dh 电话  ",dh)
        # print("sj 手机  ",sj)
        # print("dz 地址  ",dz)
        # print("zy  主营  ",zy)
        myJDBC.addDate(dataDb="cn_china_cn", name=name, lxr=lxr, dh=dh, sj=sj, zy=zy, dz=dz, url=url)
        print("--------------------------------------------------------------")
        if name == "" and lxr == "" and dh == "" and sj == "" and dz == "" and zy == "":
            print("全都是空，更换ip")
            myIP.rep_Ip()
            myIP.get_proxies()


# 这个主要用于测试的   {'http': 'http://183.155.109.40:59603'}
if __name__ == '__main__':
    print()
    # # 获取列表页表中所有数据
    # list_search = myJDBC.getDataDb("search")
    # for search in list_search:
    #
    #     id = search[0]
    #     url = search[1]
    #     isOrNo = search[2]
    #     print(id)
    #     print(url)
    #     print(isOrNo)
    #     if isOrNo == 0:
    #         start(url)
    # #   每次执行完本列表页  则修改下数据
    #     myJDBC.updateIsOrNo("search",id)
    # https://jiushenjiuhang.cn.china.cn
    # https://www.china.cn/hunningtujiaobanc/3747179508.html
    # proxie = myIP.get_proxies()

    start("https://shop1368412296764.cn.china.cn/contact-information/")

    # for dh in DHlist:
    #     print(dh)
"""
列表页的  链接 有两种  加个判断
普通的  直接去搞页码 去抓取数据   --  有可能会有页码 但是没有数据  所以需要加判断
有分类的 判断下  一共多少数据   再去细分
"""
