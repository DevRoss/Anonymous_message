from website.models import Messages, SS
from rest_framework import generics
from rest_framework.views import APIView
from website.serializer import *
from rest_framework import parsers
from rest_framework import filters
from utils.authentication import ExpiringTokenAuthentication
from rest_framework import permissions
from rest_framework.authtoken.models import Token


# from rest_framework.response import Response
# from rest_framework import status


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


class GetSS(generics.ListAPIView):
    queryset = SS.objects.all()
    serializer_class = GetSSSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
