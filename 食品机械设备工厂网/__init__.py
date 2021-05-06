#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/30 14:54
@Desc   ： .... https://www.wzcn.cn/company/spjgjx.html
                详情页的手机号和电话号  是用  <li>电话：<em onclick="showAlert('MTU2NjI3MjU5NTk=');">1566****959点击查看</em></li>
                showAlert 中的字符串   进行base64解密就是 对应的手机号和电话号

                处理列表页的时候  不能从下一页的标签中获取下一页的链接
                获取共多少条 和多少页
                以此来递归自身的详情页方法

                本网站数据量有点少  预计不到一万条
=================================================='''
import requests

if __name__ == '__main__':
    proxies = {"http": None, "https": None}
    url = "https://www.wzcn.cn/company/spjgjx.html"
    htmlpage = requests.get(url=url,proxies=proxies).text
    print(htmlpage)
