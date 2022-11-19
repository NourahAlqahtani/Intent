from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority_choices = models.TextChoices("Goal Type", ["High", "Medium", "Low"])

    goaltitle = models.CharField(max_length=1024)
    is_public = models.BooleanField()
    priority = models.CharField(max_length=64, choices = priority_choices.choices, default=priority_choices.Medium)
    description = models.TextField()
    time_start = models.DateTimeField(auto_now=True)
    time_end = models.DateTimeField(auto_now=True)

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete = models.CASCADE)
    task = models.CharField(max_length=1024)
    is_done = models.BooleanField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="images/")
    back_img = models.ImageField(upload_to="images/")
    about = models.CharField(max_length=1024)


