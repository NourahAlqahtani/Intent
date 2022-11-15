from django.urls import path
from . import views

app_name = "Intent"

urlpatterns = [
    path("front/", views.front, name="front"),
    path("register/", views.register , name ="register"),
    path("signin/", views.signin , name ="signin"),
    path("home/", views.home, name="home"),
    path("profile/",views.profile,name = "profile"),
    path("goal/",views.add_goal,name = "add_goal"),
    path("goal/<goal_id>",views.goal,name = "goal"),
    path("task/<goal_id>/",views.add_task,name = "add_task"),
    path("search/",views.search,name = "search"),
]
