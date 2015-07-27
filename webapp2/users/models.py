from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import check_password
from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from django.db import models
from django.contrib.sessions.models import Session


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
    Img = models.CharField(max_length=1048576, null=True)
    token = models.CharField(max_length=1076, null=True)

    friends = models.ManyToManyField('self')
    friends_request = models.ManyToManyField('self')
    #
    USERNAME_FIELD = 'username'
    #
    objects = UserManager()


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    session = models.ForeignKey(Session)

class Test(models.Model):
    text = models.CharField(max_length=100, null=True)