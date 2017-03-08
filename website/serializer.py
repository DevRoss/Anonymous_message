from rest_framework import serializers
from website.models import Messages
from django.utils import dateformat

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
