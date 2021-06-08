#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-07 9:41
@Desc   ：
=================================================='''
from fake_useragent import UserAgent

"""
陈东风
13681247125
13681247125
378492571

"""
ua = UserAgent()
header = {
    'User-Agent': ua.random,
    # 'Cookie': 'UM_distinctid=178e8b45023384-0c653d29ec84b5-d7e1938-125f51-178e8b45024845; safedog-flow-item=F0B06A15A0414431C327A36A76D67417; ASP.NET_SessionId=pnd4kr45hhns2k45ddbyof45; Hm_lvt_e2689ecbba89d681b31e360cb5d08d80=1622688527,1623029717; Hm_lpvt_e2689ecbba89d681b31e360cb5d08d80=1623030910; CNZZDATA1973171=cnzz_eid%3D515471263-1618809838-%26ntime%3D1623026108'
}
proxiesNone = {
    "http": None,
    "https": None
}
import requests

reqTest = requests.get(url="http://wangshouyi.1588.tv/", headers=header,proxies = proxiesNone).text
print(reqTest)