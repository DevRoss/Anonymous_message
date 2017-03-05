from website.views import GetMessageList
from django.conf.urls import url

urlpatterns = [
    url(r'messagelist/$', GetMessageList.as_view()),
]