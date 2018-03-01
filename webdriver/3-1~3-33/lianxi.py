#!/usr/bin/env Python
# coding=utf-8

import csv
csv_file=csv.reader(open('Stu_info.csv','r'))
for stu in csv_file:
    print(stu)

stu=['Marry',28,'Changsha']
stu1=['Rom',23,'Chengdu']

out=open('Stu_info.csv','a',newline='')
csv_write=csv.writer(out,dialect='excel')
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("Write File Over!")


from xml.dom import minidom

dom=minidom.parse('Class_info.xml')
root=dom.documentElement

names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')

for i in range(4):
    print(names[i].fisstChild.data)
    print(ages[i].fisstChild.data)
    print(citys[i].fisstChild.data)

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

driver.find_element_by_tag_name('option')[1].click()
driver.find_element_by_css_selector("[value='2]").click()

driver.quit()




driver=webdriver.Firefox()
driver.get("http://www.baidu.com")




