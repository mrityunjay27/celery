from django.shortcuts import render

# Create your views here.

def index(request):
    print("Result: ")
    return render(request, "myapp/home.html")

def about(request):
    print("Result: ")
    return render(request, "myapp/about.html")

def contact(request):
    print("Result: ")
    return render(request, "myapp/contact.html")