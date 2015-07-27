# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150627_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frdreq',
            name='receiver',
            field=models.ForeignKey(related_name='receiver_frdreq', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='frdreq',
            name='sender',
            field=models.ForeignKey(related_name='sender_frdreq', to=settings.AUTH_USER_MODEL),
        ),
    ]
