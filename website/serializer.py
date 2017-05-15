from rest_framework import serializers
from website.models import Messages, User, SS
from django.utils import dateformat
import base64
from Anonymous_message.settings import MEDIA_ROOT

# from rest_framework.exceptions import ValidationError
# from django.contrib.auth.models import User

'''
数据序列化
'''


# 获取留言列表
class GetMessageSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    class Meta:
        model = Messages
        fields = ('content', 'time')

    def get_time(self, obj):
        return dateformat.format(obj.time, 'U')


# 发表留言
class PostMessageSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    class Meta:
        model = Messages
        fields = ('content', 'time')

    def get_time(self, obj):
        return dateformat.format(obj.time, 'U')


class AddOrGetSSSerializer(serializers.ModelSerializer):
    ss_link = serializers.SerializerMethodField()

    class Meta:
        model = SS
        fields = ('server_name', 'ip', 'port', 'password', 'region', 'encrypt_method', 'ss_link', 'qr_code')

    def get_ss_link(self, obj):
        config = '{encrypt_method}:{password}@{ip}:{port}'
        config = config.format(encrypt_method=obj.encrypt_method, password=obj.password, ip=obj.ip, port=obj.port)
        server_name = str('#' + obj.server_name).encode()
        ret = b'ss://' + base64.urlsafe_b64encode(config.encode()) + server_name
        return ret
