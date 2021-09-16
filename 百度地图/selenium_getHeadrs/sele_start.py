#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qiyangPythonCrawler -> start
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-09 16:58
@Desc   ：
=================================================='''
from time import sleep

from selenium import webdriver

options = webdriver.ChromeOptions()

# options.add_argument('----')

driver = webdriver.Chrome("D:\\driver\\chromedriver\\chromedriver.exe")

ssc = """美食 餐厅 饭店 食物 餐馆 餐饮 川菜 湘菜 粤菜 东北菜 江浙菜 浙菜 意大利菜 法国菜 德国菜 俄罗斯菜 中东料理 日韩料理 泰国菜 越南菜 印度菜 菲律宾菜 印尼菜 东南亚菜 中式快餐 西餐 中餐 肯德基 麦当劳 德克士 必胜客 王婆大虾 海底捞 真功夫 永和大王 小肥羊 味千拉面 大娘水饺 蜜雪冰城 汉堡王 烤鸭 火锅 自助餐 烧烤 海鲜 小吃 汉堡 披萨 牛排 寿司 快餐 甜点 冷饮 茶饮 冰淇淋 饮品 面包 西点 烤肉 羊蝎子 米线 涮羊肉 虾 蟹 饺子 水饺 串串香 卤味 香锅 外卖 早餐 美食广场 酒店 地方小吃 食堂 
"""

dm = "郑州"
wd = "披萨"
driver.get(url="https://map.baidu.com/")

sleep(6)

cookies_all = driver.get_cookies()

print(cookies_all)

sleep(3)

current_url_Str = driver.current_url

sleep(3)
print(current_url_Str)

driver.close()
