"""
This module contains a simple tasks that accepts two parameters:
    - priority of the queue
    - a message
and prints those parameters
"""
from datetime import datetime
from celery import Celery

celery = Celery()
celery.main = 'Test app'
celery.config_from_object('celeryconfig')
celery.autodiscover_tasks(
    ['tasks'],
    force=True
)


@celery.task
def task(prio, message):
    print(f'{prio}: {message}')
