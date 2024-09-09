# Generated by Django 5.1.1 on 2024-09-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech_therapist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speech_therapist',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='speech_therapist',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
