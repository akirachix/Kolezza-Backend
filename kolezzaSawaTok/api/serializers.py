from rest_framework import serializers
from child_module.models import ChildModule

'''
Serializer for the ChildModule model
This serialize converts ChildModule model instances into JSON format
andvalidates incoming JSON data before saving it to the database
'''
class ChildModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildModule
        fields = '__all__'