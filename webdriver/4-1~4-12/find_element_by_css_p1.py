#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# 根据ID定位
# driver.find_element_by_css_selector("#kw").send_keys("selenium")
#根据class定位
# driver.find_element_by_css_selector('.s_ipt').send_keys(u"selenium 我要自学网")
# 根据属性定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys(u"selenium 我要自学网")


# 通过元素层级定位
driver.get("http://www.51zxw.net")
driver.find_element_by_css_selector("form#loginForm>ul>input[type='password']").send_keys("51zxw")
# driver.find_element_by_css_selector('#kw').send_keys(u"selenium 我要自学网")

sleep(2)
# driver.find_element_by_id("su").click()
sleep(2)
driver.quit()
