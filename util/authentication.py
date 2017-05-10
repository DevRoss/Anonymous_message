from .headers import get_authorization_header
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
import datetime
from django.utils import timezone


class ExpiringTokenAuthentication(BaseAuthentication):
    model = Token

    def authenticate(self, request):
        auth = get_authorization_header(request)
        if not auth:
            return None
        try:
            token = auth.split()
            token = token[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        token_cache = 'token_' + key
        cache_user = cache.get(token_cache)
        if cache_user:
            return (cache_user, key)
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Authenticate failed.')
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('The user is forbidden.')
        utc_now = timezone.now()
        if token.created < utc_now - timezone.timedelta(hours=24 * 30):
            raise exceptions.AuthenticationFailed('Token has been expired.')
        if token:
            token_cache = 'token_' + key
            cache.set(token_cache, token.user, 24 * 7 * 60 * 60)
        return (token.user, token)

    def authenticate_header(self, request):
        return 'Token'
