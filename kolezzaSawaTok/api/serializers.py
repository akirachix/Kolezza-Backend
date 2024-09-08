from rest_framework import serializers
from child_progress.models import ChildProgress
class ChildProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildProgress
        fields = '__all__'