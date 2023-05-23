from rest_framework import serializers

from .models import *


class PassageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passage
        fields = '__all__'
