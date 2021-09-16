#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-06 11:21
@Desc   ：
=================================================='''

"""

使用selessium  获取json  数据请求参数   
然后用requests   获取数据 并解析

两个搜索词的库
    1.地名库::
        每一个城市  一个地点的库 用做搜索词 
        在搜索的时候  需要把城市的名字给加上去 有可能存在多个城市存在一个地名
    2.饮食库::
        现在百度自身的搜索词 有点少

dervi  打开的页面  要注意   有些搜索词的  出来的数据并不多


注意:::
    根据坐标系   无法直接定位到  具体街区
    
    
    
    
    
现在已经可以成功获取到 selenium 请求页面的URL   根据 selenium 生成的json   URL  和对应的Cookie   请求json  数据  


根据生成的URl和cookie 请求到的json 可以一次获取到本次搜索的所有数据

    
"""
