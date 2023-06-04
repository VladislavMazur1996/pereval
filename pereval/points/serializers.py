from rest_framework import serializers

from .models import *


class PassageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = '__all__'


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'username',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'phone',
        ]


class CoordsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
