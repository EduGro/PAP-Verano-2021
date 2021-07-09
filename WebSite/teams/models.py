from django.db import models

from tournament.models import Tournaments

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_image = models.URLField(max_length=200)

    def __str__(self):
        return self.team_name + ', Imagen: ' + self.team_image

class Position(models.Model):
    position_name = models.CharField(max_length=200)

    def __str__(self):
        return self.position_name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=200)
    player_image = models.URLField(max_length=200)

    def __str__(self):
        return 'Nombre: ' + self.player_name + ', Imagen: ' + self.player_image + ', Posición: ' + str(self.position) + ', Equipo: ' + str(self.team)

class NFT(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)
    contract_address = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)

    def __str__(self):
        return 'Nombre: ' + self.title + " Equipo: " + self.team.team_name + " Torneo: " + self.tournament.tournament_name

class Teams_Tournaments(models.Model):
    foreignKeyTeam = models.ForeignKey(Team, on_delete=models.CASCADE)
    foreignKeyTournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    register_day = models.DateTimeField('register date')
    
    def __str__(self):
        return "Equipo: " + self.team.team_name + " Torneo: " + self.tournament.tournament_name
