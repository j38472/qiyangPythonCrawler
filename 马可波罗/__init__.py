#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> __init__.py
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021/4/30 15:15
@Desc   ：
            列表页:::::::
            http://china.makepolo.com/list/d16/
            这个列表页面   d 的范围在1(包含)--25(不包含)
            例子: https://china.makepolo.com/list/spc327/
            !!!!注意 本页面是产品界面  并非是企业目录
            最后一层的列表页  只显示其中一百页面  可以添加参数

            可以进入企业 的目录 去获取详情页面 的URL
            这个列表  数据量并不多  通常都是在一百页以下
            本网站可以通过获取下一页的URL  来判断是否进行继续对自己  递归
            详情页::::::::::
            进入  联系我们 的页面  相关数据 本页面全部都有
            电话号和手机号是 js 异步加载的 照片
            照片的 URL 在照片的标签里面
            <img src="/purchase/buildStringToimg.php?t_page=pro&phone=ff96h8xhvRFXlNjvzMhyxvBJptXUuC39mNYAeiCq8JquXKJ*GqgxqQ"style="padding: 19px 0 0 5px;">
            src : 里面的数据 取出  在与  http://ct1234h.cn.makepolo.com 拼接后面  即可获取到照片
            rf ua 应该需要设置
            先生成一个标准库  再搞到坐标值
=================================================='''

import requests

if __name__ == '__main__':
    proxies = {"http": None, "https": None}
    url = "http://senbaoyuan02.cn.makepolo.com/contact_us.html"
    htmlpage = requests.get(url=url,proxies=proxies).text
    print(htmlpage)
