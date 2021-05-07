#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> test
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/26 10:08
@Desc   ：
=================================================='''
from time import sleep
import time
import requests

import hashlib
import base64

from 中国供应商.run.myJDBC import updateIsOrNo

"""""

(this['$store']['state']['url']['index']
/api/movie
58f7e546190d6a8c7a60aeddcf8729c7
"MDg1OGZmYTI3MjFiZTliM2M1MWViYWQ3MDlkMTljYWQ5ZmM3MzljNywxNjE5NzQ1MjQz"


https://spa6.scrape.center/api/movie/?limit=10&offset=0&token=OGI1NzEyNTdiMDNjNzhhMzc2ZDE1ZDVjY2M3ZGNhMjYxNjJhM2YwNywxNjE5NzQ5NzA4
https://spa6.scrape.center/api/movie/?limit=10&offset=10&token=NWVlNDAxYWJlODA2MGExYWUxZWE3ZjY2Y2Y5MmNmMjA4YmM3YjRiYywxNjE5NzQ5NzM2
"""

def getToken():
    t = int(time.time())
    t = str(t)
    # print(t)
    # print(type(t))
    res = "/api/movie," + t
    print(res)
    sh1 = hashlib.sha1(res.encode('utf-8'))
    en = sh1.hexdigest()
    print(en)
    ba = en + "," + t
    # print(type(ba))
    data_bytes = ba.encode("utf-8")
    bs64 = base64.b64encode(data_bytes)
    bs64 = str(bs64)
    bs64 = bs64[2:-1]
    print(bs64)
    return bs64

def cs(i):
    if i == 1:
        i+=1
        print(i)

        cs(i)

    else:
        return i
def recursion(n):
    v = n//2 # 地板除，保留整数
    # print(v) # 每次求商，输出商的值
    if v>2:
        ''' 当商为0时，停止，返回Done'''
        recursion(v)
    else:
        return v
    v = recursion(v)

def sum_recu(n):
    cent = 0
    if n==520:
        n=50
        sum_recu(n)
    return n
if __name__ == '__main__':
    updateIsOrNo("search",1)
    # print("main",sum_recu(520))

    # requests.get(url="https://proxy.qg.net/replace?Key=F58B5B03A518E080")
    # dz = "' '山东 潍坊 诸城市 密州街道普乐工业园''"
    # dz = dz.replace("'","")
    # print(dz)


    # url = "https://spa10.scrape.center/"
    # page = requests.get(url=url)
    # page.encoding = "utf-8"
    # html = page.text
    # print(html)



    # url = """https://spa6.scrape.center/api/movie/?limit=10&offset=0&token=%s"""%(getToken())
    # print(url)
    # html = requests.get(url=url).text
    # print(html)
    # for i in range(1,9):
    #     token = getToken()
    #     url = """https://spa6.scrape.center/api/movie/?limit=10&offset=%s&token=%s"""%(i*10,token)
    #     print(url)
    #     sleep(1)
    #     html =  requests.get(url=url).text
    #     print(html)
    #     print("-"*90)