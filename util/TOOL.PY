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

    def set_Qx_Data(self,data):
        """
        清洗数据
        :param data:
        :return data:
        """
        data = data.replace(" ","")
        data = data.replace("\r","")
        data = data.replace("\n","")
        data = data.replace("-","")
        data = data.replace("电话：","")
        # data = data.replace(" ","")

        return data

    def get_SJC10(self):
        t = time.time()
        t = int(t)
        return str(t)
    def get_SJC13(self):
        millis = int(round(time.time() * 1000))
        return millis
    def getsjCall(self,data):
        try:
            sj = re.search(r"1[0-9]{10}", data, flags=re.S).group(0)
            return sj
        except Exception as e:
            print(e)
        return ""



