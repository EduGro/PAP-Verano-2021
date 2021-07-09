import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Tournaments(models.Model):
    tournament_name = models.CharField(max_length=200)
    tournament_city = models.CharField(max_length=100)
    tournament_start_date = models.DateTimeField('start date')
    tournament_end_date = models.DateTimeField('end date')

    def __str__(self):
        return "Nombre: " + self.tournament_name + ", Ciudad: " + self.tournament_city + ", Fecha de inicio: " + self.tournament_start_date.strftime("%d %B %Y") + ", Duaración: " + self.duration + " días"

    def next_tournaments(self):
        return self.tournament_start_date >= timezone.now()

    @property
    def is_in_progress(self):
        return (self.tournament_end_date >= timezone.now() and self.tournament_start_date <= timezone.now())

    @property
    def duration(self):
        return str((self.tournament_end_date - self.tournament_start_date).days)
