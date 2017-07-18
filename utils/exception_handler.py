from rest_framework.views import exception_handler
from rest_framework import exceptions

'''
Default: 1
AuthenticationFailed: 2
PermissionDenied : 3

'''


def my_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # print(exc)
    # print(context)
    if response is not None:
        if isinstance(exc, exceptions.AuthenticationFailed):
            response.data['error_code'] = 2
        elif isinstance(exc, exceptions.PermissionDenied):
            response.data['error_code'] = 3
        else:
            response.data['error_code'] = 1
    return response
