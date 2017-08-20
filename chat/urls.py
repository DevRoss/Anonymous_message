from django.conf.urls import url
from .views import CreateRoom, EnterRoom

urlpatterns = [
    url(r'create$', CreateRoom.as_view()),
    url(r'enter/(?P<label>[\w\d]+)', EnterRoom.as_view()),
]
