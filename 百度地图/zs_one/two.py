#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> two
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-28 10:21
@Desc   ：
=================================================='''

import json
import time

from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options

from myJDBC.jdbc import mySqlJdbc

jdbc = mySqlJdbc()

dataBD_name = "map_baidu_data"


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

if __name__ == '__main__':
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

    kw ='政府机构'

    # addrs = ['郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡','信阳',
    # '焦作', '濮阳', '许昌', '漯河', '三门峡', '卧龙', '商丘', '周口', '驻马店',
    #
    # '新郑市', '新密市', '登封市', '荥阳市', '巩义市', '偃师市', '舞钢市', '汝州市', '林州市', '卫辉市', '辉县市', '沁阳市', '孟州市', '禹州市', '长葛市', '义马市', '灵宝市', '永城市', '项城市', '邓州市', '济源市']
    addrs = [

                # '涧西区','西工区','老城区','瀍河回族区','偃师区','新安县','孟津区','洛宁县','嵩县','栾川县','汝阳县','伊川县',
                # '叶县','郏县','宝丰县','鲁山县','新华区','卫东区','湛河区','石龙区','新城区','高新区','舞钢市','汝州市','林州市','林州市','安阳县','内黄县','汤阴县','滑县','文峰区','北关区','殷都区','龙安区','安阳新区',


        #      '浚县','淇县','淇滨区','山城区','鹤山区','卫滨区','红旗区','牧野区','凤泉区','辉县市','卫辉市','长垣市','新乡县','获嘉县','原阳县','延津县','封丘县',
        # '解放区','山阳区','中站区','马村区','沁阳市','孟州市','修武县','武陟县','博爱','温县',
        # '浉河区', '平桥区', '潢川县', '光山县', '息县', '新县', '罗山县', '商城县', '淮滨县', '固始县',
        # '濮阳县', '清丰县', '南乐县', '范县', '台前县',





        '源汇区', '郾城区', '召陵区', '舞阳县', '临颍县',
        '湖滨区','陕州区','灵宝市','义马市','卢氏县','渑池县',
        '宛城区', '卧龙区，邓州市', '南召县', '镇平县', '内乡县', '淅川县', '新野县', '唐河县', '桐柏县', '方城县', '西峡县', '社旗县',
        '夏邑县', '虞城县', '柘城县', '宁陵县', '睢县', '民权县', '梁园区', '睢阳区',
        '川汇区', '淮阳区', '项城市', '扶沟县', '西华县', '商水县', '沈丘县', '郸城县', '太康县', '鹿邑县',
             '魏都','建安','禹州','长葛','鄢陵','襄城',
        # '','','','','','','','','','','','','','','','','','','','','','',
        #      # '','','','','','','','','','','','','','','','','','','','','','','','','','','','',



             ]

    for add in addrs:
        time.sleep(1.2)

        proxy.new_har("my_baidu", options={'captureHeaders': True, 'captureContent': True})
        bdMapSearch(driver, add+kw)
        time.sleep(3.2)
        getContentText(proxy)