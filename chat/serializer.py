from rest_framework import serializers
from .models import Room, Message


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class EnterRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
