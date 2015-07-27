from django.conf.urls import url

from .api import basic
from .api import friend



urlpatterns = [
    url(r'^signup$', basic.signup),
    url(r'^login$', basic.login),
    url(r'^logout$', basic.logout),
    #
    url(r'^addreq$', friend.add_req),
    url(r'^getreq$', friend.get_req),
    url(r'^resreq$', friend.res_req),
    url(r'^frdlist$', friend.frd_list),
    url(r'^getavatar$', friend.get_avatar),
    #
    url(r'^test$', basic.test),
    url(r'^validate$', friend.validate),
    url(r'^v2$', friend.v2),

]
