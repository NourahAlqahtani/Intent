from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def front(request:HttpResponse):
    return render(request,"Intent/front.html")

def register(request:HttpResponse):
    return render(request,"Intent/register.html")

def signin(request:HttpResponse):
    return render(request,"Intent/signin.html")

def home(request:HttpResponse):
    return render(request,"Intent/home.html")

def profile(request:HttpResponse):
    return render(request,"Intent/profile.html")

def search(request:HttpResponse):
    return render(request,"Intent/search.html")