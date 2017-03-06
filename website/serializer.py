from rest_framework import serializers
from website.models import Messages
from django.utils import dateformat


class GetMessageSerializer(serializers.ModelSerializer):
    unix_time = serializers.SerializerMethodField()

    class Meta:
        model = Messages
        fields = ('content', 'unix_time')

    def get_unix_time(self, obj):
        return dateformat.format(obj.time, 'U')

# class PostMessageSerializer(serializers.ModelSerializer):
#
