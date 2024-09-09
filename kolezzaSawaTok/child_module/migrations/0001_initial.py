# Generated by Django 5.1 on 2024-09-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('module_level', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
