# Generated by Django 3.2.4 on 2021-07-09 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_delete_teams_tournaments'),
        ('teams', '0002_auto_20210621_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams_Tournaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_day', models.DateTimeField(verbose_name='register date')),
                ('foreignKeyTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
                ('foreignKeyTournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournaments')),
            ],
        ),
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('contract_address', models.CharField(max_length=200)),
                ('token', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournaments')),
            ],
        ),
    ]
