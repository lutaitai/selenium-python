#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

driver.find_element_by_link_text(u"程序开发").click()
sleep(2)
driver.find_element_by_partial_link_text(u"神秘面纱").click()

sleep(2)
driver.quit()
