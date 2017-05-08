from django.conf.urls import url
from .views import UserLogin, UserLogout
urlpatterns = [
    url(r'userlogin/?$', UserLogin.as_view(), name='user_login'),
    url(r'userlogout/?$', UserLogout.as_view(), name='user_logout'),
]
