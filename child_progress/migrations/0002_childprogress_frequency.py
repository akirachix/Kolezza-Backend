# Generated by Django 4.2 on 2024-09-21 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("child_progress", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="childprogress",
            name="frequency",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
