from django.conf.urls import url
from website.views import *

urlpatterns = [
    url(r'messagelist/?$', GetMessageList.as_view()),
    url(r'postmessage/?$', PostMessage.as_view()),
    url(r'postmessagedev/?$', PostMessageDev.as_view()),
    url(r'getss/?$', GetSS.as_view()),
    url(r'addss/?$', AddSS.as_view()),
    url(r'additem/?$', AddItem.as_view()),
    url(r'get_shot/?$', GetShot.as_view()),
    url(r'create_shot/?$', CreateShot.as_view()),
]
