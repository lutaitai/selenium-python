#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)

driver.implicitly_wait(5)

try:
    c=ctime()
    print ctime()
    driver.find_element_by_css_selector("#kw").send_keys("Python")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print msg
finally:
    print(ctime())

sleep(3)
driver.quit()