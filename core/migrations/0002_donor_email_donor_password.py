# Generated by Django 4.2.3 on 2023-07-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
