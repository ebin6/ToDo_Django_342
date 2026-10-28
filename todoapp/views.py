from django.shortcuts import render

# Create your views here.

def home(request):
    name="Ebin"
    todos=["Complete LMS task","Attend soft skill session",
           "Learn React","Update LinkedIn Profile"]
    return render(request,"index.html",{"user_name":name,"my_task":todos})

def aboutUs(request):
    return render(request,"about-us.html")

def userLogin(request):
    return render(request,"login.html")

def userRegister(request):
    return render(request,"register.html")