from __future__ import absolute_import, unicode_literals

# The shared_task decorator is used to create reusable Celery tasks 
# that can be shared across different parts of your Django application.
from celery import shared_task

@shared_task()
def add(x,y):
    return x+y
    