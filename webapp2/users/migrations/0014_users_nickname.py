# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150717_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='nickname',
            field=models.CharField(null=True, max_length=100, unique=True),
        ),
    ]
