from .models import Room
from rest_framework.generics import CreateAPIView, ListAPIView


class CreateRoom(CreateAPIView):
    pass


class EnterRoom(ListAPIView):
    pass
