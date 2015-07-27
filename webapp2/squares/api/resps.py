from django.http import JsonResponse

responses = {
    'SUCCEEDED': 200,
    'UNHANDLED': 1,
    'CONTACT_UNAVAILABLE': 201,
    'WRONG_PASSWORD': 202,
    'NOT_LOGGED_IN': 203,
    'DOES_NOT_EXIST':204,
    'FRIEND_ALREADY_EXISTS': 205,
    'TIMEOUT': 206,
}

json_resps = {key: JsonResponse({'errcode': value}) for key, value in responses.items()}
