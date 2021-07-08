#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> ioTool
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-07-08 13:50
@Desc   ：
=================================================='''
import pandas as pd
import numpy as np


class MyIoToolUtil:
    def outXlsx(self, data, dataFile):
        """
        生成Xlsx文件  一维的
        :param data: 数组
        :param dataFile: 文件路径和文件名字
        :return:
        """
        data_df = pd.DataFrame(data)
        # data_df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # data_df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        writer = pd.ExcelWriter(dataFile)
        data_df.to_excel(writer, float_format='%.5f')
        writer.save()
