# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(null=True, max_length=1076),
        ),
    ]
