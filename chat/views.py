from .models import Message
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import CreateRoomSerializer, EnterRoomSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError


class CreateRoom(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateRoomSerializer


class EnterRoom(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EnterRoomSerializer

    def get(self, request, label, *args, **kwargs):
        if not label:
            raise ParseError('Not label is found.')
        self.queryset = Message.objects.filter(room=label)
        return self.list(request, *args, **kwargs)
