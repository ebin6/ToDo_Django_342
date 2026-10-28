from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def aboutUs(request):
    return render(request,"about-us.html")

def userLogin(request):
    return render(request,"login.html")

def userRegister(request):
    return render(request,"register.html")