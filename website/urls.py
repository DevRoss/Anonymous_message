from django.conf.urls import url
from website.views import (GetMessageList,
                           PostMessage)

urlpatterns = [
    url(r'messagelist/$', GetMessageList.as_view()),
    url(r'postmessage/$', PostMessage.as_view()),
]
