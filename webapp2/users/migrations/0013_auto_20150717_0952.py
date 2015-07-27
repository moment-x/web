# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150717_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frdreq',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='frdreq',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='host',
        ),
        migrations.RemoveField(
            model_name='users',
            name='friendss',
        ),
        migrations.AddField(
            model_name='users',
            name='friends',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friends_rel_+'),
        ),
        migrations.AddField(
            model_name='users',
            name='friends_request',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friends_request_rel_+'),
        ),
        migrations.DeleteModel(
            name='FrdReq',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
