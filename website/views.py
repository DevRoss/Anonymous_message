from website.models import Messages, SS
from rest_framework import generics
from rest_framework.views import APIView
from website.serializer import *
from rest_framework import parsers
from rest_framework import filters
from utils.authentication import ExpiringTokenAuthentication
from rest_framework import permissions
from utils.ss_config import generate_qc, generate_ss_uri
from rest_framework.response import Response
from rest_framework import status
from price_tracker.price_tracker.jingdong.jd_api import add_item
from utils.get_page import Browser

# from rest_framework.response import Response
# from rest_framework import status

'''Message相关API'''


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


'''SS相关API'''


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
        '''
        旧写法
        serializer.validated_data['qr_code'] = '/'.join(['http://'+DOMAIN, 'media', 'QR', file_name])
        '''

        # media/QR/file_name
        serializer.validated_data['qr_code'] = '/'.join(['media', 'QR', file_name])
        # print(serializer.validated_data['qr_code'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer.validated_data['error_code'] = 0
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)


'''爬虫相关API'''


class AddItem(APIView):
    parser_classes = (parsers.JSONParser,)
    serializer_class = AddItemSerializer

    def post(self, request, *args, **kwargs):
        serializer = AddItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer.validated_data)
            if (add_item(serializer.validated_data['item_url'])):
                ret = {'error_code': 0}
                return Response(ret, status=status.HTTP_202_ACCEPTED)
        ret = {'error_code': 1}
        return Response(ret, status=status.HTTP_400_BAD_REQUEST)


class CreateShot(generics.CreateAPIView):
    serializer_class = AddShotSerializer
    parser_classes = (parsers.JSONParser,)

    def post(self, requeset, *args, **kwargs):
        serializer = AddShotSerializer(data=requeset.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['file_path'] = Browser().get_full_page_shot(serializer.validated_data.get('url'))
            print(serializer.validated_data['file_path'])
            self.perform_create(serializer)
            serializer.validated_data['error_code'] = 0
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=self.headers)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetShot(generics.ListAPIView):
    serializer_class = GetShotSerializer
    queryset = PageShot.objects.all()
