import datetime

import requests
from fake_useragent import UserAgent
from urllib.parse import quote
from urllib.parse import unquote
import craw
from requests.adapters import HTTPAdapter

'''=================================================
@Project -> File   ：qiyangPythonCrawler
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/25 14:04
@Desc   ：启动项  入口处
================================================='''
if __name__ == '__main__':
    Headers = {
    'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }

    url = "https://www.google.com.hk"

    keep = True
    maxtimes = 3
    count = 0
    print(datetime.datetime.now())
    while keep and count < maxtimes:
        try:
            res = requests.head(url=url, headers=Headers, timeout=5)
            keep = False
        except Exception as e:
            print(datetime.datetime.now())
            count = count + 1
            print('重试' + str(count))
    # # 获取电话号
    # craw.start();
    #
    #
    # print(unquote("%E9%A5%AE%E6%96%99"))
    # ua = UserAgent()
    # print(ua.ie)
    # print(ua.opera)
    # print(ua.chrome)
    # print(ua.google)
    # print(ua['google chrome'])
    # print(ua.firefox)
    # print(ua.ff)
    # print(ua.safari)

    # i = 0;
    # while (i < 50):
    #     print(ua.random)
    #     i += 1
