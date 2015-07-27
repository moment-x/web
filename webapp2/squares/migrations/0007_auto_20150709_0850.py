# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squares', '0006_auto_20150702_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textentity',
            name='addressArr',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='textentity',
            name='imgArr',
            field=models.BinaryField(null=True),
        ),
    ]
