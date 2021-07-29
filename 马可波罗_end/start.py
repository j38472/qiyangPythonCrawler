#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-02 16:30
@Desc   ：OCR
=================================================='''
import os
import re
import time
from PIL import Image
import pytesseract
import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc

jdbc = mySqlJdbc()
ua = UserAgent()
proxiesNone = {
    "http": None,
    "https": None
}

def getHtml(url,header):
    # time.sleep(0.5)
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=6,verify=False)
        reqHtml = req.text
        # print(reqHtml)
        # exit()
        return reqHtml
    except Exception:
        print("cccc")

def dow_img(url,header,name):
    # print(url)
    # time.sleep(1.5)
    try:
        req = requests.get(url=url, headers=header, proxies=proxiesNone, timeout=6,verify=False)
        # 拼接图片名
        file_name = "image/" + name + ".jpg"
        # print(file_name)
        # 将图片存入本地
        fp = open(file_name, 'wb')
        # 写入图片
        fp.write(req.content)
        fp.close()
    except Exception:
        print("cccc")


def getXQ(url):
    print(url)
    t = int(time.time())
    # print(url)
    host_xq = re.search(r"//([a-zA-Z]*[0-9]*[a-zA-Z]*[0-9]*[a-zA-Z]*[0-9]*[a-zA-Z]*[0-9]*.cn.makepolo.com)", url, flags=re.S)
    if host_xq:
        host_xq = host_xq.group(1)
        # print("host_xq  ",host_xq)
        # exit()
        header_xq = {
            'User-Agent': ua.random,
            # 'path': pathurl,
            'cookie': 'Hm_lpvt_7e7577ecbf4c96abade7fbcaa1d3b519={}'.format(str(t)),
            'Host': host_xq,
            'Referer': 'http://china.makepolo.com/'
        }
        xq_html = getHtml(url,header_xq)
        if xq_html:
            # 只取一个手机号  手机号可能会取不到  有些公司的 联系方式暂未开放
            sj_xpath = "//div[@class='phone_mask_list']/img/@src"
            # 电话号
            dh_xpath = "//ul/li[3]/span/img/@src"
            # 联系人
            lxr_xpath = "//div[1]/ul/li[1]/span/text()"
            # 名字
            name_xpath = "//h1/text()"
            # 地址
            dz_xpath ="//ul/li[7]/span/text()"
            # 主营
            zy_xpath = "//div[@class='company_hd f_l']/p/text()"

            selector_xq = etree.HTML(xq_html)
            sj_url = selector_xq.xpath(sj_xpath)
            dh_url = selector_xq.xpath(dh_xpath)
            lxr = selector_xq.xpath(lxr_xpath)
            name = selector_xq.xpath(name_xpath)
            zy = selector_xq.xpath(zy_xpath)
            dz = selector_xq.xpath(dz_xpath)

            if lxr:
                lxr= lxr[0]
                lxr = lxr.replace("&nbsp", "")
            else:
                lxr = ""

            if name:
                name= name[0]
            else:
                name = ""

            if zy:
                zy= zy[0]
            else:
                zy = ""

            if dz:
                dz = dz[0]
            else:
                dz = ""
            # 第二种页面格式
            sj_xpath_two = "//div[@class='y_contact_list']/ul/li[3]/img[1]/@src"

            header_phone = {
                'User-Agent': ua.random,
                # 'path': pathurl,
                # 'cookie': 'Hm_lpvt_7e7577ecbf4c96abade7fbcaa1d3b519={}'.format(str(t)),
                'Referer': url,
                'Host': host_xq,
            }
            sj = ""
            dh = ""
            # OCR
            try:
                if sj_url :
                    # print("sj         http://"+host_xq+sj_url[0])
                    dow_img("http://"+host_xq+sj_url[0],header_phone,"sj")
                    img = Image.open("image\sj.jpg")
                    sj = pytesseract.image_to_string(img)
                    os.remove("image\sj.jpg")
                    sj = qx_sj(sj)

                if dh_url:
                    # print("dh         http://"+host_xq+dh_url[0])
                    img_url = "http://"+host_xq+dh_url[0]
                    dow_img(img_url,header_phone,"dh")
                    img = Image.open("image\dh.jpg")
                    dh = pytesseract.image_to_string(img)
                    os.remove("image\dh.jpg")
                    dh = qx_dh(dh)
            except Exception:
                print("CCCCCCCC")
            zy = qx_mh(zy)
            name = qx_mh(name)
            lxr = qx_mh(lxr)
            dz = qx_mh(dz)
            # print(name)
            # print(url)
            # print(zy)
            # print(lxr)
            # print(dh)
            # print(sj)
            # print(dz)
            # print(dh)
            # print(sj)
            if len(zy)>300:
                zy = zy[0:300]
            jdbc.inXqDate(name,url,zy,lxr,dh,sj,dz,"mkbl_data")
            print("---------------------------------------------------------")
            # exit()

def qx_sj(strSj):
    strSj = strSj.replace("", "")
    strSj = strSj.replace("'", "")
    strSj = strSj.replace("\n", "")
    strSj = strSj.replace("\r", "")
    strSj = strSj.replace("\r\n", "")
    strSj = strSj.replace("\'", "")
    strSj = strSj.replace("\"", "")
    return strSj

def qx_dh(strDh):
    strDh = strDh.replace("", "")
    strDh = strDh.replace("'", "")
    strDh = strDh.replace("\r\n", "")
    strDh = strDh.replace("\n", "")
    strDh = strDh.replace("\r", "")
    strDh = strDh.replace(" ", "-")
    return strDh

def qx_mh(s):
    s =  s.replace("'", "")
    s =  s.replace("\\", "")
    return s


def getLB(url):
    header_UA = {
        'User-Agent': ua.random,
    }
    html = getHtml(url, header_UA)
    if html:
        selector_lb = etree.HTML(html)
        xq_url_list = set(selector_lb.xpath("//a[@class='check_phone']/@href"))
        # print(len(xq_url_list))
        # print(xq_url_list)
        for xq_url in xq_url_list:
            xq_url = "http:" + xq_url
            # print(xq_url)
            isOrNo = jdbc.getUrlGs(xq_url, "mkbl_data")
            if isOrNo <1:
                getXQ(xq_url)
            else:
                print("已经有这条数据了    ",xq_url)
        xyy_url = selector_lb.xpath("//div[@class='s_l']/div[@class='nextpage']/a/@href")
        xyy_url_name = selector_lb.xpath("//div[@class='s_l']/div[@class='nextpage']/a/text()")
        if xyy_url_name:
            if xyy_url_name[len(xyy_url_name)-1].find('下一页') > -1:
                xyy_ = xyy_url[len(xyy_url)-1]
                print("存在下一页",xyy_)
                getLB(xyy_)
            else:
                print("不存在下一页")


if __name__ == '__main__':
    # getXQ("http://jorsune.cn.makepolo.com/contact_us.html")
    # url = "http://china.makepolo.com/list/spc1276/"
    # k = re.search(r"spc([0-9]*)/", url, flags=re.S).group(1)
    # url = "http://caigou.makepolo.com/scw.php?newcid=" + k + "&search_flag=q1"
    # getLB(url)
    # exit()

    getLB("http://caigou.makepolo.com/scw.php?pg=21&newcid=1201&search_flag=q1")
    jdbc.setSearch(168, "mkbl_search")

    # getXQ("http://wfaolongfood.cn.makepolo.com/contact_us.html")
    # exit()
    id_url_list = jdbc.getLbUrl("mkbl_search")
    for idAndUrl in id_url_list:
        id = idAndUrl[0]
        url = idAndUrl[1]
        k = re.search(r"spc([0-9]*)/", url, flags=re.S).group(1)
        url = "http://caigou.makepolo.com/scw.php?newcid="+k+"&search_flag=q1"
        # print(url)
        getLB(url)
        jdbc.setSearch(id,"mkbl_search")
        # exit()