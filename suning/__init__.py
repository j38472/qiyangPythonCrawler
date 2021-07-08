#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-28 14:17
@Desc   ：
=================================================='''

import requests
from fake_useragent import UserAgent

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}

'''

        paging  当前页的  刷新页数  应该是一个页码  有三个 
        keyword 搜索字段  
        
        
    https://list.suning.com/emall/searchV1Product.do?ci=500363&pg=03&yjhx=0&cp=0&il=0&st=0&iy=-1&hf=solr_55468_attrId:%E9%A9%B4%E8%82%89%252F%E9%A9%AC%E8%82%89&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&paging=1&sub=1&spf=_&jzq=124
    https://list.suning.com/emall/searchV1Product.do?ci=500363&pg=03&yjhx=0&cp=0&il=0&st=0&iy=-1&hf=solr_55468_attrId:%E9%A9%B4%E8%82%89%252F%E9%A9%AC%E8%82%89&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&paging=1&sub=1&spf=_&jzq=124
    https://list.suning.com/emall/searchV1Product.do?ci=500363&pg=03&yjhx=0&cp=0&il=0&st=0&iy=-1&hf=solr_55468_attrId:%E9%A9%B4%E8%82%89%252F%E9%A9%AC%E8%82%89&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&paging=3&sub=1&spf=_&jzq=124
            -------------------------------
    https://search.suning.com/emall/searchV1Product.do?keyword=%E7%83%9F%E6%9C%BA%E7%81%B6%E5%85%B7&ci=0&pg=01&yjhx=&cp=1&il=0&st=0&iy=0&adNumber=0&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&sub=1&jzq=18523
    https://search.suning.com/emall/searchV1Product.do?keyword=%E7%83%9F%E6%9C%BA%E7%81%B6%E5%85%B7&ci=0&pg=01&yjhx=&cp=1&il=0&st=0&iy=0&adNumber=0&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&paging=1&sub=1&jzq=18527
    https://search.suning.com/emall/searchV1Product.do?keyword=%E7%83%9F%E6%9C%BA%E7%81%B6%E5%85%B7&ci=0&pg=01&yjhx=&cp=1&il=0&st=0&iy=0&adNumber=0&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&paging=2&sub=1&jzq=18527
    https://search.suning.com/emall/searchV1Product.do?keyword=%E7%83%9F%E6%9C%BA%E7%81%B6%E5%85%B7&ci=0&pg=01&yjhx=&cp=1&il=0&st=0&iy=0&adNumber=0&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=371&paging=3&sub=1&jzq=18527
'''
url = "https://list.suning.com/0-500363-0-2-0-0-0___0_0-0-0-0-0-616359.html#search-path"

req = requests.get(url=url, headers=header, proxies=proxiesNone)
print(req.text)

