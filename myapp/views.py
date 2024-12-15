from django.shortcuts import render
from celeryproject.celery import add
# Create your views here.

def index(request):
    print("Result: ")
    ans = add.delay(10,20)
    print("Result: ", ans)  # ans will hold id of process, after 19 second result will be printed on terminal
    return render(request, "myapp/home.html")

def about(request):
    print("Result: ")
    return render(request, "myapp/about.html")

def contact(request):
    print("Result: ")
    return render(request, "myapp/contact.html")