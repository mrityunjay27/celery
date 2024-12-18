from django.shortcuts import render
from celeryproject.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult
# Create your views here.

# def index(request):
#     print("Result: ")
#     ans = add.delay(10,20)
#     print("Add Result: ", ans)  # ans will hold id of process, after 19 second result will be printed on terminal
#     subs = sub.apply_async(args=[10,20])
#     print("Sub Result: ", subs)
#     return render(request, "myapp/home.html")

# Displaying result after task execution.

def check_result(request, task_id):
    # Retrieve the task result using the task ID
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())

    return render(request, "myapp/result.html", {'result': result})


def index(request):
    result = add.delay(19,1)
    return render(request, "myapp/home.html", {'result': result})



def about(request):
    print("Result: ")
    return render(request, "myapp/about.html")

def contact(request):
    print("Result: ")
    return render(request, "myapp/contact.html")