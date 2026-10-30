from django.shortcuts import render
from todoapp.models import Tasks

# Create your views here.

def home(request):
    name="Ebin"
    todos=Tasks.objects.all()
    return render(request,"index.html",{"user_name":name,"my_task":todos})

def aboutUs(request):
    return render(request,"about-us.html")

def addTask(request):
    return render(request,"add-task.html")

def userLogin(request):
    return render(request,"login.html")

def userRegister(request):
    return render(request,"register.html")