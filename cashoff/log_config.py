# -*- coding: utf-8 -*-

'''Log configuration'''

from Cashoff.settings import LOG_DB_FILE
import logging

def db_logger(name):
    '''Settings for loggers'''

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOG_DB_FILE)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger