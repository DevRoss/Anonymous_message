from rest_framework import serializers
from website.models import Messages, User
from django.utils import dateformat
from rest_framework.exceptions import ValidationError
from django.db.models import Q
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


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data.get("password", None)
        if not username:
            raise ValidationError('A username or email is required to login.')
        user = User.objects.filter(username=username)
        print(user)
        if user.exists():
            print(user.count())
            user_obj = user.first()
        else:
            raise ValidationError("Incorrect username")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect password. Please try again.')
        return data
