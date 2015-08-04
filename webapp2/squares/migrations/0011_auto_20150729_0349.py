# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0010_auto_20150729_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingdata',
            name='data',
        ),
        migrations.AddField(
            model_name='pendingdata',
            name='json',
            field=models.CharField(max_length=1048576, null=True),
        ),
    ]
