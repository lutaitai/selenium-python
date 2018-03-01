#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
sleep(2)

# 将滚动条拖到最底部
js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(4)

# 将滚动条拖到最顶部
js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(3)

driver.quit()