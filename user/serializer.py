from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework import exceptions

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data.get("password", None)
        if not username:
            raise exceptions.AuthenticationFailed('A username or email is required to login.')
        user = User.objects.filter(username=username)
        print(user)
        if user.exists():
            user_obj = user.first()
        else:
            raise exceptions.AuthenticationFailed("Incorrect username")
        if user_obj:
            if not user_obj.check_password(password):
                raise exceptions.AuthenticationFailed('Incorrect password. Please try again.')
        # data['token'] = Token.objects.create(user=user_obj)
        return data
