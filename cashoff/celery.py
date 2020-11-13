# -*- coding: utf-8 -*-
'''For using Celery in the project: 
    https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732'''

import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cashoff.settings')
 
app = Celery('cashoff')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
