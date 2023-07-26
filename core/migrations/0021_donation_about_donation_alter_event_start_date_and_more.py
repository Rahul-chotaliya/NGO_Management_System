# Generated by Django 4.2.3 on 2023-07-24 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_donor_name_alter_event_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='about_donation',
            field=models.TextField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 13, 53, 58, 727609)),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 13, 53, 58, 727609)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 13, 53, 58, 726610)),
        ),
    ]
