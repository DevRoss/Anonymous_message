from .models import Room
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import CreateRoomSerializer
from rest_framework.permissions import AllowAny


class CreateRoom(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateRoomSerializer


class EnterRoom(ListAPIView):
    pass
