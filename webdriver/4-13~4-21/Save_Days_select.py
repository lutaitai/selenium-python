from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
sleep(2)

#利用select来定位
select=Select(driver.find_element_by_css_selector("[name='CookieDate']"))
#选项
# select.select_by_index(1)
#文字
# select.select_by_visible_text("留一月")
#属性
select.select_by_value("2")

sleep(3)
driver.quit()
