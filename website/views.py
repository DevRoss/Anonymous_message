# from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
from website.models import Messages
from website.serializer import (GetMessageSerializer,
                                PostMessageSerializer)


# Create your views here.

class GetMessageList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = GetMessageSerializer


class PostMessage(generics.CreateAPIView):
    serializer_class = PostMessageSerializer


