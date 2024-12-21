import os
from datetime import timedelta
from time import sleep
from celery.schedules import crontab

from django.conf import settings

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')
app.conf.update(
    imports=[
        'myapp.tasks',
    ]
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="Addition_Task")
def add(x,y):
    sleep(19)  # Sleep to make ut async
    return x +y

# Method 2 of running task with celery beat.
# app.conf.beat_schedule = {
#     'every-10-seconds': {
#             'task': 'myapp.tasks.clear_session_cache',
#             'schedule': 10,
#             'args': (10101,),
#         },
# }


# # Use of timedelta
# app.conf.beat_schedule = {
#     'every-10-seconds': {
#             'task': 'myapp.tasks.clear_session_cache',
#             'schedule': timedelta(seconds = 10),
#             'args': (10101,),
#         },
# }

# Use of crontab
# Advantage over time delta : Specific time points (e.g., every minute or daily at 6 PM).
app.conf.beat_schedule = {
    'every-10-seconds': {
            'task': 'myapp.tasks.clear_session_cache',
            'schedule': crontab(minute='*/1'),  # Runs every 1 minute
            'args': (10101,),
        },
}