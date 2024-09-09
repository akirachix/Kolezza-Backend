from django.db import models

# Create your models here.
class LevelOfStuttering(models.Model):
    """
    Represents a record of a child's level of stuttering.
    This model captures different types of stuttering, their descriptions, and duration.
    A unique identifier for each level of stuttering record
    A field to describe the type of stuttering (e.g., developmental, acquired)
    A text field providing a detailed description of the stuttering type
    A duration field to record how long the stuttering has been occurring
    """
    id = models.AutoField(primary_key=True)  
    type_of_stuttering = models.CharField(max_length=100)  
    description = models.TextField()  
    duration = models.DurationField()  
    def __str__(self):
        """
        Return a string representation of the LevelOfStuttering, showing the type of stuttering.
        """
        return f"{self.type_of_stuttering}"