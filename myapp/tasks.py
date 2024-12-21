import json
from sys import intern

from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task(name="sub_task")
def sub(x, y):
    sleep(10)
    return x - y

@shared_task()
def clear_session_cache(ids):
    print("Session cleared: ", ids)
    return ids

@shared_task()
def clear_redis_data(key):
    # Configured this from admin panel with the help of django celery beat.
    print("Redis data cleared: ", key)
    return key

@shared_task()
def clear_rabbitmq_data(key):
    # Configured this from via code
    print("RabbitMQ data cleared: ", key)
    return key

# Create a schedule to run every 20 seconds.
schedule, created = IntervalSchedule.objects.get_or_create(
    every=20,
    period=IntervalSchedule.SECONDS
)

# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic',
    task='myapp.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(['hello'])
)

