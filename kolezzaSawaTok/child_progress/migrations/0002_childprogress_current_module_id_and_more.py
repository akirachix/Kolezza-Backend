# Generated by Django 5.1 on 2024-09-09 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child_module', '0004_rename_level_of_stuttering_id_childmodule_childprogress_level_of_stuttering_id'),
        ('child_progress', '0001_initial'),
        ('level_of_stuttering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='childprogress',
            name='current_module_id',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='child_progress', to='child_module.childmodule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childprogress',
            name='level_of_stuttering_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='child_progress_stuttering', to='level_of_stuttering.levelofstuttering'),
            preserve_default=False,
        ),
    ]
