#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element(By.ID,'kw').clear()
driver.find_element(By.NAME,'wd').send_keys("selenium")
driver.find_element(By.CLASS_NAME,'s_ipt').send_keys(u"自学网")
driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("Python")

sleep(3)
driver.find_element(By.ID,'su').click()
sleep(5)
driver.quit()