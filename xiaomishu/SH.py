#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> SH
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-08-24 10:48
@Desc   ： 本程序为上海地区的专属爬虫
=================================================='''
import re
from time import sleep

import requests
from fake_useragent import UserAgent
from lxml import etree

from myJDBC.jdbc import mySqlJdbc
from util.TOOL import MyToolUtil

ua = UserAgent()
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
}

proxiesNone = {
    "http": None,
    "https": None,
}


def getHtmlSel(url):
    sleep(1.24)
    req_text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    # print(req_text)
    selector = etree.HTML(req_text)
    return selector


def getHtmlText(url):
    sleep(1.24)
    req_text = requests.get(url=url, headers=header, proxies=proxiesNone).text
    return req_text


# mdAll = ['', '-sp2', '-sp4', '-sp16', '-sp2048', '-sp1', '-sp8']
sAll = ['', '-s263', '-s267', '-s255', '-s255_5153', '-s255_5202', '-s255_5198', '-s255_5232', '-s255_5314',
        '-s255_5154',
        '-s255_5161', '-s255_5206', '-s255_5207', '-s255_5209', '-s255_5233', '-s255_5257', '-s255_5262', '-s255_5268',
        '-s255_5269', '-s255_5277', '-s255_5278', '-s255_5291', '-s255_5293', '-s273', '-s273_5308', '-s273_5158',
        '-s273_5164',
        '-s273_5299', '-s273_5168', '-s273_5175', '-s273_5181', '-s273_5185', '-s273_5190', '-s273_5258', '-s273_5263',
        '-s275_5191', '-s275_5195', '-s275_5151', '-s275_5313', '-s275_5147', '-s275_5204', '-s275_5248', '-s275',
        '-s275_5254',
        '-s275_5261', '-s275_5285', '-s257_5165', '-s257_5290', '-s257_5267', '-s261_5300', '-s261_5267', '-s261',
        '-s261_5219',
        '-s261_5176', '-s261_5204', '-s261_5168', '-s261_5183', '-s261_5190', '-s261_5205', '-s261_5249', '-s261_5263',
        '-s261_5271', '-s261_5288', '-s261_5301', '-s261_5306', '-s261_5315', '-s261_10866', '-s265_5247', '-s265',
        '-s265_5253',
        '-s265_5213', '-s265_5252', '-s265_5249', '-s265_5248', '-s265_5251', '-s265_5254', '-s265_5265', '-s265_6344',
        '-s265_6345', '-s266_5150', '-s266_5151', '-s266_5172', '-s266_5178', '-s266_5194', '-s266_5195', '-s266',
        '-s266_5224',
        '-s266_5253', '-s266_5254', '-s266_5261', '-s266_5282', '-s266_6344', '-s266_6345', '-s260_5191', '-s260',
        '-s260_5185',
        '-s260_5161', '-s260_5314', '-s260_5210', '-s260_5173', '-s260_5199', '-s260_5233', '-s260_5278', '-s260_5287',
        '-s260_5291', '-s256_5162', '-s256_5163', '-s256_5192', '-s256_5193', '-s256_5194', '-s256_5195', '-s256',
        '-s256_5196',
        '-s259_5167', '-s259_5189', '-s259_5256', '-s259_5266', '-s262_5182', '-s262_5184', '-s262_5215', '-s262',
        '-s262_5219',
        '-s262_5301', '-s258_5272', '-s258_5311', '-s258_5304', '-s258_5309', '-s258_5223', '-s258_5294', '-s259',
        '-s258', '-s258_5275',
        '-s274_5196', '-s274_5197', '-s274_5250', '-s274_5252', '-s274_5255', '-s274_5265', '-s274_5284', '-s274',
        '-s274_5312',
        '-s271_5245', '-s271_5295', '-s269_5179', '-s269_5280', '-s269_5170', '-s269_5234', '-s269_5155', '-s271',
        '-s269', '-s269_5157',
        '-s269_5169', '-s269_5197', '-s269_5225', '-s269_5228', '-s269_5284', '-s269_5286', '-s268_5152', '-s268',
        '-s268_5216',
        '-s268_5220', '-s268_5222', '-s268_5226', '-s268_5227', '-s268_5274', '-s268_5289', '-s268_5292', '-s272_5148',
        '-s272',
        '-s272_5159', '-s272_5160', '-s272_5212', '-s272_5214', '-s272_6349', '-s264_5171', '-s264_5180', '-s264_5186',
        '-s264',
        '-s264_5187', '-s264_5200', '-s264_5201', '-s264_5203', '-s264_5208', '-s264_5221', '-s264_5229', '-s264_5259',
        '-s264_5260', '-s264_5270', '-s264_5276', '-s264_5281', '-s264_5310']
xadqAll = ['', '-rSH_PD', '-rSH_PD_01', '-rSH_PD_13', '-rSH_PD_12', '-rSH_PD_08', '-rSH_PD_06', '-rSH_PD_04',
           '-rSH_PD_09',
           '-rSH_PD_14', '-rSH_PD_22', '-rSH_PD_10', '-rSH_PD_07', '-rSH_PD_11', '-rSH_PD_26', '-rSH_PD_28',
           '-rSH_PD_27', '-rSH_PD_15', '-rSH_PD_25', '-rSH_PD_24', '-rSH_PD_29', '-rSH_PD_64', '-rSH_PD_30',
           '-rSH_PD_50', '-rSH_PD_52', '-rSH_PD_54', '-rSH_PD_55', '-rSH_PD_56', '-rSH_PD_58', '-rSH_PD_59',
           '-rSH_PD_60', '-rSH_PD_61', '-rSH_PD_62', '-rSH_PD_63', '-rSH_PD_250', '-rSH_XH', '-rSH_XH_01',
           '-rSH_XH_02', '-rSH_XH_17', '-rSH_XH_18', '-rSH_XH_19', '-rSH_XH_04', '-rSH_XH_21', '-rSH_XH_06',
           '-rSH_XH_07', '-rSH_XH_05', '-rSH_XH_16', '-rSH_XH_08', '-rSH_XH_20', '-rSH_CN', '-rSH_CN_01', '-rSH_CN_02',
           '-rSH_CN_07', '-rSH_CN_03', '-rSH_CN_05', '-rSH_CN_10', '-rSH_CN_04', '-rSH_CN_08', '-rSH_JA', '-rSH_JA_02',
           '-rSH_JA_05', '-rSH_JA_04', '-rSH_JA_07', '-rSH_JA_08', '-rSH_JA_06', '-rSH_JA_01', '-rSH_JA_03',
           '-rSH_JA_50', '-rSH_JA_BQ', '-rSH_JA_DN', '-rSH_JA_DN00', '-rSH_JA_DY', '-rSH_JA_HC', '-rSH_JA_PP',
           '-rSH_JA_PP00', '-rSH_JA_SB', '-rSH_JA_SH', '-rSH_JA_XC', '-rSH_JA_ZB', '-rSH_HP', '-rSH_HP_02',
           '-rSH_HP_03', '-rSH_HP_01', '-rSH_HP_07', '-rSH_HP_08', '-rSH_HP_10', '-rSH_HP_05', '-rSH_HP_04',
           '-rSH_HP_09', '-rSH_HP_06', '-rSH_HP_XT', '-rSH_HP_DP', '-rSH_HP_JJ', '-rSH_HP_HH', '-rSH_HP_RJ',
           '-rSH_HP_LB', '-rSH_HP_SB', '-rSH_HP_RJ00', '-rSH_MH', '-rSH_MH_05', '-rSH_MH_06', '-rSH_MH_12',
           '-rSH_MH_23', '-rSH_MH_10', '-rSH_MH_08', '-rSH_MH_21', '-rSH_MH_22', '-rSH_MH_16', '-rSH_MH_02',
           '-rSH_MH_13', '-rSH_MH_01', '-rSH_MH_24', '-rSH_MH_52', '-rSH_MH_53', '-rSH_MH_54', '-rSH_MH_55',
           '-rSH_MH_56', '-rSH_MH_57', '-rSH_MH_59', '-rSH_MH_60', '-rSH_MH_61', '-rSH_YP', '-rSH_YP_02', '-rSH_YP_03',
           '-rSH_YP_05', '-rSH_YP_01', '-rSH_YP_07', '-rSH_YP_04', '-rSH_YP_06', '-rSH_YP_08', '-rSH_YP_53',
           '-rSH_YP_54', '-rSH_HK', '-rSH_HK_02', '-rSH_HK_04', '-rSH_HK_03', '-rSH_HK_08', '-rSH_HK_01', '-rSH_HK_13',
           '-rSH_HK_12', '-rSH_HK_14', '-rSH_HK_15', '-rSH_HK_54', '-rSH_PT', '-rSH_PT_10', '-rSH_PT_20', '-rSH_PT_03',
           '-rSH_PT_01', '-rSH_PT_19', '-rSH_PT_02', '-rSH_PT_04', '-rSH_PT_21', '-rSH_PT_50', '-rSH_PT_55',
           '-rSH_PT_56', '-rSH_BS', '-rSH_BS_03', '-rSH_BS_01', '-rSH_BS_06', '-rSH_BS_02', '-rSH_BS_04', '-rSH_BS_05',
           '-rSH_BS_07', '-rSH_BS_51', '-rSH_BS_52', '-rSH_BS_53', '-rSH_BS_55', '-rSH_BS_56', '-rSH_BS_57',
           '-rSH_BS_58', '-rSH_BS_59', '-rSH_BS_60', '-rSH_QP', '-rSH_QP_01', '-rSH_QP_02', '-rSH_QP_50', '-rSH_QP_51',
           '-rSH_QP_52', '-rSH_QP_53', '-rSH_QP_54', '-rSH_SJ', '-rSH_SJ_0', '-rSH_SJ_1', '-rSH_SJ_2', '-rSH_SJ_3',
           '-rSH_SJ_50', '-rSH_SJ_51', '-rSH_SJ_52', '-rSH_SJ_53', '-rSH_SJ_54', '-rSH_SJ_55', '-rSH_SJ_56',
           '-rSH_SJ_57', '-rSH_SJ_58', '-rSH_SJ_59', '-rSH_SJ_60', '-rSH_SJ_61', '-rSH_CM', '-rSH_CM_50', '-rSH_CM_51',
           '-rSH_CM_52', '-rSH_CM_53', '-rSH_CM_54', '-rSH_CM_55', '-rSH_FX', '-rSH_FX_50', '-rSH_FX_51', '-rSH_FX_52',
           '-rSH_FX_53', '-rSH_FX_54', '-rSH_FX_55', '-rSH_FX_56', '-rSH_FX_57', '-rSH_FX_58', '-rSH_FX_59', '-rSH_JD',
           '-rSH_JD_0', '-rSH_JD_1', '-rSH_JD_2', '-rSH_JD_3', '-rSH_JD_50', '-rSH_JD_51', '-rSH_JD_52', '-rSH_JD_53',
           '-rSH_JD_54', '-rSH_JD_55', '-rSH_JD_56', '-rSH_JJ', '-rSH_JJ_0', '-rSH_JJ_1', '-rSH_JJ_2', '-rSH_JS',
           '-rSH_JS_50', '-rSH_JS_51', '-rSH_JS_52', '-rSH_JS_53', '-rSH_JS_54', '-rSH_JS_55', '-rSH_JS_56',
           '-rSH_JS_57', '-rSH_JS_58', '-rSH_JS_59', '-rSH_JS_60']

if __name__ == '__main__':



    exit()

    """
        http://www.xiaomishu.com/shop/search-sp1-rSH_CN-s273_5308/
    """
    url = "http://www.xiaomishu.com/shop/search"
    cont = 0
    # for sp in mdAll:
    for s in sAll:
        for rSH in xadqAll:
            url_ = url  + rSH + s
            print(url_)
            if cont >100:
                break
            cont += 1
            pass
    print(cont)
    exit()



    asd = "http://www.xiaomishu.com/shop/search"
    allccc = []
    for c in xadqAll:
        # sel = getHtmlSel(url=asd + c)
        # listccc = sel.xpath("//div[@class='s-district-sub nc-items nc-sub nc-more clearfix']/a/@href")
        # print(listccc)
        # allccc += listccc

        try:
            reStr = re.search("(-rSH_[A-Z]{2}(/|_[0-9A-Za-z]*))", c).group(1)
            print(reStr)
            allccc.append(reStr)
        except Exception as e:
            print("          ", e)
    print(allccc)
    exit()

    """
    url 列表请求URL  分析
    http://www.xiaomishu.com/shop/search-sp1-rSH_CN-s273_5308/
    
           rSH  :  行政区分类
                _:  行政区的详情下级
    
    """

    url = "http://www.xiaomishu.com/shop/search-rSH_PD/"
    sel = getHtmlSel(url=url)
    url_list = sel.xpath("//div[@class='s-district nc-items clearfix']/a/@href")
    print(url_list)
