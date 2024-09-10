from django.contrib import admin
from .models import ChildModule
from rest_framework import serializers

# Import the ChildModule model to register it with the Django admin site
from .models import ChildModule

# Register the ChildModule model with the Django admin site
admin.site.register(ChildModule)