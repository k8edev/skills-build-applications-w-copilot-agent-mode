import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        with open('octofit_tracker/test_data.json') as f:
            data = json.load(f)

        # Populate Users
        for user_data in data['users']:
            User.objects.create(**user_data)

        # Populate Teams
        for team_data in data['teams']:
            Team.objects.create(**team_data)

        # Populate Activities
        for activity_data in data['activities']:
            Activity.objects.create(**activity_data)

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            Leaderboard.objects.create(**leaderboard_data)

        # Populate Workouts
        for workout_data in data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
