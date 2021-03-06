# Generated by Django 3.2.4 on 2021-07-05 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_rename_tournament_tournaments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournaments',
            name='tournament_city',
            field=models.CharField(default='Guadalajara', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournaments',
            name='tournament_end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournaments',
            name='tournament_name',
            field=models.CharField(default='Torneo Generico', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournaments',
            name='tournament_start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='start date'),
            preserve_default=False,
        ),
    ]
