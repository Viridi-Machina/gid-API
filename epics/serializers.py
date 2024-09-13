from rest_framework import serializers

from .models import Epic, Task, STATUS_CHOICES, PRIORITY_CHOICES

# Epic Serializer ---------------------------------------------------|
class EpicSerializer(serializers.ModelSerializer):
    """
    Serializer for Epic list and detail views.
    """
    created_by = serializers.ReadOnlyField(
        source='created_by.username'
        )
    is_creator = serializers.SerializerMethodField()
    verbose_status = serializers.ChoiceField(
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
    is_completed = serializers.SerializerMethodField()

    # Method to return true if all tasks within an epic are complete
    def get_is_completed(self, obj):
        tasks = obj.tasks.all()
        status = False
        status_list = []
        for task in tasks:
            if task.status != 'COMP':
                break
            else:
                status_list.append(task.status)
            if len(status_list) == len(tasks):
                status = True
        return status


    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.created_by

    # Method to find names of assigned and unique users to given tasks
    def get_assignees(self, obj):
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
            'id', 'title', 'image', 'created_by', 'is_creator',
            'status', 'verbose_status', 'created_at', 'updated_at',
            'assigned_users', 'assignees','assigned_tasks',
            'tasks', 'is_completed'
        ]

# Task Serializer ---------------------------------------------------|
class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task list and detail views.
    """
    epic_title = serializers.ReadOnlyField(
        source='epic.title'
        )
    created_by = serializers.ReadOnlyField(
        source='created_by.username'
        )
    is_creator = serializers.SerializerMethodField()
    assignee = serializers.ReadOnlyField(
        source='assigned_to.name'
        )
    verbose_status = serializers.ChoiceField(
        STATUS_CHOICES, source='get_status_display',
        read_only=True
        )
    verbose_priority = serializers.ChoiceField(
        PRIORITY_CHOICES, source='get_priority_display',
        read_only=True
        )
    created_at = serializers.DateTimeField(
        format='%d/%m/%y', read_only=True
        )
    updated_at = serializers.DateTimeField(
        format='%d/%m/%y at %H:%M', read_only=True
        )
    completion_date = serializers.DateField(
        format='%d/%m/%y'
        )

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.created_by

    class Meta:
        model = Task
        fields = [
            'id', 'epic', 'epic_title', 'title', 'description',
            'assignee', 'assigned_to', 'created_by', 'is_creator',
            'status', 'verbose_status', 'priority', 'verbose_priority',
            'created_at', 'updated_at', 'completion_date'
        ]
