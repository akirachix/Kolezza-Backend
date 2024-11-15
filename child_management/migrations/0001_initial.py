# Generated by Django 5.1 on 2024-09-13 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("child_module", "0001_initial"),
        ("level_of_stuttering", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Child_Management",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=28)),
                ("last_name", models.CharField(max_length=28)),
                ("middle_name", models.CharField(max_length=28)),
                ("gender", models.CharField(max_length=28)),
                ("date_of_birth", models.DateField()),
                ("is_deleted", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "childmodule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_progress",
                        to="child_module.childmodule",
                    ),
                ),
                (
                    "level_of_stuttering_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="child_management_level",
                        to="level_of_stuttering.levelofstuttering",
                    ),
                ),
            ],
        ),
    ]
