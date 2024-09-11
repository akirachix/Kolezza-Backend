from django.db import models
from level_of_stuttering.models import LevelOfStuttering

"""
the class is for childModule it has the following attributes:
name of the child
description of the module
duration of the module
module level
"""


# Create your models here.
class ChildModule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)  # Increased length from 20 to 50
    description = models.CharField(max_length=50)
    duration = models.DurationField()
    module_level = models.PositiveSmallIntegerField()
    level_of_stuttering_id = models.ForeignKey(
        LevelOfStuttering,
        on_delete=models.CASCADE,
        related_name="assigned_level_of_stuttering",
    )

    def __str__(self):
        return f"{self.module_level}"