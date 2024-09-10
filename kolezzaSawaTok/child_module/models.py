from django.db import models
from level_of_stuttering.models import LevelOfStuttering

'''
the class is for childModule it has the following attributes:
name of the child
description of the module
duration of the module
module level
'''

# Create your models here.
class ChildModule(models.Model):
    id = models.AutoField(primary_key=True)  
    name=models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    duration = models.DurationField()
    module_level=models.PositiveSmallIntegerField()
    level_of_stuttering_id = models.ForeignKey(LevelOfStuttering, on_delete=models.CASCADE, related_name='assigned_level_of_stuttering')

#String representation: The __str__ method defines the string representation of the ChildModule instance. In this case, it returns the duration of the child module.
    def __str__(self):
        return f"{self.module_level}"