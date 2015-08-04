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
def send(request):
    from ..tasks import upload_pending_data_notify_receiver
    import json
    receiver = Users.objects.get(username=request.POST['headDic[receiver]'])
    upload_pending_data_notify_receiver.delay(request.user, receiver, json.dumps(request.POST.dict()))
    return JsonResponse({'error': 200})


@csrf_exempt
@login_required
def receive(request, id):
    pendingdata = PendingData.objects.get(id=id)
    if request.user.id == pendingdata.receiver_id:
        data = pendingdata.json
        dataim = json.loads(data)
        dataim['errcode'] = 0
        return JsonResponse(dataim)
    else:
        return JsonResponse(
            {
             'errorcode': 1
             }
        )