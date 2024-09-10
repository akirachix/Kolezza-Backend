from django.db import models
from datetime import datetime, timedelta

from child_progress.models import ChildProgress

class Session(models.Model):
    
    """Represents a speech session for children using the device
    Compute duration based on start and end times
    Create datetime objects for start and end times
    Calculate duration
    Set duration to zero if end time is before start time
    Save session data to the database"""
    id = models.AutoField(primary_key=True)
    session_date = models.DateField()
    session_start_time = models.TimeField()
    session_end_time = models.TimeField()
    duration = models.DurationField(null=True, blank=True)
    child_progress = models.ForeignKey(ChildProgress, on_delete=models.CASCADE, related_name='sessions')

    def __str__(self):
        return f"Session from {self.session_start_time} to {self.session_end_time}"
    
    def save(self, *args, **kwargs):
        if self.session_start_time and self.session_end_time:
            start_datetime = datetime.combine(self.session_date, self.session_start_time)
            end_datetime = datetime.combine(self.session_date, self.session_end_time)
            if end_datetime > start_datetime:
                self.duration = end_datetime - start_datetime
            else:
                self.duration = timedelta()
        super().save(*args, **kwargs)
