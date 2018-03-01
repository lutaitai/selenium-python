#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost/")

# 输入用户名
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys(u'鹿太太')

# 输入密码
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('123456')

# 点击登录
driver.find_element_by_name('Submit').click()
sleep(8)

# 退出
driver.find_element_by_link_text('退出').click()
sleep(3)
driver.switch_to_alert().accept()


driver.quit()