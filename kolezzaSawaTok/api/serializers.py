from rest_framework import serializers
from child_management.models import Child_Management
from speech_therapist.models import Speech_Therapist

from rest_framework import serializers

"""Serializer for the Speech_Therapist model
Specifies the model to be serialized
Includes all fields from the Speech_Therapist model 
"""
class SpeechTherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech_Therapist 
        fields = "__all__" 
         
"""Serializer for the Child_Management model
Specifies the model to be serialized
Includes all fields from the Child_Management model
 """
class ChildManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Management  
        fields = "__all__"  