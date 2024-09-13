from django.db import models


class GuardianManager(models.Manager):
    def get_queryset(self):
        # Only return active guardians by default
        return super().get_queryset().filter(is_active=True)

    def all_with_deleted(self):
        # Return all guardians, including soft-deleted ones
        return super().get_queryset()


class Guardian(models.Model):
    """
    Represents a guardian responsible for a child.
    Guardians can be soft-deleted by marking them as inactive.
    A unique identifier for each guardian
    The guardian's first name
    The guardian's second name (middle name or any other second name)
    The guardian's last name
    The guardian's phone number, which must be unique
    The guardian's residential address
    A boolean flag indicating whether the guardian is active (soft deletion)

    """

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    # Use the custom manager
    objects = GuardianManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def soft_delete(self):
        self.is_active = False
        self.save_guardian()

    def save_guardian(self):
        self.save()
