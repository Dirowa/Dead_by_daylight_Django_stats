# Generated by Django 4.2.1 on 2023-05-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbd_stats', '0004_game_player_1_game_player_2_game_player_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='overall_play_style',
            field=models.CharField(choices=[('normal', 'normal'), ('meme', 'meme'), ('Sweat', 'sweat'), ('Challanges', 'challanges')], default='normal', max_length=10),
        ),
    ]