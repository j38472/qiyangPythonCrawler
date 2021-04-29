#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> demoIp
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/27 10:22
@Desc   ：
=================================================='''

# coding=utf-8
import requests
import myIP

listiii = []


def aa():
    global listiii
    listiii.append("aa")
    print("aa",listiii)


def bb():
    global listiii

    listiii = []
    print("bb",listiii)
def cc():
    global listiii

    print("cc",listiii)



if __name__ == '__main__':
    aa()
    bb()
    cc()
    print()
