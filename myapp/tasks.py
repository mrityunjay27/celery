from celery import shared_task
from time import sleep

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