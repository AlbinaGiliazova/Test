# -*- coding: utf-8 -*-
'''Schedule for Celery'''

from celery.schedules import crontab

# from: https://habr.com/ru/post/461775/
CELERYBEAT_SCHEDULE = {
   'parsing_starter': {
     'task': 'parsing_starter',
     'schedule': crontab(hour=18),
  },
}
