# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20150701_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Img',
            field=models.CharField(max_length=1048576, null=True),
        ),
    ]
