#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.com")

# 层及定位
# driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys('51zxw')
# sleep(2)
# driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys(6666)

# 逻辑组合定位
driver.find_element_by_xpath("//input[@class='loinp' and @name='username']").send_keys('51zxw')
sleep(2)
driver.find_element_by_xpath("//input[@class='loinp' and @name='password']").send_keys('6666')
