#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-15 9:15
@Desc   ：
=================================================='''

import json
import time
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options

from myJDBC.jdbc import mySqlJdbc

jdbc = mySqlJdbc()

server = Server(r"D:\driver\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()

dataBD_name = "map_baidu_data1"


def bdMapSearch(driver, keys):
    input_box = driver.find_element_by_xpath("//input[@id='sole-input']")
    input_box.clear()
    input_box.send_keys(keys)
    time.sleep(1.2)
    driver.find_element_by_xpath("//button[@id='search-button']").click()


def jxJsonWb(json_content):
    for json_data in json_content:
        # print(json_data)
        print(len(json_data))
        print(type(json_data))
        print("<><>" * 20)
        addrs = ''
        name = ""
        sjdh = ''
        try:
            addrs = json_data['addr']
            # print("addr     ", addrs)
        except Exception as e:
            print(e)

        try:
            name = json_data['name']
            # print("name     ", name)
        except Exception as e:
            print(e)

        try:
            sjdh = json_data['tel']
            # print("tel     ", sjdh)
        except Exception as e:
            print(e)

        if len(sjdh) > 7:
            gs = jdbc.getSjGs(sj=sjdh, dataBD=dataBD_name)
            if gs < 1:
                jdbc.inXqDate(name=name, url="", zy="", lxr="", dh="", sj=sjdh, dz=addrs, dataBD=dataBD_name)


def getContentText():
    count_json_text_len = 0
    result = proxy.har
    for rs in result['log']['entries']:
        data = rs['request']['method'], rs['request']['url']
        url_data = rs['request']['url']
        content_data = rs['response']['content']

        if url_data.find("map.baidu.com/?newmap=") > 1:
            # print(url_data)
            # print(content_data)
            sizeGs = content_data['size']
            if sizeGs > 20000:
                text__Ccc = content_data['text']

                if len(text__Ccc) > 100000:
                    # print(len(text__Ccc))
                    json_text = json.loads(text__Ccc)['content']
                    count_json_text_len += len(json_text)
                    print("len(json_text)   ", count_json_text_len)

                    # print("json_text    ", json_text)
                    print("---------------------------" * 22)
                    jxJsonWb(json_text)
    return count_json_text_len


if __name__ == '__main__':
    # getContentText()
    # exit()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
    proxy.new_har("my_baidu", options={'captureHeaders': True, 'captureContent': True})
    driver.get(url="https://map.baidu.com/")

    # time.sleep(3)
    # exit()
    # c = []
    # print(c[2])

    addr_datas = jdbc.get_BD_Data("zz_dqname")
    count = 0
    wd_one_s = ['美食',
                '餐厅',
                '饭店',
                '中餐厅',
                '西餐厅',
                '甜品冷饮',
                '快餐',
                '日韩料理', ]
    for addr_data in addr_datas:
        # print(addr)
        addr = addr_data[1]
        id = addr_data[0]
        for wd in wd_one_s:
            print("郑州" + addr + wd)
            wordpass = "郑州" + addr + wd

            time.sleep(3)
            bdMapSearch(driver, wordpass)
            time.sleep(7)
            cs_count_sql = getContentText()
            time.sleep(3)

            count += 1
        jdbc.updata_zzDQName(count=cs_count_sql, idS=id)
    print("郑州一共的搜索词有   ", count, "  个  ")

    # time.sleep(7)
    # c = ["郑州建设路美食", "郑州棉纺路美食"]
    # for ssc in c:
    #     bdMapSearch(driver, ssc)
    #     time.sleep(7)
    #     getContentText()
    #     time.sleep(7)

    driver.close()
