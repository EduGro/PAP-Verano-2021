# Generated by Django 3.2.4 on 2021-07-11 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_delete_teams_tournaments'),
        ('teams', '0005_auto_20210709_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams_tournaments',
            name='foreignKeyTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournamentTeam', related_query_name='tournamentTeam', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='teams_tournaments',
            name='foreignKeyTournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournamentTournament', related_query_name='tournamentTournament', to='tournament.tournaments'),
        ),
    ]
