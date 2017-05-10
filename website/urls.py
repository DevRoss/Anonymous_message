from django.conf.urls import url
from website.views import (GetMessageList,
                           PostMessage,
                           PostMessageDev,
                           GetSS
                           )

urlpatterns = [
    url(r'messagelist/?$', GetMessageList.as_view()),
    url(r'postmessage/?$', PostMessage.as_view()),
    url(r'postmessagedev/?$', PostMessageDev.as_view()),
    url(r'getss/?$', GetSS.as_view()),
]
