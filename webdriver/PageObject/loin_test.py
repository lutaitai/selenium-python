#!/usr/bin/env Python
# coding=utf-8

from LoginPage1 import *
from selenium import webdriver

driver=webdriver.Firefox()

username=u'鹿太太'
password='123456'

test_user_Login(driver,username,password)
sleep(6)

driver.quit()