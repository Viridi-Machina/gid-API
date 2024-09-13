from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from .models import Epic, Task
from .serializers import EpicSerializer, TaskSerializer
from gid_API.permissions import IsCreatorOrReadOnly

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
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'created_by',
        'status'
    ]
    search_fields = [
        'title'
    ]
    ordering_fields = [
        'created_by',       # By creator
        'assigned_users',   # By total assignees
        'assigned_tasks',   # By total tasks
        'created_at',       # By time created
    ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EpicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update/delete an Epic if you're the owner.
    """
    serializer_class = EpicSerializer
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Epic.objects.annotate(
        assigned_users=Count('tasks__assigned_to', distinct=True),
        assigned_tasks=Count('tasks')
    )


# Task views --------------------------------------------------------|
class TaskList(generics.ListCreateAPIView):
    """
    List Tasks and create new task if logged in
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'epic',
        'created_by',
        'status',
        'priority'
    ]
    search_fields = [
        'title'
    ]
    ordering_fields = [
        'created_by',       # By creator
        'assigned_to',      # By assignee
        'created_at',       # By time created
        'priority',         # By task priority
        'updated_at'        # By recent activity
    ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List Tasks and create new task if logged in
    """
    serializer_class = TaskSerializer
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Task.objects.all()
