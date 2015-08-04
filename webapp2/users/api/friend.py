from django.contrib.auth.decorators import login_required        # django
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .resps import json_resps                                    # project
from users.models import Users

import base64                                                    # python


ADD_POST_FIELD_FRIEND = 'friend'
RES_POST_FIELD_FRIEND = 'friend'
RES_POST_FIELD_DECISION = 'decision'
RES_DECISION_YES = 'yes'
JSON_RESPONSE_DOES_NOT_EXIST = 'DOES_NOT_EXIST'
JSON_RESPONSE_SUCCEED = 'SUCCEEDED'
USERS_MODEL_FIELD_USERNAME = 'username'
USERS_MODEL_FIELD_NICKNAME = 'username'
LIST_PAIR_USERNAME = 'username'
LIST_PAIR_NICKNAME = 'nickname'
AVATAR_POST_FIELD_USERNAME = 'username'
UTF8 = 'utf-8'
VALIDATE_POST_FIELD_USERNAMES = 'usernames[]'


@csrf_exempt
@login_required()
def add_req(request):
    data = request.POST.dict()
    try:
        friend = Users.objects.get(username=data[ADD_POST_FIELD_FRIEND])
    except Users.DoesNotExist:
        return json_resps[JSON_RESPONSE_DOES_NOT_EXIST]
    request.user.friends_request.add(friend)
    from ..tasks import add_req_push
    add_req_push(request.user, friend)
    return json_resps[JSON_RESPONSE_SUCCEED]


@csrf_exempt
@login_required()
def get_req(request):
    senders = request.user.friends_request.values_list(USERS_MODEL_FIELD_USERNAME, flat=True)
    return JsonResponse(list(senders),  safe=False)


@csrf_exempt
@login_required()
def res_req(request):
    friend = Users.objects.get(username=request.POST[RES_POST_FIELD_FRIEND])
    request.user.friends_request.remove(friend)
    if request.POST[RES_POST_FIELD_DECISION] == RES_DECISION_YES:
        request.user.friends.add(friend)
    return json_resps[JSON_RESPONSE_SUCCEED]


@csrf_exempt
@login_required()
def frd_list(request):
    friends = request.user.friends.values_list(USERS_MODEL_FIELD_USERNAME, USERS_MODEL_FIELD_NICKNAME)
    username, nickname = zip(*friends)
    pair = {LIST_PAIR_USERNAME: username, LIST_PAIR_NICKNAME: nickname}
    return JsonResponse(pair, safe=False)



@csrf_exempt
@login_required
def validate(request):
    this_user = request.user
    users_to_be_validated = request.POST.getlist('usernames[]')
    users_not_existed = [entry for entry in users_to_be_validated
                       if not Users.objects.filter(username=entry).exists()]
    users_existed = [user for user in users_to_be_validated if user not in users_not_existed]
    this_user_friend_set = this_user.friends.all()
    users_already_friends = [user for user in users_existed if this_user_friend_set.filter(username=user).exists()]
    users_not_yet = [user for user in users_existed if user not in users_already_friends]
    return JsonResponse({'users_not_existed': users_not_existed,
                         'users_already_friends': users_already_friends,
                         'users_not_yet': users_not_yet})


@csrf_exempt
@login_required
def v2(request):
    users_to_be_val = request.POST.getlist('usernames[]')
    valid_query = Users.objects.filter(pk__in=users_to_be_val)
    invalid = [entry for entry in users_to_be_val
               if entry not in valid_query.values_list("username", flat=True)]
    users_already_friends = Users.objects.all().filter(friends=4)
    return HttpResponse(str(users_already_friends))


