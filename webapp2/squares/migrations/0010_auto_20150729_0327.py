# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squares', '0009_pendingdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendingdata',
            name='json',
        ),
        migrations.AddField(
            model_name='pendingdata',
            name='data',
            field=models.BinaryField(null=True),
        ),
    ]
