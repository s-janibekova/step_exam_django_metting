# Generated by Django 3.0.8 on 2020-07-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='room',
        ),
    ]
