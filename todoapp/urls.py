from django.urls import path
from todoapp import views

urlpatterns=[
    path("about-us/",views.aboutUs,name="about_us"),
    path("login/",views.userLogin,name="signin"),
    path("register/",views.userRegister,name="signup"),
    path("",views.home,name="index"),
]