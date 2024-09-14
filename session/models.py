from django.db import models
from child_progress.models import ChildProgress  # Ensure this is the correct import
from datetime import datetime, date, time, timedelta

class Session(models.Model):
    child_progress = models.ForeignKey(ChildProgress, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_start_time = models.TimeField()
    session_end_time = models.TimeField()
    duration = models.DurationField(editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.session_start_time and self.session_end_time:
            duration = datetime.combine(date.min, self.session_end_time) - datetime.combine(date.min, self.session_start_time)
            if duration < timedelta():
                duration += timedelta(days=1)
            self.duration = duration
        else:
            self.duration = timedelta()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Session on {self.session_date} from {self.session_start_time} to {self.session_end_time}"
