#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# 手动添加Cookie
driver.add_cookie({'name':'BAIDUID','value':'23C3EC7629B20559B40F0C5BACFCE150:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'3RhVHZnN0lKT0FlcEkyVi1INVdKRmVJZ05IVTJ2ZHZLdGFSQWZjZmxPYlhwSHBhQUFBQUFBJCQAAAAAAAAAAAEAAAAJjhs2vL7ErMSpaGFwcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANcXU1rXF1NaN'})

sleep(3)
driver.refresh()

sleep(3)