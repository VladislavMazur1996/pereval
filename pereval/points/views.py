from rest_framework import generics
from .serializers import PassageDetailSerializer


class PassageCreateView(generics.CreateAPIView):
    serializer_class = PassageDetailSerializer
