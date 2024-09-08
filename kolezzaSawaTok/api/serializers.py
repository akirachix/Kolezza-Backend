from rest_framework import serializers
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering

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
 