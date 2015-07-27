from django.http import HttpResponse,JsonResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from users.models import Users
from .resps import json_resps

from django.http import JsonResponse
import base64


@csrf_exempt
@login_required()
def add_req(request):
    data = request.POST.dict()
    try:
        friend = Users.objects.get(username=data['friend'])
    except Users.DoesNotExist:
        return json_resps['FRIEND_ALREADY_EXISTS']
    request.user.friends_request.add(friend)

    from ..tasks import add_req_push_n
    add_req_push_n(request.user, friend)
    # 2b
    from ..tasks import add_req_push
    add_req_push(request.user, friend)
    # 2b
    return json_resps['SUCCEEDED']


@csrf_exempt
@login_required()
def get_req(request):
    senders = request.user.friends_request.values_list('username', flat=True)
    return JsonResponse(list(senders),  safe=False)


@csrf_exempt
@login_required()
def res_req(request):
    friend = Users.objects.get(username=request.POST['friend'])
    request.user.friends_request.remove(friend)
    if request.POST['decision'] == 'yes':
        request.user.friends.add(friend)
    return json_resps['SUCCEEDED']


@csrf_exempt
@login_required()
def frd_list(request):
    friends = request.user.friends.values_list('username', 'nickname')
    username, nickname = zip(*friends)
    pair = {'username': username, 'nickname': nickname}
    return JsonResponse(pair, safe=False)


@csrf_exempt
def get_avatar(request):
    img = Users.objects.get(username=request.POST['username']).Img
    return JsonResponse(base64.b64encode(img).decode('utf-8'), safe=False)


# @csrf_exempt
# @login_required
# def test(request):
#     ip_address = request.META.get('REMOTE_ADDR', '')
#     content = request.session.items()
#     return JsonResponse((dict(content), ip_address), safe=False)


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


