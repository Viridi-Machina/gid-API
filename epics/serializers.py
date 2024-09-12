from rest_framework import serializers

from .models import Epic, Task, Profile, STATUS_CHOICES, PRIORITY_CHOICES
from profiles.serializers import ProfileSerializer

class AssigneeSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    class Meta:
        model = Task
        fields = ['assigned_to']

# Epic Serializer ---------------------------------------------------|
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
    assignees = serializers.SerializerMethodField()
    assigned_tasks = serializers.ReadOnlyField()
    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    
    # Method to find names of assigned and unique users to given tasks
    def get_assignees(self,obj):
        tasks = obj.tasks.all()
        assignees = []
        for task in tasks:
            if task.assigned_to:
                if task.assigned_to.name not in assignees:
                    assignees.append(task.assigned_to.name)
        return assignees

    class Meta:
        model = Epic
        fields = [
            'id', 'title', 'image', 'created_by',
            'status', 'created_at', 'updated_at',
            'assigned_users', 'assignees',
            'assigned_tasks', 'tasks'
        ]

# Task Serializer ---------------------------------------------------|
class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task
    """
    created_by = serializers.ReadOnlyField(
        source='created_by.username'
        )
    assigned_to = serializers.ReadOnlyField(
        source='assigned_to.name'
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
