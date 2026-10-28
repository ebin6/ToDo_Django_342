from django.urls import path
from todoapp import views

urlpatterns=[
    path("about-us/",views.aboutUs),
    path("",views.home),
]