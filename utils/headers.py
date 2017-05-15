from rest_framework import HTTP_HEADER_ENCODING


def get_authorization_header(request):
    '''
    Return AUTHENTICATION CODE 
    :param request: 
    :return: 
    '''
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, type('')):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth
