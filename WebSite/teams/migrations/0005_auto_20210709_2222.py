# Generated by Django 3.2.4 on 2021-07-10 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_delete_teams_tournaments'),
        ('teams', '0004_alter_nft_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamNFT', related_query_name='teamNFT', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='nft',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournamentNFT', related_query_name='tournamentNFT', to='tournament.tournaments'),
        ),
    ]
