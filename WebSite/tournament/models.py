import datetime

from django.db import models
from django.utils import timezone
from teams.models import Team

# Create your models here.
class Tournaments(models.Model):
    tournament_name = models.CharField(max_length=200)
    tournament_city = models.CharField(max_length=100)
    tournament_start_date = models.DateTimeField('start date')
    tournament_end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.tournament_name + ", Duration: " + duration()

    def next_tournaments(self):
        return self.tournament_start_date >= timezone.now()

    @property
    def is_in_progress(self):
        return (self.tournament_end_date >= timezone.now() and self.tournament_start_date <= timezone.now())

    def duration(self):
        return str((self.tournament_end_date - self.tournament_end_date).days)

class Teams_Tournaments(models.Model):
    foreignKeyTeam = models.ForeignKey(Team, on_delete=models.CASCADE)
    foreignKeyTournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    register_day = models.DateTimeField('register date')
