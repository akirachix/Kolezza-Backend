from rest_framework import serializers
from session.models import Session
from child_progress.models import ChildProgress
from child_management.models import Child_Management
from users.models import User 
from speech_therapist.models import Speech_Therapist
from child_module.models import ChildModule
from guardian.models import Guardian
from level_of_stuttering.models import LevelOfStuttering

# Session Serializer
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

# ChildProgress Serializer
class ChildProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProgress
        fields = "__all__"

# ChildManagement Serializer
class ChildManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Management
        fields = "__all__"

# ChildModule Serializer
class ChildModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildModule
        fields = "__all__"

# LevelOfStuttering Serializer
class LevelOfStutteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelOfStuttering
        fields = "__all__"

    def validate_duration(self, value):
        if value.total_seconds() <= 0:
            raise serializers.ValidationError("Duration must be a positive value.")
        return value

# Guardian Serializer
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

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

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
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user  

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

# SpeechTherapist Serializer
class SpeechTherapistSerializer(serializers.ModelSerializer):
    # Nested UserSerializer to handle user data
    user = UserSerializer()

    class Meta:
        model = Speech_Therapist
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'email',
            'hospital_name',
            'phone_number',
            'is_deleted',
            'updated_at',
            'deleted_at'
        ]

    def create(self, validated_data):
        # Extract user data from validated_data
        user_data = validated_data.pop('user')
        
        # Create or update the User instance
        user, created = User.objects.get_or_create(
            username=user_data.get('username'),
            defaults={
                'first_name': user_data.get('first_name'),
                'last_name': user_data.get('last_name'),
                'email': user_data.get('email'),
                'role': user_data.get('role')
            }
        )

        if created:
            user.set_password(user_data.get('password'))
            user.save()

        # Create the Speech Therapist instance linked to the User
        speech_therapist = Speech_Therapist.objects.create(user=user, **validated_data)
        return speech_therapist

    def update(self, instance, validated_data):
        # Update the User instance
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            user.role = user_data.get('role', user.role)
            user.save()

        # Update the Speech Therapist instance
        return super().update(instance, validated_data)
