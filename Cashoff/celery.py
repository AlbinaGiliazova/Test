# -*- coding: utf-8 -*-
'''Configuration for Celery'''

import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cashoff.settings')
celery_app = Celery('Cashoff')
celery_app.conf.broker_url = 'redis://:Z80mBEm3fmHcJH02sSsYqnmBEgZK1lvX@redis-13583.c232.us-east-1-2.ec2.cloud.redislabs.com:13583/0'
celery_app.conf.timezone = 'Europe/Moscow'

# From: https://webdevblog.ru/python-celery/
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()

# this allows you to schedule items in the Django admin.
celery_app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

celery_app.conf.beat_schedule = {
        'parse-every-day': {
            'task': 'parsing_task',
            'schedule': crontab(hour=17, minute=15),
            }
        }


