from django.conf.urls import url
from .views import CreateRoom, EnterRoom

urlpatterns = [
    url(r'anonymous-chat/create$', CreateRoom.as_view()),
    url(r'anonymous-chat/enter/(?P<label>[\w\d]+)', EnterRoom.as_view()),
]
