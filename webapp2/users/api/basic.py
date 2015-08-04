from django.contrib.auth import authenticate                # django
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .resps import json_resps                               # project
from users.models import Users


SIGNUP_POST_FIELD_NICKNAME = 'nickname'
SIGNUP_POST_FIELD_USERNAME = 'username'
LOGIN_POST_FIELD_DEVICE_TOKEN = 'deviceTokenStr'
JSON_RESPONSE_SUCCEED = 'SUCCEEDED'
JSON_RESPONSE_WRONG_PASSWORD = 'WRONG_PASSWORD'
JSON_RESPONSE_CONTACT_UNAVAILABLE = 'CONTACT_UNAVAILABLE'



@csrf_exempt
def signup(request):
    data = request.POST.dict()
    data[SIGNUP_POST_FIELD_NICKNAME] = data[SIGNUP_POST_FIELD_USERNAME]
    try:
        Users.objects.create_user(**data)
    except IntegrityError:
        return json_resps[JSON_RESPONSE_CONTACT_UNAVAILABLE]
    return json_resps[JSON_RESPONSE_SUCCEED]


@csrf_exempt
def logout(request):
    auth_logout(request)
    return json_resps[JSON_RESPONSE_SUCCEED]


@csrf_exempt
def login(request):
    data = request.POST.dict()
    user = authenticate(**data)
    if user:
        user.token = data[LOGIN_POST_FIELD_DEVICE_TOKEN]
        user.save()
        auth_login(request, user)
        return json_resps[JSON_RESPONSE_SUCCEED]
    else:
        return json_resps[JSON_RESPONSE_WRONG_PASSWORD]

