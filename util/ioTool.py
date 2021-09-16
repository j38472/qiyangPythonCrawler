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


    def DataQPXlsx(self,list_data_all):
        data_list_len = len(list_data_all)

        gs = 2

        print()
        qwe = int(data_list_len/gs)

        for g in range(qwe):
            print(g)
        # data1 = list_data_all[0:2]
        # data2 = list_data_all[2:4]
        # data3 = list_data_all[4:6]
        # data4 = list_data_all[6:8]
        # data5 = list_data_all[8:]
        # print(len(data1))
        # print(len(data2))
        # print(len(data3))
        # print(len(data4))
        # print(len(data5))



if __name__ == '__main__':
    ioxlsxMy = MyIoToolUtil()
    c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    ioxlsxMy.DataQPXlsx(c)