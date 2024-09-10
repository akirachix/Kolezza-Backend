from rest_framework import serializers
from child_progress.models import ChildProgress
from child_management.models import Child_Management
from speech_therapist.models import Speech_Therapist
from child_module.models import ChildModule
from users.models import User
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering

class ChildProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProgress
        fields = '__all__'

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
'''
Serializer for the ChildModule model
This serialize converts ChildModule model instances into JSON format
andvalidates incoming JSON data before saving it to the database
'''
class ChildModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildModule
        fields = '__all__'

class LevelOfStutteringSerializer(serializers.ModelSerializer):
    """
    Serializer for LevelOfStuttering model.
    Handles the conversion of LevelOfStuttering instances to JSON and vice versa.
    """
    class Meta:
        model = LevelOfStuttering  
        fields = '__all__' 

    def validate_duration(self, value):
        """
        Validate that the duration field is a positive value.
        """
        if value.total_seconds() <= 0:
            raise serializers.ValidationError("Duration must be a positive value.")  
        return value

class GuardianSerializer(serializers.ModelSerializer):
    """
    Serializer for Guardian model.
    Handles the conversion of Guardian instances to JSON and vice versa.
    """
    class Meta:
        model = Guardian  
        fields = '__all__'  

    def validate_phone_number(self, value):
        """
        Validate that the phone number is unique.
        """
        if Guardian.objects.exclude(id=self.instance.id).filter(phone_number=value).exists():
            raise serializers.ValidationError("This phone number is already in use.")  
        return value

    def validate(self, attrs):
        """
        Additional validation for Guardian fields.
        """
        if 'first_name' in attrs and 'last_name' in attrs:
            if attrs['first_name'].strip() == "" or attrs['last_name'].strip() == "":
                raise serializers.ValidationError("First name and last name cannot be empty.")  # Raise validation error if either is empty
        return attrs

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'is_superuser', 'is_speech_therapist']

class GuardianSerializer(serializers.ModelSerializer):

    def roleValidation(self, data):
        is_superuser = data.get('is_superuser', False)
        is_speech_therapist = data.get('is_speech_therapist', False)

        if is_superuser and is_speech_therapist:
            raise serializers.ValidationError('A user cannot be both a superuser and a speech therapist.')
        
        if not is_superuser and not is_speech_therapist:
            raise serializers.ValidationError('A user must be either a superuser or a speech therapist.')

        return data

    def create(self, validated_data):
        # Handle password hashing here
        user = User(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_superuser=validated_data.get('is_superuser', False),
            is_speech_therapist=validated_data.get('is_speech_therapist', False),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
