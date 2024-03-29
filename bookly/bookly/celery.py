from __future__ import absolute_import,unicode_literals

from celery import Celery

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','bookly.settings')

celery=Celery('bookly')

celery.config_from_object('django.conf:settings','CELERY')

celery.autodiscover_tasks()