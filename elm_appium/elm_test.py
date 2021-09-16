#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：allCool -> elm_test
@IDE    ：PyCharm
@Author ：Mr. cyh
@Date   ：2021-09-07 11:09
@Desc   ：
=================================================='''
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from elm_appium.util_tool import appium_tool

appium_tool_util = appium_tool()

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0.0',
    'deviceName': 'VBJ0218526009881',
    'appPackage': 'com.huawei.android.launcher',
    'appActivity': 'unihome.UniHomeLauncher',
    'automationName': 'Uiautomator2',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    # 'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_accessibility_id("饿了么")
el1.click()
time.sleep(5)

appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=200)       #这个应该管用了
# appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=130)  #这个应该管用了
# appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=100)
# appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=200)
# appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=200)
# appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=200)
# appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=300)

time.sleep(4)
#
el2 = driver.find_element_by_xpath(
    # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
    "//android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]"
)
el2.click()
time.sleep(5)



"""
商家                                                荣耀十的窗口 1-5
第一次遍历商家xpath  索引从三开始
//android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]
                                 
"""

# print(driver.contexts)
# print(driver.page_source)
# exit()

#  点击商家 进入商家信息页面
febx = driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[3]")
febx.click()


# 根据坐标跳转到商家信息页面
# appium_tool_util.tap_positions(driver)


appium_tool_util.hd_swipe(driver, 477, 1950, 630, 1286, duration=200)

# 点击 电话号
febx1 = driver.find_element_by_xpath("//android.widget.ImageView[1]")
febx1.click()


# print(driver.contexts)
# print(driver.page_source)

febx2 = driver.find_element_by_xpath("//android.widget.EditText")
print(driver.contexts)
print("<><><>"*33)
print(driver.page_source)
print("<><><>"*33)
print(febx2.text)
exit()








time.sleep(5)

driver.quit()
driver.close()
time.sleep(5)

el3 = driver.find_element_by_xpath(
    "//*[@id=\"screenshotContainer\"]/div/div/div/div/div/div[75]")
el3.click()
time.sleep(3)
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
el4.click()
time.sleep(10)
e5 = driver.find_element_by_id("com.android.contacts:id/digits")
print(e5.text)

driver.quit()

"""
//*[@id="screenshotContainer"]/div/div/div/div/div/div[148]
"""
