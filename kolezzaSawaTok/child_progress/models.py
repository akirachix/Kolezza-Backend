from django.db import models

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
    def __str__(self):
        return f"Progress for Module: {self.started_module_at} - Stuttering Level: {self.finished_module_at}"