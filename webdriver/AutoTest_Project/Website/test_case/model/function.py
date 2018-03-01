#!/usr/bin/env Python
# coding=utf-8

from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from time import sleep

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    print(func_path)

    base_dir=os.path.dirname(func_path)
    print(base_dir)

    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    print(base_dir)

    base=base_dir.split('/Website')[0]
    print(base)
    filepath=base+'/Website/test_report/screen_shot/'+filename
    print("filepaht:"+filepath)
    driver.get_screenshot_as_file(filepath)

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f .close()

    smtpsever='smtp.163.com'
    # 发送邮箱用户名和密码
    user='18701873051@163.com'
    password='123jhh'

    # 发送和接收邮箱
    sender='18701873051@163.com'
    receives=['jhh5845201314@126.com','770464963@qq.com','2430033501@qq.com']

    # 发送邮件主题和内容
    subject='Web Selenium 自动化报告'

    # HTML邮件正文
    msg=MIMEText(mail_content,'html','utf-8')
    msg['subject']=subject
    msg['From']=sender
    msg['To']=','.join(receives)

    smtp=smtplib.SMTP_SSL(smtpsever,465)
    # helo向服务器标识用户身份
    smtp.helo(smtpsever)
    # 服务器返回结果确认
    smtp.ehlo(smtpsever)
    # 登录邮箱服务器用户名和密码
    smtp.login(user,password)

    print("Start send email...")
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print("Send email end")

def latest_report(report_dir):
    lists=os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))

    print("the latest report is "+lists[-1])

    file =os.path.join(report_dir,lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver,'sougou.jpg')
    driver.quit()