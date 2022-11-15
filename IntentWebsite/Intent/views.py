from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpRequest
from .models import Goal ,Task


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
    #  if request.method == "POST":
    #     goal = Goal(goaltitle =request.POST["goaltitle"], is_public = request.POST["is_public"], priority=request.POST["priority"], description = request.POST["description"])
    #     goal.save()
    #     return redirect("Intent:add_task",goal.id)
        # new_task = Task(goal=new_goal,task = request.POST["task"],is_done = False)
        # new_task.save()
    return render(request,"Intent/profile.html")
    # return render(request,"Intent/profile.html", {"Goal":Goal })

def add_goal(request : HttpResponse):
    if request.method == "POST":
        goal = Goal(goaltitle =request.POST["goaltitle"], is_public = request.POST["is_public"], priority=request.POST["priority"], description = request.POST["description"])
        goal.save()
        return redirect("Intent:goal",goal.id)

    return render(request ,"Intent/add_goal.html", {"Goal":Goal })

def add_task(request : HttpResponse, goal_id:int ):
    goal = Goal.objects.get(id=goal_id)

    if request.method == "POST":
        new_task = Task(goal=goal,task = request.POST["task"],is_done = False)
        new_task.save() 
        # return redirect("Intent:profile")
    return redirect( "Intent:goal",goal.id)


def goal(request:HttpRequest, goal_id:int):
    try:
        goal = Goal.objects.get(id=goal_id)
        tasks = Task.objects.filter(goal = goal)
    except:
        return render(request , "Intent/profile.html")
    
    if request.method == "POST":
        return redirect("Intent:profile")

    return render(request,"Intent/goal.html",{"goal":goal , "tasks":tasks})


def search(request:HttpResponse):
    return render(request,"Intent/search.html")