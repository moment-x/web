# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150627_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='identifier',
            new_name='username',
        ),
    ]
