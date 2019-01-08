from django.urls import re_path
from .views import servidores,serverInfo
urlpatterns = [
    re_path(r'^serverInfo/(?P<serverName>[A-Z a-z]+)/',serverInfo,name="serverInfo"),
]

