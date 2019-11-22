#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import
import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from sbcelery.usecelery import sb_app

from sbcelery.utils.send_email import pack_html, send_email

@sb_app.task
def tsend_email():
   url = "http://www.baidu.com"
   receiver = '2540757573@qq.com'
   content = pack_html(receiver, url)
   # content = 'this is email content.'
   send_email(receiver, "fdsfgsdf")
   print('send email ok!')

@sb_app.task
def add(x, y):
   return x+y
