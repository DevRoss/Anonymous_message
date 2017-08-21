from rest_framework import serializers
from .models import Room, Message


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'label')


class EnterRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('room', 'handle', 'message', 'timestamp')
