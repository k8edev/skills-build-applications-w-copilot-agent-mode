from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team_name = models.CharField(max_length=100)  # Removed related_name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    member_list = models.JSONField()  # Renamed from 'members' to 'member_list' to avoid clash
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')  # Added related_name here
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
