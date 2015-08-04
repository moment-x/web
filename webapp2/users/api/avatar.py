from qimage.image import multipleEntrySign

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from users.models import UserAvatar, Users

import uuid, hashlib

from qimage import image
from webapp2 import settings

@csrf_exempt
def signUploadAvatar(request):
    userid = request.user.username
    fileid = 'avatar' + '-' + userid + '-' + uuid.uuid4()
    hashStr = image.APPID + fileid + settings.SECRET_KEY
    m = hashlib.md5()
    m.update(hashStr)
    md5 = m.hexdigest()
    retDic = {
        'fileid': fileid,
        'sign': multipleEntrySign(fileid),
        'md5': md5
    }
    return JsonResponse(retDic, safe=False)


def qimage_avatar_callback(request):
    data = request.POST.dict()
    hashStr = image.APPID + data['fileid'] + settings.SECRET_KEY
    m = hashlib.md5()
    m.update(hashStr)
    md5 = m.hexdigest()
    if data['magic_context'] == md5:
        username = data['fileid'].split('-')[1]
        user = Users.objects.get(username=username)
        UserAvatar.objects.create(user=user)