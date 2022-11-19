from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpRequest
from .models import Goal ,Task ,Comment, Profile ,User
#import random

# Create your views here.

def front(request:HttpResponse):
    return render(request,"Intent/front.html")

# def register(request:HttpResponse):
#     return render(request,"Intent/register.html")

# def signin(request:HttpResponse):
#     return render(request,"Intent/signin.html")

def home(request:HttpResponse):
    goals = Goal.objects.all()
    # random_goal = random.choice(goals)
    # return render(request,"Intent/home.html", {"goals":goals, "random_goal":random_goal})
    return render(request,"Intent/home.html", {"goals":goals})
# ,user_id:int
def profile(request:HttpResponse):
    # user = User.objects.get(id=user_id)
    goals = Goal.objects.all()
    #  if request.method == "POST":
    #     goal = Goal(goaltitle =request.POST["goaltitle"], is_public = request.POST["is_public"], priority=request.POST["priority"], description = request.POST["description"])
    #     goal.save()
    #     return redirect("Intent:add_task",goal.id)
        # new_task = Task(goal=new_goal,task = request.POST["task"],is_done = False)
        # new_task.save(),"user":user
    return render(request,"Intent/profile.html", {"goals":goals})
    # return render(request,"Intent/profile.html", {"Goal":Goal })

def add_goal(request : HttpResponse):
    if request.method == "POST":
        goal = Goal(goaltitle =request.POST["goaltitle"], is_public = request.POST["is_public"], priority=request.POST["priority"], description = request.POST["description"])
        goal.save()
        return redirect("Intent:tasks",goal.id)

    return render(request ,"Intent/add_goal.html", {"Goal":Goal })

def add_task(request : HttpResponse, goal_id:int ):
    goal = Goal.objects.get(id=goal_id)

    if request.method == "POST":
        new_task = Task(goal=goal,task = request.POST["task"],is_done = False)
        new_task.save() 
        # return redirect("Intent:profile")
    return redirect( "Intent:tasks",goal.id)


def tasks(request:HttpRequest, goal_id:int):
    try:
        goal = Goal.objects.get(id=goal_id)
        tasks = Task.objects.filter(goal = goal)
    except:
        return render(request , "Intent/profile.html")
    
    if request.method == "POST":
        return redirect("Intent:profile")

    return render(request,"Intent/tasks.html",{"goal":goal , "tasks":tasks})

def viewgoal(request:HttpRequest, goal_id:int):
    try:
        goal = Goal.objects.get(id=goal_id)
        tasks = Task.objects.filter(goal = goal)
        comments = Comment.objects.filter(goal = goal)
    except:
        return render(request , "Intent/not_found.html")
    return render(request, "Intent/viewgoal.html", {"goal" : goal,"tasks":tasks, "comments" : comments})

def add_comment(request: HttpRequest,goal_id:int):
    goal = Goal.objects.get(id=goal_id)

    if request.method == "POST":
        new_comment = Comment(user = request.user, goal=goal, content=request.POST["content"])
        new_comment.save()

    
    return redirect("Intent:viewgoal", goal_id)

def search(request:HttpResponse):
    return render(request,"Intent/search.html")

def not_found(request:HttpResponse):
    return render(request,"Intent/not_found.html")

def test(request:HttpResponse):
    return render(request,"Intent/test.html")
# ,user_id:int
def edit_profile(request: HttpRequest):
    # user = User.objects.get(id=user_id)
    if request.method == "POST":
        profile = Profile(user = request.user , profile_img=request.FILES["profile_img"],back_img=request.FILES["back_img"], about = request.POST["about"])
        profile.save()
        return redirect("Intent:profile",{"profile":profile})
    return render(request, "Intent/edit_profile.html")
