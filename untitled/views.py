from django.shortcuts import render
from django.http import Http404, HttpResponse
import json
from sbcelery.tasks import tsend_email,add
from sbcelery.utils.send_email import pack_html, send_email

# Create your views here.

def hello(request):
    sdfdsf = add.delay(3,4)
    # tsend_email.delay()
    # content = 'this is email content.'
    smtp = "smtp.qq.com"
    sender = '1156145880@qq.com'
    receiver = '2540757573@qq.com'
    # 授权密码
    pwd = 'l123gfeabcy'

    title = "hello I am xxx"
    contents = "{}发送给{}的邮件".format(sender, receiver)

    try:
        ldqplxo = MIMEText(contents, 'plain', 'utf-8')
        ldqplxo['From'] = Header(sender, 'utf-8')
        ldqplxo['To'] = Header(receiver, 'utf-8')
        ldqplxo['Subject'] = Header(title, 'utf-8')
        mbdrewr = smtplib.SMTP_SSL(smtp, 465)
        mbdrewr.login(sender, pwd)
        mbdrewr.sendmail(sender, receiver, ldqplxo.as_string())
        mbdrewr.quit()
    except Exception as e:
        print('错误>>>', e)
    return HttpResponse("sfg");

# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

