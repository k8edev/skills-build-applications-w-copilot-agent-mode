from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team_name = models.CharField(max_length=100)  # Renamed to avoid conflict

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    member_list = models.ManyToManyField(User)  # Renamed to avoid conflict

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
