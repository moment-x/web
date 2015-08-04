from django.conf import settings                         #django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.sessions.models import Session
from django.db import models

MODEL_SELF = 'self'
FIELD_USERNAME = 'username'

class UserManager(BaseUserManager):
    def create_user(self, password, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()

    def delete_user_sessions(self, user):
        user_sessions = UserSession.objects.filter(user=user)
        for user_session in user_sessions:
            user_session.session.delete()

class Users(AbstractBaseUser):
    username = models.CharField(max_length=100, null=True, unique=True, db_index=True)
    nickname = models.CharField(max_length=100, null=True, unique=True)
    year = models.CharField(max_length=100, null=True)
    month = models.CharField(max_length=100, null=True)
    day = models.CharField(max_length=100, null=True)
    constellation = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=100, null=True)
    cardNum = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    token = models.CharField(max_length=1076, null=True)

    friends = models.ManyToManyField(MODEL_SELF)
    friends_request = models.ManyToManyField(MODEL_SELF)
    #
    USERNAME_FIELD = FIELD_USERNAME
    #

    objects = UserManager()


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    session = models.ForeignKey(Session)


class UserAvatar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    url = models.CharField(max_length=200, null=True)