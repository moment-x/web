from django.conf.urls import url        # django

from .api import basic, friend, avatar    # project


urlpatterns = [
    url(r'^signup$', basic.signup),
    url(r'^login$', basic.login),
    url(r'^logout$', basic.logout),
    #
    url(r'^addreq$', friend.add_req),
    url(r'^getreq$', friend.get_req),
    url(r'^resreq$', friend.res_req),
    url(r'^frdlist$', friend.frd_list),
    #
    url(r'^validate$', friend.validate),
    #
    url(r'^avatarsign$', avatar.signUploadAvatar),
    url(r'^qimage_avatar_callback$', avatar.qimage_avatar_callback),
]
