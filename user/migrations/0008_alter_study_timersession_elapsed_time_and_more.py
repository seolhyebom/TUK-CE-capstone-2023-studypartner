# Generated by Django 5.0.2 on 2024-04-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_study_timersession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study_timersession',
            name='elapsed_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='study_timersession',
            name='goal_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='study_timersession',
            name='remaining_time',
            field=models.TimeField(),
        ),
    ]
