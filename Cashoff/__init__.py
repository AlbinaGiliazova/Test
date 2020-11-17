'''celery into Django at startup'''

from .celery import celery_app

# https://webdevblog.ru/asinhronnye-zadachi-v-django-s-redis-i-celery/
__all__ = ('celery_app',) 