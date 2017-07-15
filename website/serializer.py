from rest_framework import serializers
from website.models import Messages, User, SS
from django.utils import dateformat
import base64
from Anonymous_message.settings import DOMAIN
from rest_framework.validators import ValidationError, BaseUniqueForValidator

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


class GetSSSerializer(serializers.ModelSerializer):
    ss_uri = serializers.SerializerMethodField()

    class Meta:
        model = SS
        fields = ('server_name', 'ip', 'port', 'password', 'region', 'encrypt_method', 'ss_uri', 'qr_code')

    def get_ss_uri(self, obj):
        config = '{encrypt_method}:{password}@{ip}:{port}'
        config = config.format(encrypt_method=obj.encrypt_method, password=obj.password, ip=obj.ip, port=obj.port)
        server_name = str('#' + obj.server_name).encode()
        ret = b'ss://' + base64.urlsafe_b64encode(config.encode()) + server_name
        return ret

    def get_qr_code(self, obj):
        url = obj.qr_code
        # 兼容旧写法
        if 'tofun.online' in url:
            return url.replace('tofun.online', DOMAIN)
        else:
            new_url = '/'.join(['http://' + DOMAIN, url])
            return new_url


class AddSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SS
        fields = ('server_name', 'ip', 'port', 'password', 'region', 'encrypt_method')


class AddItemSerializer(serializers.Serializer):
    def validate_item_url(self, value):
        if 'jingdong' in value:
            pass
        elif 'jd' in value:
            pass
        else:
            raise ValidationError('This is not a jd url')
        return value

    item_url = serializers.URLField()
