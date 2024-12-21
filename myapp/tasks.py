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