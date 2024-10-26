# Generated by Django 4.2 on 2024-10-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("speech_therapist", "0004_speech_therapist_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="speech_therapist",
            name="profile_picture",
        ),
        migrations.AddField(
            model_name="speech_therapist",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="speech_therapist",
            name="first_name",
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name="speech_therapist",
            name="last_name",
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]