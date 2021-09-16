#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> tool
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-08 15:32
@Desc   ：
=================================================='''
import re
import time


class MyToolUtil:

    def set_Qx_Data(self, data):
        """
        清洗数据
        :param data:
        :return data:
        """
        data = data.replace(" ", "")
        data = data.replace("\r", "")
        data = data.replace("\n", "")
        data = data.replace("-", "")
        data = data.replace("电话：", "")
        # data = data.replace(" ","")

        return data

    def get_SJC10(self):
        t = time.time()
        t = int(t)
        return str(t)

    def get_SJC13(self):
        millis = int(round(time.time() * 1000))
        return millis

    def getsjCall(self, data):
        try:
            sj = re.search(r"1[0-9]{10}", data, flags=re.S).group(0)
            return sj
        except Exception as e:
            print(e)
        return ""

    def getSjList(self, data):
        # print(data)
        try:
            result = re.findall(r"联系方式：(1[0-9]{10})", data, flags=re.S)
            return set(result)
        except Exception as e:
            print(e)

    def getSjAllList(self, data):
        """
        正则表达式直接匹配整个 页面 ,获取所有 "\D(1[0-9]{10})\D" 并返回set
        :param data:
        :return: set
        """
        # print(data)
        try:
            result = re.findall("\D(1[0-9]{10})\D", data, flags=re.S)
            # print(result)
            # exit()
            return set(result)
        except Exception as e:
            print("getSjAllList          ", e)

    def getReStrAllList(self, ReStr, data):
        """
        正则表达式直接匹配整个 页面 ,获取所有 "\D(1[0-9]{10})\D" 并返回set
        :param data:
        :return: set
        """
        # print(data)
        try:
            result = re.findall(ReStr, data, flags=re.S)
            # print(result)
            # exit()
            return set(result)
        except Exception as e:
            print("getSjAllList          ", e)

    def getReData(self, ReStr, data):
        # print(data)
        try:
            result = re.search(ReStr, data, flags=re.S).group(1)
            return result
        except Exception as e:
            print("getReData          ", e)

    def getReData0(self, ReStr, data):
        # print(data)
        try:
            result = re.search(ReStr, data, flags=re.S).group(0)
            return result
        except Exception as e:
            print("getReData          ", e)
