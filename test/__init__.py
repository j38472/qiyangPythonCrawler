#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/5/7 10:15
@Desc   ：
=================================================='''

# from apscheduler.schedulers.blocking import BlockingScheduler
#
# ##  apscheduler定时框架
# def get_data(self,_quene):
#     '''
#     使用apscheduler定时框架创建定时任务
#     '''
#     # 创建调度器对象
#     scheduler = BlockingScheduler()
#     # 添加定时任务
#     scheduler.add_job(self.get_bar, 'cron', second='*/10', args=[_quene])
#     # 启动调度器，后台监控定时任务，到点执行
#     scheduler.start()
import base64
import datetime
import time

from myJDBC.jdbc import mySqlJdbc


def get_sc():
    jdbc = mySqlJdbc()

if __name__ == '__main__':
    time1 = "2021-06-30 09:54:02"
    time2 = "2021-06-30 09:54:06"
    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    delta = d2 - d1

    # if delta > '0:00:04':
    #     print("Cccc")

    # print(delta.seconds)
    second = delta.seconds
    if second < 30:
        print("哦买噶 这两个列表页  结束时间戳 相差小于30秒")
    else:
        print("哈利路亚 两个列表页  结束时间戳  相差大于30秒")
    exit()
    # print(base64.b64decode("aaaaaaaa"))
    pass
