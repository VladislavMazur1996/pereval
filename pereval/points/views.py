from rest_framework import generics
from .serializers import *
from .models import *


class PassageCreateView(generics.CreateAPIView):
    serializer_class = PassageDetailSerializer


class PassageListView(generics.ListAPIView):
    serializer_class = PassageDetailSerializer
    queryset = Passage.objects.all()


class PassageDetailView(generics.RetrieveAPIView):
    serializer_class = PassageDetailSerializer
    queryset = Passage.objects.all()


class CoordsCreateView(generics.CreateAPIView):
    serializer_class = CoordsDetailSerializer


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UsersDetailSerializer


class PhotoCreateView(generics.CreateAPIView):
    serializer_class = PhotoDetailSerializer

