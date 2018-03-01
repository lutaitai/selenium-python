#!/usr/bin/env Python
# coding=utf-8

import unittest
from BSTestRunner import BSTestRunner
import time
import smtplib                       #发送邮件模块
from email.mime.text import MIMEText  #定义邮件内容
from email.header import Header       #定义邮件标题
import os

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
    report_dir='./test_report'
    test_dir='./test_case'
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+'result.html'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    with open(report_name,'wb') as f:
        runner=BSTestRunner(stream=f,title='Test Report',description='baidu search')
        runner.run(discover)
    f.close()
    # 获取最新测试报告
    latest_report=latest_report(report_dir)
    # 发送邮件报告
    send_mail(latest_report)





