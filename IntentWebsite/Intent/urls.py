from django.urls import path
from . import views

app_name = "Intent"

urlpatterns = [
    path("front/", views.front, name="front"),
    # path("register/", views.register , name ="register"),
    # path("signin/", views.signin , name ="signin"),
    path("home/", views.home, name="home"),
    path("profile/",views.profile,name = "profile"),
    # path("edit_profile/",views.edit_profile ,name = "edit_profile"),
    path("add_goal/",views.add_goal,name = "add_goal"),
    path("tasks/<goal_id>",views.tasks,name = "tasks"),
    path("add_task/<goal_id>/",views.add_task,name = "add_task"),
    path("search/",views.search,name = "search"),
    path("viewgoal/<goal_id>/",views.viewgoal,name="viewgoal"),
    path("add_comment/<goal_id>/", views.add_comment, name="add_comment"),
    path("404/",views.not_found,name="not_found"),
    path("test/",views.test,name="test"),
]
