#!/usr/bin/env python  
# encoding: utf-8  
#目的是拒绝隐式引入，celery.py和celery冲突。
from __future__ import absolute_import,unicode_literals 
import os
from celery import Celery
from django.conf import settings

# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")

#创建celery应用
sb_app = Celery('untitled',broker='amqp://guest:guest@localhost:5672')
sb_app.config_from_object('django.conf:settings')
#如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。比如你添加了一个任#务，在django中会实时地检索出来。
sb_app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)