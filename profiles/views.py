from rest_framework import generics, filters
from django.db.models import Count
# from django_filters.rest_framework import DjangoFilterBackend

from gid_API.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer



class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        assigned_tasks=Count('assignee')
    ).order_by('-assigned_tasks')


class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()