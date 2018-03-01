#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)

driver.find_element_by_css_selector("#kw").send_keys("Python")

#显示等待--判断搜索按钮是否存在
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
element.click()

sleep(3)
driver.quit()

