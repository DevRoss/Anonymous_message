from website.models import Messages, SS
from rest_framework import generics
from rest_framework.views import APIView
from website.serializer import *
from rest_framework import parsers
from rest_framework import filters
from utils.authentication import ExpiringTokenAuthentication
from rest_framework import permissions
from Anonymous_message.settings import MEDIA_ROOT
import os
from utils.ss_config import generate_qc, generate_ss_uri
from rest_framework.response import Response
from rest_framework import status


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


class AddSS(generics.CreateAPIView):
    serializer_class = AddSSSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (parsers.JSONParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 如果表单验证成功
        # 生成二维码并储存路径
        ss_uri = generate_ss_uri(serializer=serializer)
        generate_qc(ss_uri, serializer.validated_data['server_name'])
        file_name = serializer.validated_data['server_name'] + '.png'
        serializer.validated_data['qr_code'] = os.path.join(MEDIA_ROOT, 'QR', file_name)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer.validated_data['error_code'] = 0
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)
