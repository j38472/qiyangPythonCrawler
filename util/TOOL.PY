#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> tool
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-08 15:32
@Desc   ：
=================================================='''


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

        return data