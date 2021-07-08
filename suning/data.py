#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> data
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-28 15:33
@Desc   ：
=================================================='''
import re
import requests
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()
header = {
    'User-Agent': ua.random,
    # 'Cookie': 'tradeLdc=NJYH; tradeMA=71; _snma=1%7C162493069073585067%7C1624930690735%7C1624930693438%7C1624930694928%7C4%7C1; _snvd=1624930681478I7bAo/zqrT5; _snmc=1; _snsr=localhost%3A63342%7Creferral%7C%7C%7C; _snzwt=THtBDo17a556aa84bk9fj2c84; _df_ud=70b3a7c1-9584-400d-acac-25bfd3bb2f3d; _device_session_id=p_68361e6a-2555-4d07-a044-d23d3a569a75; hm_guid=b306566f-4a03-4bcb-8a03-cb3877281922',
    # 'Referer': 'http://localhost:63342/',
}
proxiesNone = {
    "http": None,
    "https": None
}

KW = "/keyword/getKeyword.html?callback=getKeyword"

"""
"supplierCode1":"70080826",     #商品唯一ID  
"supplierCode2":"70080826",     #商品唯一ID  
"logoUrlBig":"//image.suning.cn/uimg/cshop/logo/000000000070080826.jpg_300w_300h?1533002535839", #商标
"companyName":"太阳雨节能电器有限公司",    #公司名字
"Qstar":"9.68",
"shopName":"太阳雨官方旗舰店",      #品牌名字
"indexUrl":"//shop.suning.com/70080826/index.html", #该公司的主页URL
"supplierCode":"70080826",      #商品唯一ID  
"logoUrl_60":"//image.suning.cn/uimg/cshop/logo/000000000070080826.jpg_60w_60h?1533002535839",
"Apercent":"31.15%",
"shopStatus":"0",
"telPhone":"0518-80626835",     #电话号
"assImg":"//res.suning.cn/images/ShoppingArea/V9/online.gif",
"equityFlag":"Y",
"Qcompare":1,
"pageType":"shopinfo",
"Qpercent":"24.33%",
"qrCode":"//code.suning.cn/pc/build.do?longUrl=68747470733a2f2f73686f702e6d2e73756e696e672e636f6d2f37303038303832362e68746d6c3f616454797065436f64653d3131313526616449643d3030373030383038323626736f7572636546726f6d3d73686f702d7172636f6465&bizCode=i9kfFe&logo=http://image.suning.cn/uimg/cshop/logo/000000000070080826.jpg_60w_60h?1533002535839",
"Dcompare":-1,
"Acompare":1,
"Dpercent":"4.12%",
"shopDomain":"//shop.suning.com/70080826/index.html",
"Astar":"9.47",
"shopId":"70080826",
"companyProvince":"江苏",     #公司  省
"companyCity":"连云港市",       #公司 城市
"Dstar":"9.30",
"imStatus":"0",
"star":"1",
"licencePageUrl":"//shop.suning.com/70080826/showLicence.html",
"realLogoUrl":"http://image.suning.cn/uimg/cshop/logo/000000000070080826.jpg?1533002535839",
"pageId":"shopinfo",
"logoUrl":"//image.suning.cn/uimg/cshop/logo/000000000070080826.jpg_60w_60h?1533002535839",
"companyAddress":"江苏连云港市瀛洲南路199号",  #公司  地址
"shopDstatus":0,
"shopType":"0",
"countryName":"中国"  国家名字


/jsonp/71411410/shopinfo/shopinfo.html?callback=shopinfo
url = "http://list.suning.com/0-251027-0.html"


71411410
70725278
70080826
70069021
"""


# 直接遍历 整个 苏宁的 所有的
# spcode : "70179588",
# supplierCode1:"70179588",
# shopId : "70179588",
# 根据返回的 jsonp  判断是不是有这家商店    获取 companyAddress:地址  indexUrl:主页URL   companyName:公司名字  shopName:网上商铺名字


def getKW(url):
    jsonp = getdata(url=url)
    print(jsonp.status_code)
    if jsonp.status_code != 403:
        text =jsonp.text
        print(text)
        parse_data_dice = eval(parse_jsonp(text))
        print(parse_data_dice)
        zy = ""
        for key, value in parse_data_dice.items():
            print(key, "  :   ", value)
            for v in value:
                zy += v+","
        return zy


def parse_jsonp(jsonp_str):
    try:
        gro1 = re.search('^[^(]*?\((.*)\)[^)]*$', jsonp_str).group(1)
        print(gro1)
        return gro1
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


def get_dict(url):
    jsonp = getdata(url=url).text
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
            # print(indexUrl)

            url_zy_hotWord = "{}/jsonp/{}/keyword/getKeyword.html?callback=getKeyword".format(indexUrl, supplierCode)
            # print(url_zy_hotWord)
            zy = getKW(url_zy_hotWord)

        print("<<<<<<<<<<<<<<<<"*8)
        print("zy   ", zy)
        print(" indexUrl        " + indexUrl)
        print("companyName+shopName         " + companyName + shopName)
        print("telPhone         " + telPhone)
        print(" companyAddress        " + companyAddress)
        print(">>>>>>>>>>>>>>>>>"*8)

    else:
        print("空的啊  宝贝  啊哈哈哈哈!")
        # if key == "":
        #     print(key, '   :    ', value)


if __name__ == '__main__':
    """
    
        71300377
        71411410
        70725278
        70080826
        70069021
        70067092
        70207291
        
        
        同步的搞定了   但是同步的太慢了  有太多的页码页面 都是空的
        明天修改为  异步请求  httpx  来一波
        
    """

    """
    #  商铺信息接口
    http://shop.suning.com/jsonp/70080826/shopinfo/shopinfo.html?callback=shopinfo
    
    #商铺 的搜索词 的接口
      https://3songshu.suning.com/jsonp/70069021/keyword/getKeyword.html?callback=getKeyword
    """
    url_T = "http://shop.suning.com/jsonp/{}/shopinfo/shopinfo.html?callback=shopinfo"
    url = "http://shop.suning.com/jsonp/{}/shopinfo/shopinfo.html?callback=shopinfo".format("70067092")
    url_sc = "http://3songshu.suning.com/jsonp/70067092/keyword/getKeyword.html?callback=getKeyword"
    print(url)
    get_dict(url)
    exit()

    """
    https://ds.suning.com/ds/personalizedWord/-20089--162485869787940429-371-showHotkeywords.xjsonp?callback=showHotkeywords&_=1624946222129
    """
    id = 70000000          #0000000
    for wy_id in range(1000,9999999):
        id_a = id+wy_id
        url_Z = url_T.format(id_a)
        get_dict(url_Z)
        print(id_a)
        print(url_Z)
        print("----------------"*12)
        # if wy_id>11050:
        #     exit()

    # exit()
    # get_dict(url)
    # getKW(url_sc)

# selector = etree.HTML(req.text)
# js_list = selector.xpath("//script/text()")
# print(len(js_list))
# for js in js_list:
#     print(js)
#     print("----------------------------------------------------------------------------------------------------------")
