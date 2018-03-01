#!/usr/bin/env Python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://baidu.com")

# driver.find_element_by_id("kw").send_keys(u"Selenium 我要自学网")
driver.find_element_by_name("wd").send_keys(u"Selenium 我要自学网")

sleep(2)
driver.find_element_by_id("su").click()
sleep(3)

driver.quit()
