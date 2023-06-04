from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .serializers import *
from .models import *


class PassageCreateView(generics.CreateAPIView):
    serializer_class = PassageDetailSerializer


class PassageDetailView(generics.RetrieveAPIView):
    serializer_class = PassageDetailSerializer
    queryset = Passage.objects.all()


class PassageUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PassageDetailSerializer
    queryset = Passage.objects.all()

    def patch(self, request, *args, **kwargs):
        response_data = {"state": 0}
        if self.get_object().status == 'NE':
            self.partial_update(request, *args, **kwargs)
            response_data['state'] = 1
        else:
            raise ValidationError("Status is not new")
        return Response(response_data, status=status.HTTP_200_OK)


class CoordsCreateView(generics.CreateAPIView):
    serializer_class = CoordsDetailSerializer


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UsersDetailSerializer


class PhotoCreateView(generics.CreateAPIView):
    serializer_class = PhotoDetailSerializer


class CoordsUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CoordsDetailSerializer


class PhotoUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PhotoDetailSerializer


class PassageListView(generics.ListAPIView):
    serializer_class = PassageDetailSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        email = self.kwargs['email']
        return Passage.objects.filter(user__email=email)
