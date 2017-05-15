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
from utils.qc_generator import generate_qc
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


class AddOrGetSS(generics.ListCreateAPIView):
    queryset = SS.objects.all()
    serializer_class = AddOrGetSSSerializer
    authentication_classes = (ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 如果表单验证成功
        # 生成二维码并储存路径
        generate_qc(serializer.data['ss_link'], serializer.data['server_name'])
        file_name = serializer.data['server_name'] + '.png'
        serializer.data['qr_code'] = os.path.join(MEDIA_ROOT, file_name)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
