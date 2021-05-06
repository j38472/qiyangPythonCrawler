#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> IP
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/27 9:24
@Desc   ：封我IP  解决一哈
=================================================='''
import requests
import json

# 资源申请
from 中国供应商.run import myJDBC

get_IP = "http://proxy.qg.net/allocate?Key=F58B5B03A518E080"
# 资源释放
rel_IP = "http://proxy.qg.net/release?Key=F58B5B03A518E080"
# 资源更换
rep_IP = "http://proxy.qg.net/replace?Key=F58B5B03A518E080"
# 资源查询
que_IP = "http://proxy.qg.net/query?Key=F58B5B03A518E080"


# 资源申请
def get_Ip():
    req = requests.get(url=get_IP)
    print(req)


# 资源释放
def rel_Ip():
    req = requests.get(url=rel_IP)
    print(req)


# 资源更换
def rep_Ip():
    print("更换代理IP了!!!!!!")
    re = requests.get(url=rep_IP).text


# 资源查询
def que_Ip():
    re = requests.get(url=que_IP).text
    print("资源查询 ",re)
    reJson = json.loads(re)
    if reJson["TaskList"]:
        tasklist = reJson["TaskList"]
        for dc in tasklist:
            DataList=dc["Data"]
        for data in DataList:
            print(data["IP"])
            print(data["port"])
    else:
        get_Ip()
    return data

def get_proxies():
    # 查询资源
    data = que_Ip()
    # 代理服务器
    proxyHost = data["IP"]  # ip地址
    proxyPort = data["port"]  # 端口号
    proxyMeta = "http://%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }
    proxies = {
        "http": proxyMeta,
    }
    print("当前proxies为: ",proxies)

    myJDBC.inProxyMeta(proxyMeta)
    return proxies


if __name__ == '__main__':
    # rel_Ip()
    # get_Ip()
    get_proxies()
    #
    # pmeta = myJDBC.getSqlProxyMeta()
    # pmeta[0][0]


    # re = requests.get(url="http://proxy.qg.net/query?Key=F58B5B03A518E080").text
    # print(re)
    # reJson = json.loads(re)
    # print(type(reJson))


    # que_Ip()
