#!/usr/bin/env Python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpsever='smtp.163.com'

user='18701873051@163.com'
password='123jhh'

sender='18701873051@163.com'
receives=['jhh5845201314@126.com','770464963@qq.com','2430033501@qq.com']

subject='Web Seleniun 自动化测试报告'
content='<html><h1 style="color:red">我要自学网,自学成才</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['subject']=Header(subject,'utf-8')
msg['From']=sender
msg['TO']=','.join(receives)

smtp=smtplib.SMTP_SSL(smtpsever,465)
smtp.helo(smtpsever)
smtp.ehlo(smtpsever)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msg.as_string())
smtp.quit()
print("Send email end")