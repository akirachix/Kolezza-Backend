from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

"""This model is for the speech therapist. It represents the data stored in
   our database.
   Save changes to the database
  Name of the hospital associated with the therapist
  Boolean to indicate whether the record is soft deleted or not
  Timestamp for when the therapist record was soft-deleted, if applicable
  Soft delete method to mark a record as deleted without
  actually removing it from the database
  Set is_deleted to True to indicate that the record is soft deleted
  """

class Speech_Therapist(models.Model):
    id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=28)
    profile_picture= models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number=models.CharField(max_length = 15)
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Optional field to track deletion time

    def clean(self):
        """Custom validation for the Speech_Therapist model."""
        if not self.hospital_name:
            raise ValidationError("Hospital name cannot be empty.")

    def soft_delete(self):
        """Soft delete the therapist record by marking it as deleted."""
        self.is_deleted = True  # Mark as deleted
        self.deleted_at = timezone.now()  # Set deletion timestamp
        self.updated_at = timezone.now()  # Update the timestamp
        self.save()

    def __str__(self):
        return f"{self.hospital_name} - {'Deleted' if self.is_deleted else 'Active'}"
