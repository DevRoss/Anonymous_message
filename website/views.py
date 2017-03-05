# from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
from website.models import Messages
from website.serializer import GetMessageSerializer


# Create your views here.

class GetMessageList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = GetMessageSerializer