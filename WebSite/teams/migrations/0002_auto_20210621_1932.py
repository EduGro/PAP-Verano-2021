# Generated by Django 3.2.4 on 2021-06-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='team_text',
            new_name='team_name',
        ),
        migrations.AddField(
            model_name='player',
            name='player_image',
            field=models.URLField(default='https://i.imgur.com/6Uurv10.png'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='team_image',
            field=models.URLField(default='https://i.imgur.com/DnRjHZD.png'),
            preserve_default=False,
        ),
    ]