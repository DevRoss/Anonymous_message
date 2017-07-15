from django.conf.urls import url
from website.views import (GetMessageList,
                           PostMessage,
                           PostMessageDev,
                           GetSS,
                           AddSS,
                           AddItem
                           )

urlpatterns = [
    url(r'messagelist/?$', GetMessageList.as_view()),
    url(r'postmessage/?$', PostMessage.as_view()),
    url(r'postmessagedev/?$', PostMessageDev.as_view()),
    url(r'getss/?$', GetSS.as_view()),
    url(r'addss/?$', AddSS.as_view()),
    url(r'additem/?$', AddItem.as_view()),
]
