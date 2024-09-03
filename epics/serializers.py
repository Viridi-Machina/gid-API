from rest_framework import serializers
from .models import Epic, STATUS_CHOICES


class EpicSerializer(serializers.ModelSerializer):
    """
    Serializer for Epic list view
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    status = serializers.ChoiceField(STATUS_CHOICES, source='get_status_display')
    created_at = serializers.DateTimeField(format='%d/%m/%y', read_only=True)
    updated_at = serializers.DateTimeField(format='%d/%m/%y at %H:%M', read_only=True)

    class Meta:
        model = Epic
        fields = [
            'id', 'title', 'image', 'created_by',
            'status', 'created_at', 'updated_at'
        ]
