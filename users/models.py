from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

import users

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        print("Extra fields received:", extra_fields)  

        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
       extra_fields.setdefault("is_staff", True)
       extra_fields.setdefault("is_superuser", True)
       extra_fields.setdefault("role", "superadmin")
    
       user = self.create_user(email, username, password, **extra_fields)

       if user:
         print("User created:", user.first_name, user.last_name)  
       else:
        print("User creation failed.") 

       return user



class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("speech_therapist", "Speech Therapist"),
        ("superadmin", "Super Admin"),
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, unique=True)
    first_name = models.CharField(max_length=16, blank=True, null=True)
    last_name = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_speech_therapist = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]  
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        if self.role == "speech_therapist":
            self.is_speech_therapist = True
            self.is_superuser = False
        elif self.role == "superadmin":
            self.is_superuser = True
            self.is_speech_therapist = False
        else:
            self.is_speech_therapist = False
            self.is_superuser = False
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        permissions = [
            ("can_add_user", "Can add user"),  
        ]

