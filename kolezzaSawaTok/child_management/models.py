from django.db import models
from django.utils import timezone

"""This model is meant to be used by the therapist to onboard a 
particular child to the database. 
Auto-incrementing primary key for each child
Child's first name
Child's last name
Stores the child's date of birth
Boolean field to mark soft deletion, default is False
Timestamp for when the record is soft-deleted
Record the current time as the deletion time
Save the changes to the database
Set is_deleted to True to soft delete the record
"""
class Child_Management(models.Model):
    
    id = models.AutoField(primary_key=True)  
    first_name = models.CharField(max_length=28)  
    last_name = models.CharField(max_length=28)    
    date_of_birth = models.DateField()    
    is_active = models.BooleanField(default=True)    
    updated_at = models.DateTimeField(null=True, blank=True)   

    def soft_delete(self):
        self.is_updated = True  
        self.updated_at = timezone.now() 
        self.save()  
        
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
   
