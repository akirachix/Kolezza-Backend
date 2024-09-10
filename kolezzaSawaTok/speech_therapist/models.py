from django.db import models
from django.utils import timezone

from users.models import User


class Speech_Therapist(models.Model):
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
   id = models.AutoField(primary_key=True)  
   hospital_name = models.CharField(max_length=28) 
   phone_number = models.CharField(max_length=28)
   profile_picture = models.ImageField()
   role = models.CharField(max_length=28)
   is_active = models.BooleanField(default=True)  
   updated_at = models.DateTimeField(null=True, blank=True)
   user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

     
   def soft_delete(self):
     self.updated_at = timezone.now()
     self.save()  
     

   