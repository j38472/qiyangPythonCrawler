#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-08 13:59
@Desc   ：http://www.chinafoods.com.cn/UserCenter/Index.aspx?uid=103244
=================================================='''
import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil

ua = UserAgent()
header = {
    'User-Agent': ua.random,
}
proxiesNone = {
    "http": None,
    "https": None
}
jdbc = mySqlJdbc()
tool = MyToolUtil()

def get_data(url):
    print(url)
    requ = requests.get(url, headers=header, proxies=proxiesNone, timeout=7,allow_redirects=False)
    print(requ.status_code)

    if requ.status_code == 200:
        text = requ.text
        selector = etree.HTML(text)

        name_list = selector.xpath("//*[@id=\"all\"]/div[6]/div[1]/div[1]/div[2]/div[1]/text()")
        dh_list = selector.xpath("//*[@id=\"all\"]/div[6]/div[1]/div[2]/div[2]/div[1]/text()[3]")
        sj_list = selector.xpath("//*[@id=\"all\"]/div[6]/div[1]/div[2]/div[2]/div[1]/text()[2]")
        zy_list = selector.xpath("//*[@id=\"all\"]/div[6]/div[2]/div[1]/div[2]/div/div[2]/text()")
        dz_list = selector.xpath("//*[@id=\"all\"]/div[6]/div[1]/div[2]/div[2]/div[1]/text()[6]")
        lxr_list = selector.xpath("//*[@id=\"all\"]/div[6]/div[1]/div[1]/div[2]/div[2]/text()[1]")
        name = tool.set_Qx_Data(name_list[0])
        dh = tool.set_Qx_Data(dh_list[0])
        sj = tool.set_Qx_Data(sj_list[0])
        zy = tool.set_Qx_Data(zy_list[0])
        dz = tool.set_Qx_Data(dz_list[0])
        lxr = tool.set_Qx_Data(lxr_list[0])
        jdbc.inXqDate(name=name,dh=dh,sj=sj,zy=zy,dz=dz,lxr=lxr)

if __name__ == '__main__':
    url = "http://www.chinafoods.com.cn/UserCenter/Index.aspx?uid={}"
    for i in range(0,103244):
        url_yes = url.format(i)
        get_data(url_yes)
        if i >5:
            exit()
