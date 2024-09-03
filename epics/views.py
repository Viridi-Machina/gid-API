from rest_framework import generics, permissions
from django.db.models import Count

from .models import Epic
from .serializers import EpicSerializer

# Epic views --------------------------------------------------------
class EpicList(generics.ListCreateAPIView):
    """
    List Epics and create new Epic if logged in
    """
    serializer_class = EpicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Epic.objects.annotate(
        assigned_users=Count('tasks__assigned_to', distinct=True),
        assigned_tasks=Count('tasks')
    ).order_by('-assigned_tasks')


class EpicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update/delete an Epic if you're the owner.
    """
    serializer_class = EpicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Epic.objects.annotate(
        assigned_users=Count('tasks__assigned_to', distinct=True),
        assigned_tasks=Count('tasks')
    )


# Task views --------------------------------------------------------