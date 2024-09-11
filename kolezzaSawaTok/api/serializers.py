from rest_framework import serializers
from child_progress.models import ChildProgress
from child_management.models import Child_Management
from speech_therapist.models import Speech_Therapist
from child_module.models import ChildModule
from users.models import User  # Import your custom User model
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering
from session.models import Session
# Other serializers for related models
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define model-specific settings for the serializer'''
        model = Session
        '''Specifies the model to serialize'''
        fields = "__all__"
        '''Include all fields from the Session model in the serialization'''
class ChildProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProgress
        fields = "__all__"
class SpeechTherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech_Therapist
        fields = "__all__"
class ChildManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Management
        fields = "__all__"
class ChildModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildModule
        fields = "__all__"
class LevelOfStutteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelOfStuttering
        fields = "__all__"
    def validate_duration(self, value):
        if value.total_seconds() <= 0:
            raise serializers.ValidationError("Duration must be a positive value.")
        return value
class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'
    def validate_phone_number(self, value):
        if self.instance:
            if Guardian.objects.exclude(id=self.instance.id).filter(phone_number=value).exists():
                raise serializers.ValidationError("This phone number is already in use.")
        else:
            if Guardian.objects.filter(phone_number=value).exists():
                raise serializers.ValidationError("This phone number is already in use.")
        return value
    def validate(self, attrs):
        if attrs.get('first_name', '').strip() == "" or attrs.get('last_name', '').strip() == "":
            raise serializers.ValidationError("First name and last name cannot be empty.")
        return attrs
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
            "role"
        ]
    def create(self, validated_data):
        """
        Override create method to hash the password before saving.
        """
        password = validated_data.pop('password')  
        user = User(**validated_data)  
        user.set_password(password)  
        user.save() 
        return user
    def update(self, instance, validated_data):
        """
        Override update method to ensure the password is hashed on update as well.
        """
        password = validated_data.pop('password', None)  
        if password:
            instance.set_password(password) 
        return super().update(instance, validated_data) 
