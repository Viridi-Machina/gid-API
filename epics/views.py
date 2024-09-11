from rest_framework import generics, permissions
from django.db.models import Count

from .models import Epic, Task
from .serializers import EpicSerializer, TaskSerializer

# Epic views --------------------------------------------------------|
class EpicList(generics.ListCreateAPIView):
    """
    List Epics and create new Epic if logged in.
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
        assigned_tasks=Count('tasks'),
        # assignee = Task.objects.select_related('assigned_to')
    )

    
    


# Task views --------------------------------------------------------|
class TaskList(generics.ListCreateAPIView):
    """
    List Tasks and create new task if logged in
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List Tasks and create new task if logged in
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
