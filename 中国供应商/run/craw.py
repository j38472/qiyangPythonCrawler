"""
爬虫代码
python 写起来的感觉真的有点怪啊   单位内容太多了  几行代码包含的太多了.....


"""
import base64
import re
from xml.dom.minidom import parse

import requests
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont
from lxml import etree

"""
接收匹配出的base64  解密出 并生成对应的woff文件 和 xml 文件
匹配出页面中的电话号 当前页面的 unic  值  并进入当前页面生成的xml 文件中  获取对应的数值  用该数值和标准xml（ztkuBZ.xml） 字体库匹配数值  
根据获取的电话号的unic值的顺序  输出电话号 和手机号 
如此字体中国供应商 字体的反爬 突破成功
"""


def saveWoffXml(result):
    """ 解密base64  """
    b64DeStr = base64.b64decode(result)
    # print(b64DeStr)
    """ 生成 woff 文件 """
    with open("ztku.woff", "wb")as f:
        f.write(b64DeStr)
    # 读取woff文件
    fonts = TTFont("ztku.woff")
    # 生成xml文件
    fonts.saveXML("ztku.xml")  # 保存成xml 文件
    pass


"""
解析xml 对比数据 
获得真正的电话
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
                print("找到了啊啊啊啊啊 !!!!!!!!!!!!!")
                dh += dhBz
                # dh.append(dhBz)
                # print("数字为:", dhBz)
                # print("data:", dataBz)
    return dh

"""
获取详情页面的电话号码的uni值 
"""


def getHTmlUni(response,strXpath):
    # 替换一下  不然会乱码 而且 现在不替换 之后也需要处理的
    response = response.replace("&#x", "uni")
    # print(response)

    # 获取本页面电话号的 unic码值
    html = etree.HTML(response)
    DH = ""

    DH = html.xpath("//input[@id=\"phone_a\"][@type=\"hidden\"]/@value")[0]
    DH = html.xpath("//input[@id=\""+strXpath+"\"][@type=\"hidden\"]/@value")[0]
    # DH = html.xpath("//div[@class=\"footer_txt\"]/p/span[@class=\"secret\"]/text()")
    # print(DH)
    DH = DH.split(";")
    # for dh in DH:
    #     print("adadasdsa     ", dh)
    return DH


"""
获取当前页面的 uni值所对应的内部数据
"""


def getuniData(DHNuiList):
    domTree = parse("ztku.xml")
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
    # 返回这个包含用于判断不表数据的数组
    return dhData


"""
url 列表页   一级列表页 1  二级列表页 2
https://www.china.cn/search/0s06jo.shtml   1
      https://www.china.cn/search/skfstg.shtml    2

"""
if __name__ == '__main__':
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    response = requests.get(url="https://www.china.cn/chuishishebei/4152876380.html", headers=headers).text
    """ 获取base64 """
    result = re.search(r"base64,(.*?)\)", response, flags=re.S).group(1)
    # 生成当前页面的woff  和xml
    saveWoffXml(result)
    # 获取当前页的的 uni
    DHNuiList = getHTmlUni(response,"phone_a")
    SJNuiList = getHTmlUni(response,"mobile")
    # 获取不变的重要数据
    dhDataList = getuniData(DHNuiList)
    sjDataList = getuniData(SJNuiList)
    dh = getDh(dhDataList)
    sj = getDh(sjDataList)
    print(dh)
    print(sj)


    # for dh in DHlist:
    #     print(dh)
