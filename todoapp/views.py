from django.shortcuts import render,redirect
from todoapp.models import Tasks

# Create your views here.

def home(request):
    name="Ebin"
    todos=Tasks.objects.all()
    return render(request,"index.html",{"user_name":name,"my_task":todos})

def aboutUs(request):
    return render(request,"about-us.html")

def addTask(request):
    if request.method=="POST":
        my_task=request.POST['task']
        Tasks(task=my_task).save()
        return redirect("/")
    return render(request,"add-task.html")

def deleteTask(request,task_id):
    task=Tasks.objects.get(id=task_id)
    task.delete()
    return redirect("/")


def userLogin(request):
    return render(request,"login.html")

def userRegister(request):
    return render(request,"register.html")