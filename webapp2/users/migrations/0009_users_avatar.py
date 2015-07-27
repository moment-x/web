# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150627_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.BinaryField(null=True),
        ),
    ]
