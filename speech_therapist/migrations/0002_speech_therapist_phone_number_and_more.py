# Generated by Django 4.2 on 2024-09-19 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("speech_therapist", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="speech_therapist",
            name="phone_number",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="speech_therapist",
            name="profile_picture",
            field=models.ImageField(default=django.utils.timezone.now, upload_to=""),
            preserve_default=False,
        ),
    ]
