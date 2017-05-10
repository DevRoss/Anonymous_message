from django.contrib import auth
from rest_framework.views import APIView
from .serializer import (UserLoginSerializer,
                         )
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import parsers
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import generics
from utils.authentication import ExpiringTokenAuthentication


class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.JSONParser,)

    def __create_token(self, user):

        """
        :param user: user instance 
        :return: new token
        """
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            token.delete()
        token = Token.objects.create(user=user)
        return token

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['username'])
            token = self.__create_token(user=user)
            ret_json = {
                "Token": token.key,
                "error_code": 0
            }
            # new_data = serializer.data
            return Response(ret_json, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (ExpiringTokenAuthentication,)

    def get(self, request):
        user = request.user
        user = Token.objects.get(user=user)
        user.delete()
        ret_json = {
            'error_code': 0
        }
        return Response(ret_json, status=status.HTTP_200_OK)
