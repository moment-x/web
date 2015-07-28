from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError

from users.models import Users
from .resps import json_resps




@csrf_exempt
def signup(request):
    data = request.POST.dict()
    data['nickname'] = data['username']
    try:
        Users.objects.create_user(**data)
    except IntegrityError:
        return json_resps['CONTACT_UNAVAILABLE']
    return json_resps['SUCCEEDED']


@csrf_exempt
def logout(request):
    auth_logout(request)
    return json_resps['SUCCEEDED']


@csrf_exempt
def login(request):
    data = request.POST.dict()
    user = authenticate(**data)
    if user:
        user.token = data['deviceTokenStr']
        user.save()
        auth_login(request, user)
        return json_resps['SUCCEEDED']
    else:
        return json_resps['WRONG_PASSWORD']


@csrf_exempt
def test(request):
    return HttpResponse('asdf')