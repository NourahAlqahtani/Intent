from django.urls import path
from . import views

app_name = "Intent"

urlpatterns = [
    path("front/", views.front, name="front"),
    path("register/", views.register , name ="register"),
    path("signin/", views.signin , name ="signin"),
    path("home/", views.home, name="home"),
    path("profile/",views.profile,name = "profile"),
    path("search/",views.profile,name = "profile"),
]
