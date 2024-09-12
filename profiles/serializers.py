from rest_framework import serializers
from .models import Profile
from epics.models import Task


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for profile list view
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(
        format='%d/%m/%y', read_only=True
        )
    updated_at = serializers.DateTimeField(
        format='%d/%m/%y at %H:%M', read_only=True
        )
    pending_tasks = serializers.SerializerMethodField()

    # Method to get total assigned tasks with status not 'Completed'
    def get_pending_tasks(self, obj):
        tasks = Task.objects.all()
        profile = obj.name
        pending_tasks = [task.assigned_to.name for task in tasks 
                         if task.assigned_to.name == profile
                         if task.status != 'COMP']
        total = pending_tasks.count(profile)
        return total

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'title', 'image', 'is_owner', 'pending_tasks'
        ]