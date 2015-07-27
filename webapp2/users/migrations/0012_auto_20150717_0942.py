# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150715_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='friendss',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='friendss_rel_+'),
        ),
        migrations.AlterField(
            model_name='frdreq',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver_FrdReq'),
        ),
        migrations.AlterField(
            model_name='frdreq',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender_FrdReq'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='guest',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='guest_Friend'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='host',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='host_Friend'),
        ),
    ]
