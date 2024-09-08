from rest_framework import serializers
from session.models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        '''Meta class to define model-specific settings for the serializer'''
        model = Session
        '''Specifies the model to serialize'''
        fields = "__all__"
        '''Include all fields from the Session model in the serialization'''