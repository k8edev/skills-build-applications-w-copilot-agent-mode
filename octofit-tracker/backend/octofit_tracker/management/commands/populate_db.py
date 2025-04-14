import json
from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        with open('octofit_tracker/test_data.json') as f:
            data = json.load(f)

        # Populate users
        for user_data in data['users']:
            User.objects.get_or_create(email=user_data['email'], defaults=user_data)

        # Populate teams
        for team_data in data['teams']:
            Team.objects.get_or_create(name=team_data['name'], defaults=team_data)

        # Populate activities
        for activity_data in data['activities']:
            Activity.objects.get_or_create(user_id=activity_data['user'], defaults=activity_data)

        # Populate leaderboard
        for leaderboard_data in data['leaderboard']:
            Leaderboard.objects.get_or_create(team=leaderboard_data['team'], defaults=leaderboard_data)

        # Populate workouts
        for workout_data in data['workouts']:
            Workout.objects.get_or_create(name=workout_data['name'], defaults=workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
