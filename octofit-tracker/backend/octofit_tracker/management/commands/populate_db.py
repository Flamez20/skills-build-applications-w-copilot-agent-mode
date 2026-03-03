from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data one by one
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Leaderboard.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30)
        Activity.objects.create(user=users[1], type='Cycling', duration=45)
        Activity.objects.create(user=users[2], type='Swimming', duration=60)
        Activity.objects.create(user=users[3], type='Yoga', duration=20)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Marvel')
        Workout.objects.create(name='Squats', description='Lower body strength', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
