from django.db import models
from django.conf import settings


class PictureEntity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    img = models.CharField(max_length=1048576, null=True)
    imgId = models.CharField(max_length=100, null=True)
    imgText = models.CharField(max_length=100, null=True)


class TextEntity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    titImg = models.CharField(max_length=1048576, null=True)
    title = models.CharField(max_length=1000, null=True)
    text = models.CharField(max_length=1000, null=True)
    coverImg = models.CharField(max_length=1048576, null=True)
    textId = models.CharField(max_length=100, null=True)
    width = models.CharField(max_length=100, null=True)
    height = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)


class WebEntity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    urlStr = models.CharField(max_length=100, null=True)
    coverImg = models.CharField(max_length=1048576, null=True)
    pageId = models.CharField(max_length=100, null=True)
    pageText = models.CharField(max_length=100, null=True)


class Cards(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    cardtitle = models.CharField(max_length=100, null=True)
    cardimg = models.BinaryField(null=True)
    cardtag = models.CharField(max_length=100, null=True)
    cardid = models.CharField(max_length=100, null=True)
    first = models.CharField(max_length=100, null=True)


class TextEntityExtra(models.Model):
    idStr = models.CharField(max_length=100, null=True)
    textId = models.CharField(max_length=100, null=True)
    img = models.CharField(max_length=1048576, null=True)
    local = models.CharField(max_length=100, null=True)

class PendingData(models.Model):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL)
    json = models.CharField(max_length=1048576, null=True)