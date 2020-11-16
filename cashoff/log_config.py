# -*- coding: utf-8 -*-

'''Log configuration'''

from Cashoff.settings import LOG_ARTICLE_FILE
import logging

def article_logger(name):
    '''Settings for logging in the article app'''

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOG_ARTICLE_FILE)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
