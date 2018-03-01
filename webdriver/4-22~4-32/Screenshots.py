from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")
driver.get_screenshot_as_file(r"F:\selenium lianxi\webdriver\51zxw.jpg")

driver.get("http://www.baidu.com")
driver.get_screenshot_as_file(r"F:\selenium lianxi\webdriver\baidu.png")

sleep(2)
driver.quit()