# Generated by Django 4.2 on 2024-10-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=16, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=16, null=True)),
                ("last_name", models.CharField(blank=True, max_length=16, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("speech_therapist", "Speech Therapist"),
                            ("superadmin", "Super Admin"),
                        ],
                        max_length=20,
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_speech_therapist", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "permissions": [("can_add_user", "Can add user")],
            },
        ),
    ]
