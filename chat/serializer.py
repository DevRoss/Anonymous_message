from rest_framework import serializers
from .models import Room


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

# class s
