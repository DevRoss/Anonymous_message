from .models import Message
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import CreateRoomSerializer, EnterRoomSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status
from utils.exception_handler import add_error_code_zero


class CreateRoom(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateRoomSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(add_error_code_zero(serializer.data), status=status.HTTP_201_CREATED, headers=headers)


class EnterRoom(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EnterRoomSerializer

    def get(self, request, label, *args, **kwargs):
        if not label:
            raise ParseError('Not label is found.')
        self.queryset = Message.objects.filter(room=label)
        return self.list(request, *args, **kwargs)
