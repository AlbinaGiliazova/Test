# -*- coding: utf-8 -*-
'''Celery Tasks'''

from article.parsing import parse


@app.tasks(name='parsing')
def parsing():
    parse()

@app.tasks(name='parsing_starter')
def parsing_starter():
   parsing.delay()
