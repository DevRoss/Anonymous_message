from django.conf.urls import url
from website.views import (GetMessageList,
                           PostMessage,
                           PostMessageDev,
                           Login)

urlpatterns = [
    url(r'messagelist/$', GetMessageList.as_view()),
    url(r'postmessage/$', PostMessage.as_view()),
    url(r'postmessagedev/$', PostMessageDev.as_view()),
    url(r'login/$', Login.as_view())
]
