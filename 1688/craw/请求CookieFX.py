#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> 请求CookieFX
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-10-21 15:21
@Desc   ：
=================================================='''
import requests

# url = "https://sale.1688.com/sale/zgc/scene/4pwgqz2y.html?spm=a260k.22464671.home2019category.22.63f267f1qYClDw&cateId=65"
url = "https://sale.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?jsv=2.4.11&appKey=12574478&t=1634882974274&sign=064d1ce9acb7ce21effb185da15f187c&api=mtop.taobao.widgetService.getJsonComponent&v=1.0&type=jsonp&isSec=0&timeout=20000&dataType=jsonp&callback=mtopjsonp5&data=%7B%22cid%22%3A%22FactoryRankServiceWidget%3AFactoryRankServiceWidget%22%2C%22methodName%22%3A%22execute%22%2C%22params%22%3A%22%7B%5C%22extParam%5C%22%3A%5C%22%7B%5C%5C%5C%22methodName%5C%5C%5C%22%3A%5C%5C%5C%22readRelatedRankEntries%5C%5C%5C%22%2C%5C%5C%5C%22cateId%5C%5C%5C%22%3A%5C%5C%5C%22%5C%5C%5C%22%2C%5C%5C%5C%22size%5C%5C%5C%22%3A15%7D%5C%22%7D%22%7D"

req = requests.get(url=url)
print(req)
print(req.text)
print(req.content)
print(req.cookies)
