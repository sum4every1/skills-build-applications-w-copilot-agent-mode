from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team = octo_models.Team
        Activity = octo_models.Activity
        Leaderboard = octo_models.Leaderboard
        Workout = octo_models.Workout
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@stark.com', password='password', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@rogers.com', password='password', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@wayne.com', password='password', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@kent.com', password='password', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning run', suggested_for_team=marvel)
        Workout.objects.create(name='Strength Training', description='Heavy lifting', suggested_for_team=dc)

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=110)
        Leaderboard.objects.create(user=clark, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
