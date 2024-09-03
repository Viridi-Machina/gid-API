from rest_framework import generics, permissions

from .models import Epic
from .serializers import EpicSerializer
from gid_API.permissions import IsOwnerOrReadOnly

class EpicList(generics.ListCreateAPIView):
    """
    List Epics and create new Epic if logged in
    """
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer
    permission_classes = [IsOwnerOrReadOnly]