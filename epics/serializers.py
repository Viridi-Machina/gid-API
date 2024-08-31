from rest_framework import serializers
from .models import Epic


class EpicSerializer(serializers.ModelSerializer):


    class Meta:
        model = Epic
        fields = [
            'id', 'title', 'image', 'profile_list', 'task_list', 'created_by'
            'status', 'created_at', 'updated_at'
        ]