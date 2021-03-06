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

dataBD_name = "map_baidu_data1"
dataBD_addrssName = "zz_dqname"

def bdMapSearch(driver, keys):
    try:
        input_box = driver.find_element_by_xpath("//input[@id='sole-input']")
        input_box.clear()
        input_box.send_keys(keys)
        time.sleep(1.2)
        driver.find_element_by_xpath("//button[@id='search-button']").click()
    except Exception as e:
        pass

def jxJsonWb(json_content):
    for json_data in json_content:
        # print(json_data)
        # print(len(json_data))
        # print(type(json_data))
        # print("<><>" * 20)
        addrs = ''
        name = ""
        sjdh = ''
        try:
            addrs = json_data['addr']
            # print("addr     ", addrs)
        except Exception as e:
            pass
            # print(e)

        try:
            name = json_data['name']
            # print("name     ", name)
        except Exception as e:
            pass

        try:
            sjdh = json_data['tel']
            # print("tel     ", sjdh)
        except Exception as e:
            pass

        if len(sjdh) > 7:
            sjGS = jdbc.getSjGs(sj=sjdh, dataBD=dataBD_name)
            if sjGS < 1:
                name = name.replace("'", "")
                addrs = addrs.replace("'", "")
                jdbc.inXqDate(name=name, url="", zy="", lxr="", dh="", sj=sjdh, dz=addrs, dataBD=dataBD_name)

def getContentText(proxy):
    try:
        count_json_text_len = 1
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
                        # print("len(json_text)   ", count_json_text_len)

                        # print("json_text    ", json_text)
                        # print("---------------------------" * 22)
                        jxJsonWb(json_text)
        return count_json_text_len
    except Exception as e:
        pass

def start_sss(addr_datas):
    # dictProt = {'port': 5678}D
    server = Server(r"D:\driver\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat")
    server.start()
    proxy = server.create_proxy()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=r'D:\driver\chromedriver\chromedriver.exe', options=chrome_options)

    driver.get(url="https://map.baidu.com/")

    # time.sleep(3)
    # exit()
    # c = []
    # print(c[2])

    # addr_datas = jdbc.get_BD_Data(dataBD_addrssName)
    count = 0
    wd_one_s = [
                # '美食',
                # '餐厅',
                # '饭店',
                # '中餐厅',
                # '西餐厅',
                # '甜品冷饮',
                # '快餐',
                # '日韩料理',
    ]
    count_js_close = 0
    cs_count_sql = 1
    for addr_data in addr_datas:
        time.sleep(0.8)

        proxy.new_har("my_baidu", options={'captureHeaders': True, 'captureContent': True})

        # print(addr)
        addr = addr_data[1]
        id = addr_data[0]

        start_time = time.time()

        for wd in wd_one_s:
            print("郑州" + addr + wd)
            wordpass = "郑州" + addr + wd

            time.sleep(1.2)
            bdMapSearch(driver, wordpass)
            time.sleep(3.2)

            cs_count_sql += getContentText(proxy)

            time.sleep(1.6)

            count += 1
        end_time = time.time()
        print("本次关键词用时:::::::::: ", end_time - start_time)
        jdbc.updata_zzDQName(count=cs_count_sql, idS=id)
        count_js_close += 1

    print("郑州一共的搜索词有   ", count, "  个  ")


if __name__ == '__main__':
    addrssName5_6q = jdbc.getData_startID_endID(dataBD_addrssName, 5000, 6000)
    addrssName8_9q = jdbc.getData_startID_endID(dataBD_addrssName, 8000, 9000)

    # print(len(addrssName5_6q))
    # print(len(addrssName8_9q))
    # exit()

    time.sleep(1.2)
    start_sss(addrssName5_6q)

    time.sleep(1.2)
    start_sss(addrssName8_9q)
