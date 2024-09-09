from django.db import models

from level_of_stuttering.models import LevelOfStuttering

# Create your models here.
# Create your models here.
class ChildProgress(models.Model):
    """class ChildProgress:
   Represents a child's progress in a module,
   tracking their stuttering level and module dates.
   Unique identifier for each record.
   Links to the child's current stuttering level.
   Links to the module the child is currently enrolled in.
   Date the child started the modulemodule.
   Date the child finished the module.
   Returns a string representation showing the module and stuttering level.
   """
    id = models.AutoField(primary_key=True)
    started_module_at = models.DateField()
    finished_module_at = models.DateField()
    current_level_of_stuttering_id = models.ForeignKey(LevelOfStuttering, on_delete=models.CASCADE, related_name='level_of_stuttering')

    def __str__(self):
        return f"Progress for Module: {self.started_module_at} - Stuttering Level: {self.finished_module_at}"