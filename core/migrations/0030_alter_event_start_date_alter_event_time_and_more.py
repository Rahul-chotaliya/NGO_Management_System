# Generated by Django 4.2.3 on 2023-07-25 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_event_start_date_alter_event_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 25, 10, 53, 24, 199280)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 10, 53, 24, 199280)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 25, 10, 53, 24, 198299), null=True),
        ),
    ]
