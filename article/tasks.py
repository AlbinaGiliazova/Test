# -*- coding: utf-8 -*-
'''Periodic tasks'''

from Cashoff import celery_app


@celery_app.task(name='parsing_task')
def parsing_task():
    
    from article.parsing import parse
    parse()   