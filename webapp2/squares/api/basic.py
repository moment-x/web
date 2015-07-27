from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .resps import json_resps
from squares.models import PictureEntity, WebEntity, TextEntity, Cards,TextEntityExtra
from squares.models import PendingData
from users.models import Users

import json

@csrf_exempt
@login_required
def upload(request, type):
    data = request.POST.dict()
    data['user'] = request.user
    {
        'pic': PictureEntity,
        'text': TextEntity,
        'textextra': TextEntityExtra,
        'web': WebEntity,
        'card': Cards,
    }[type].objects.create(**data)
    return json_resps['SUCCEEDED']


@csrf_exempt
@login_required
def download(request, type):
    user = request.user
    result = {
        'pic': PictureEntity,
        'text': TextEntity,
        'web': WebEntity,
        'card': Cards,
        'textextra': TextEntityExtra,
    }[type].objects.filter(user=user).values()
    return JsonResponse(list(result), safe=False)


@csrf_exempt
@login_required
def send(request):
    return JsonResponse({'gg': str(request.body)})
    # import json
    # json_data = json.dumps(request.POST)
    # return JsonResponse({'gg': request.POST.dict()})
    # receiver = Users.objects.get()
    # PendingData.objects.create(users=receiver, json=request.POST)