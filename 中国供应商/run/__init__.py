import requests
from fake_useragent import UserAgent
from urllib.parse import quote
from urllib.parse import unquote
import craw
'''=================================================
@Project -> File   ：qiyangPythonCrawler
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/25 14:04
@Desc   ：启动项  入口处
================================================='''
if __name__ == '__main__':
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # "https://www.china.cn/chuishishebei/4152876380.html"
    response = requests.get(url="url", headers=headers).text


    # 获取电话号
    craw.start();


    print(unquote("%E9%A5%AE%E6%96%99"))
    ua = UserAgent()
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
