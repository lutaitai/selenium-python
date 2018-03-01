#!/usr/bin/env Python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpsever='smtp.163.com'

user='18701873051@163.com'
password='123jhh'

sender='18701873051@163.com'
receive='jhh5845201314@126.com'

subject=u'Web selenium 自动化测试报告'
content='<html><h1 style="color:red">我要自学网，自学成才</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['subject']=Header(subject,'utf-8')
msg['From']='18701873051@163.com'
msg['TO']='jhh5845201314@126.com'

smtp=smtplib.SMTP_SSL(smtpsever,465)
smtp.helo(smtpsever)
smtp.ehlo(smtpsever)
smtp.login(user,password)

print("start send email...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("send email end!")