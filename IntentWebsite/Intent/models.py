from django.db import models

# Create your models here.


class Goal(models.Model):
    priority_choices = models.TextChoices("Goal Type", ["High", "Medium", "Low"])

    goaltitle = models.CharField(max_length=1024)
    is_public = models.BooleanField()
    priority = models.CharField(max_length=64, choices = priority_choices.choices, default=priority_choices.Medium)
    description = models.TextField()

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete = models.CASCADE)
    task = models.CharField(max_length=1024)
    is_done = models.BooleanField()
