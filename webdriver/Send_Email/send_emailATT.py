#!/usr/bin/env Python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpsever='smtp.163.com'

user='18701873051@163.com'
password='123jhh'

sender='18701873051@163.com'
receives=['jhh5845201314@126.com','770464963@qq.com','2430033501@qq.com']

subject='Web Seleniun 自动化测试报告'
content='<html><h1 style="color:red">我要自学网,自学成才</h1></html>'

send_file=open(r'F:\selenium lianxi\webdriver\zzz.png','rb').read()

att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-strem'
att['Content-Disposition']='attachment;filename="logo.png"'

msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpsever,465)
smtp.helo(smtpsever)
smtp.ehlo(smtpsever)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print("Send email end")
