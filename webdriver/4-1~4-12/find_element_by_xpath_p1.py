#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://baidu.com")

# 绝对路径定位
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys(u"51zxw")

# 利用元素熟悉定位--定位到input标签中为kw/wd/class属性为s_ipt的元素
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

# driver.find_element_by_xpath("//input[@name='wd']").send_keys("selenium")

driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("selenium")
sleep(2)
driver.find_element_by_id("su").click()
sleep(2)
driver.quit()