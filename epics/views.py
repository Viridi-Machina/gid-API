from rest_framework import generics
from django.db.models import Count

from .models import Epic
from .serializers import EpicSerializer
from gid_API.permissions import IsOwnerOrReadOnly

class EpicList(generics.ListCreateAPIView):
    """
    List Epics and create new Epic if logged in
    """
    serializer_class = EpicSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Epic.objects.annotate(
        assigned_users=Count('task__assigned_to', distinct=True),
        assigned_tasks=Count('task', distinct=True)
    )