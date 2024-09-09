# Generated by Django 5.1 on 2024-09-09 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_progress', '0002_childprogress_current_module_id_and_more'),
        ('level_of_stuttering', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childprogress',
            name='current_module_id',
        ),
        migrations.RemoveField(
            model_name='childprogress',
            name='level_of_stuttering_id',
        ),
        migrations.AddField(
            model_name='childprogress',
            name='current_level_of_stuttering_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='level_of_stuttering', to='level_of_stuttering.levelofstuttering'),
            preserve_default=False,
        ),
    ]
