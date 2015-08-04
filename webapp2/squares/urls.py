from django.conf.urls import url
from .api import basic

urlpatterns = [
    # url(r'^(?P<type>.*)/upload$', basic.upload, name='upload'),
    url(r'^send$', basic.send),
    url(r'^receive/(?P<id>.*)$', basic.receive),
]
