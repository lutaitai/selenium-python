#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
# 设置网页路径，r代表转义
file_path=r'F:\selenium lianxi\webdriver\Frame.html'
# 路径转义另一种方法
# file_path='F:\\selenium lianxi\\webdriver\\Frame.html'
driver.get(file_path)

# 切换到frame页面内******
driver.switch_to.frame("search")

driver.find_element_by_css_selector("#query").send_keys("Python")
sleep(2)
driver.find_element_by_css_selector("#stb").click()

sleep(2)
driver.quit()
