# from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter

from website.models import Messages
from website.serializer import (GetMessageSerializer,
                                PostMessageSerializer)
from rest_framework import parsers
from rest_framework import filters


# Create your views here.

class GetMessageList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = GetMessageSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('content',)
    ordering = ('-time',)


class PostMessage(generics.CreateAPIView):
    serializer_class = PostMessageSerializer
    parser_classes = (parsers.JSONParser,)


class PostMessageDev(generics.CreateAPIView):
    serializer_class = PostMessageSerializer
    parser_classes = (parsers.FormParser,)
