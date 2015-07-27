from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserSession
from django.http import JsonResponse, HttpResponse

from .models import Users


HASH_SESSION_KEY = '_auth_user_hash'


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    Users.objects.delete_user_sessions(user)
    request.session.save()
    # It can be access only after saved
    UserSession.objects.get_or_create(
        user=user,
        session_id=request.session.session_key
    )
    UserSession.objects.filter(user=user)
