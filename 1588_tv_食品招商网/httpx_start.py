#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> httpx_start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-06-07 9:41
@Desc   ：

            http://www.1588.tv/company/1
=================================================='''
import httpx
import asyncio
import time
from fake_useragent import UserAgent

ua = UserAgent()
header = {
    'User-Agent': ua.random,
    # 'Cookie': 'UM_distinctid=178e8b45023384-0c653d29ec84b5-d7e1938-125f51-178e8b45024845; safedog-flow-item=F0B06A15A0414431C327A36A76D67417; ASP.NET_SessionId=pnd4kr45hhns2k45ddbyof45; Hm_lvt_e2689ecbba89d681b31e360cb5d08d80=1622688527,1623029717; Hm_lpvt_e2689ecbba89d681b31e360cb5d08d80=1623030910; CNZZDATA1973171=cnzz_eid%3D515471263-1618809838-%26ntime%3D1623026108'
}
proxiesNone = {
    "http": None,
    "https": None
}


async def request(client,url):
    print(url)
    resp = await client.get(url, headers=header,proxies = proxiesNone)
    print(resp)
    # result = resp.json()
    # print(result)
    # assert result["code"] == 10200
    exit()

async def getXqUrlList(url):
    print(url)
    httpxHtml = httpx.get(url=url, headers=header, proxies=proxiesNone, verify=False).text
    print(httpxHtml)
    exit()

async def main():
    async with httpx.AsyncClient() as client:
        task_list = []
        for i in range(1,860):
            url = "http://www.1588.tv/company/{}".format(i)
            req = request(client,url)
            task = asyncio.create_task(req)
            task_list.append(task)
        await asyncio.gather(*task_list)


if __name__ == "__main__":
    # 开始
    start = time.time()
    asyncio.run(main())
    # 结束
    end = time.time()
    print(f'异步：发送1000次请求，耗时：{end - start}')
