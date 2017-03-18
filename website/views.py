# from django.shortcuts import render
from website.models import Messages, User
from django.db.models import Q
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.views import APIView
from website.serializer import (GetMessageSerializer,
                                PostMessageSerializer,
                                UserSerializer)
from rest_framework import parsers
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


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


class Login(APIView):
    authentication_classes = (SessionAuthentication, )
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
