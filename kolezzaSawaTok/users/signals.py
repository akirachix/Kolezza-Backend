from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import User


# Define the signal to assign permissions based on user roles:


@receiver(post_save, sender=User)
def assign_user_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            # Add the superuser to the superuser group
            superuser_group, created = Group.objects.get_or_create(name="Superuser")
            instance.groups.add(superuser_group)
            # Assign specific permissions to superuser
            permissions = Permission.objects.all()  #  Superusers get all permissions
            instance.user_permissions.set(permissions)
        else:
            if instance.is_speech_therapist:
                # Assign speech therapist group and permissions
                therapist_group, created = Group.objects.get_or_create(
                    name="Speech Therapist"
                )
                instance.groups.add(therapist_group)
                permissions = Permission.objects.filter(
                    codename__in=[
                        "can_view_patient_info",
                        "can_edit_modules",
                        "can_register_children",
                        "can_view_progress_reports",
                    ]
                )
                instance.user_permissions.set(permissions)
            else:
                pass

        instance.save()
