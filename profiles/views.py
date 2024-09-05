from rest_framework import generics

from gid_API.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer



class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()