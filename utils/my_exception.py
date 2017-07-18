from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import ugettext_lazy as _


class UserDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('User does not exist.')
    default_code = 'user_does_not_exist.'
