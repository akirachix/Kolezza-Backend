from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'is_superuser', 'is_speech_therapist']

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
