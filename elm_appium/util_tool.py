#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：allCool -> util
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-07 13:34
@Desc   ：
        为饿了吗定制的driver操作工具
=================================================='''
import time
import random

from appium import webdriver


class appium_tool():

    def hd_swipe(self, driver, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0):
        driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
        time.sleep(random.uniform(10, 20) / 10)

    def tap_positions(self, driver):
        """
        根据坐标 点击商家的
        :param driver:
        :return:
        """
        positions = [(510, 827), (632, 909)]
        driver.tap(positions, duration=100)
        time.sleep(random.uniform(30, 70) / 10)
