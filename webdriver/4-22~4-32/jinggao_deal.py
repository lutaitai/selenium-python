#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_link_text("设置").click()
sleep(1)
driver.find_element_by_link_text("搜索设置").click()
sleep(2)
driver.find_element_by_link_text("保存设置").click()
sleep(3)
# 处理警告窗口
alert=driver.switch_to_alert()
alert.accept()
sleep(2)

driver.quit()