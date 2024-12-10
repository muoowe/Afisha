# Generated by Django 5.1.1 on 2024-11-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_movie_duration_alter_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]