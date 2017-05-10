from rest_framework.views import exception_handler


def my_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # print(exc)
    # print(context)
    if response is not None:
        response.data['error_code'] = 1
    return response
