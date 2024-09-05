from rest_framework import serializers

from .models import Epic, Task, Profile, STATUS_CHOICES, PRIORITY_CHOICES
from profiles.serializers import ProfileSerializer

# class AssigneeSerializer


class EpicSerializer(serializers.ModelSerializer):
    """
    Serializer for Epic list and detail views
    """
    created_by = serializers.ReadOnlyField(
        source='created_by.username'
        )
    status = serializers.ChoiceField(
        STATUS_CHOICES, source='get_status_display'
        )
    created_at = serializers.DateTimeField(
        format='%d/%m/%y', read_only=True
        )
    updated_at = serializers.DateTimeField(
        format='%d/%m/%y at %H:%M', read_only=True
        )
    assigned_users = serializers.ReadOnlyField()
    assignee = serializers.ReadOnlyField()
    assigned_tasks = serializers.ReadOnlyField()
    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    
    # def get_assignee(self, obj):
    #     assignee = obj.select_related('assigned_to__name')
    #     return assignee

    class Meta:
        model = Epic
        fields = [
            'id', 'title', 'image', 'created_by',
            'status', 'created_at', 'updated_at',
            'assigned_users', 'assignee',
            'assigned_tasks', 'tasks'
        ]


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task
    """
    created_by = serializers.ReadOnlyField(
        source='created_by.username'
        )
    assigned_to = serializers.ReadOnlyField(
        source='assigned_to.username'
        )
    status = serializers.ChoiceField(
        STATUS_CHOICES, source='get_status_display'
        )
    priority = serializers.ChoiceField(
        PRIORITY_CHOICES, source='get_priority_display'
    )
    created_at = serializers.DateTimeField(
        format='%d/%m/%y', read_only=True
        )
    updated_at = serializers.DateTimeField(
        format='%d/%m/%y at %H:%M', read_only=True
        )
    completion_date = serializers.DateField(
        format='%d/%m/%y', read_only=True
        )
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'assigned_to',
            'created_by', 'status', 'priority', 
            'created_at', 'updated_at', 'completion_date'
        ]
