# Generated by Django 3.0.8 on 2020-07-27 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_remove_meeting_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetings.Room'),
            preserve_default=False,
        ),
    ]
