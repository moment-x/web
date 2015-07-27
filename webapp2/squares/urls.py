from django.conf.urls import url
from .api import basic

urlpatterns = [
    url(r'^(?P<type>.*)/upload$', basic.upload, name='upload'),
    url(r'^(?P<type>.*)/download$', basic.download, name='download'),
    url(r'^send$', basic.send),
]
